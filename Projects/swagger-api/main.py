from fastapi import FastAPI, Query,Body
from services.ec2 import ec2_insights
from services.cost import cost_summary
from services.s3 import get_s3_insights
import boto3
from services.athena import run_query

app = FastAPI(title="DevOps Read Only Insights API")

@app.get("/")
def root():
    sts = boto3.client("sts")
    identity = sts.get_caller_identity()

    return {
        "message": "DevOps Insights API is running",
        "account": identity["Account"],
        "user": identity["Arn"]
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/aws/ec2/insights")
def get_ec2_insights(days: int = 7):
    return ec2_insights(days)

@app.get("/aws/cost/summary")
def get_cost():
    return cost_summary()

@app.get("/aws/s3/insights")
def s3_insights(
    bucket: str = Query(..., description="Exact bucket name"),
    max_objects: int = Query(5000, le=10000),
    timeout_seconds: int = Query(10, le=30)
):
    return get_s3_insights(
        bucket_name=bucket,
        max_objects=max_objects,
        timeout_seconds=timeout_seconds
    )

@app.post("/aws/athena/query")
def athena_query(
    query: str = Body(...),
    database: str = Body(...),
    output_bucket: str = Body(...)
):
    query_id, results = run_query(query, database, output_bucket)
    return {"query_execution_id": query_id, "results": results}