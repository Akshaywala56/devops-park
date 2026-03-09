import boto3
import time

def run_query(query: str, database: str, output_bucket: str):
    athena = boto3.client("athena")

    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={"Database": database},
        ResultConfiguration={"OutputLocation": output_bucket}
    )

    query_execution_id = response["QueryExecutionId"]

    # Wait for completion
    while True:
        status = athena.get_query_execution(QueryExecutionId=query_execution_id)
        state = status["QueryExecution"]["Status"]["State"]
        if state in ["SUCCEEDED", "FAILED", "CANCELLED"]:
            break
        time.sleep(1)

    if state != "SUCCEEDED":
        raise Exception(f"Athena query {state}")

    # Fetch results
    results_paginator = athena.get_paginator("get_query_results")
    results = []
    for page in results_paginator.paginate(QueryExecutionId=query_execution_id):
        for row in page["ResultSet"]["Rows"]:
            results.append([col.get("VarCharValue") for col in row["Data"]])

    return query_execution_id, results
