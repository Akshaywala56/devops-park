import boto3
from datetime import date, timedelta

ce = boto3.client("ce")

def cost_summary():
    end = date.today()
    start = end - timedelta(days=7)

    resp = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start.strftime("%Y-%m-%d"),
            "End": end.strftime("%Y-%m-%d"),
        },
        Granularity="DAILY",
        Metrics=["UnblendedCost"],
    )

    daily = []
    total = 0.0

    for r in resp["ResultsByTime"]:
        amount = float(r["Total"]["UnblendedCost"]["Amount"])
        total += amount
        daily.append({
            "date": r["TimePeriod"]["Start"],
            "cost": round(amount, 2)
        })

    return {
        "currency": resp["ResultsByTime"][0]["Total"]["UnblendedCost"]["Unit"],
        "total_last_7_days": round(total, 2),
        "daily_cost": daily
    }
