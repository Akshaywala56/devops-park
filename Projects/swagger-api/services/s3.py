import boto3
import time
from botocore.exceptions import ClientError

s3 = boto3.client("s3")

def get_s3_insights(bucket_name: str, max_objects: int, timeout_seconds: int):
    start_time = time.time()

    try:
        # Check bucket exists and access
        s3.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        return {
            "error": "Bucket not accessible",
            "details": str(e)
        }

    paginator = s3.get_paginator("list_objects_v2")

    total_size = 0
    object_count = 0

    try:
        for page in paginator.paginate(Bucket=bucket_name):
            if "Contents" not in page:
                break

            for obj in page["Contents"]:
                total_size += obj["Size"]
                object_count += 1

                # object limit guard
                if object_count >= max_objects:
                    return _response(
                        bucket_name,
                        object_count,
                        total_size,
                        "Stopped: max object limit reached"
                    )

                # timeout guard
                if time.time() - start_time > timeout_seconds:
                    return _response(
                        bucket_name,
                        object_count,
                        total_size,
                        "Stopped: timeout reached"
                    )

    except ClientError as e:
        return {
            "error": "Failed during scan",
            "details": str(e)
        }

    return _response(
        bucket_name,
        object_count,
        total_size,
        "Completed"
    )

def _response(bucket, count, size_bytes, status):
    return {
        "bucket": bucket,
        "objects_scanned": count,
        "total_size_mb": round(size_bytes / (1024 * 1024), 2),
        "status": status
    }
