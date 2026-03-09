import boto3
from datetime import datetime, timedelta, timezone

ec2 = boto3.client("ec2")
cw = boto3.client("cloudwatch")

def ec2_insights(days: int):
    resp = ec2.describe_instances()

    total = 0
    running = 0
    idle_instances = []

    end = datetime.now(timezone.utc)
    start = end - timedelta(days=days)

    for r in resp["Reservations"]:
        for i in r["Instances"]:
            total += 1

            if i["State"]["Name"] != "running":
                continue

            running += 1
            instance_id = i["InstanceId"]

            metrics = cw.get_metric_data(
                MetricDataQueries=[
                    {
                        "Id": "cpu",
                        "MetricStat": {
                            "Metric": {
                                "Namespace": "AWS/EC2",
                                "MetricName": "CPUUtilization",
                                "Dimensions": [
                                    {"Name": "InstanceId", "Value": instance_id}
                                ],
                            },
                            "Period": 86400,
                            "Stat": "Average",
                        },
                        "ReturnData": True,
                    }
                ],
                StartTime=start,
                EndTime=end,
            )

            values = metrics["MetricDataResults"][0]["Values"]
            avg_cpu = round(sum(values) / len(values), 2) if values else 0

            if avg_cpu < 5:
                idle_instances.append({
                    "instance_id": instance_id,
                    "average_cpu": avg_cpu
                })

    return {
        "summary": {
            "total_instances": total,
            "running_instances": running,
            "idle_threshold_cpu": "5 percent",
            "analysis_days": days
        },
        "idle_instances": idle_instances,
        "message": "No idle EC2 found" if not idle_instances else "Idle EC2 detected"
    }
