import os
import boto3

# Helper function to handle S3 connections
def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("S3_SECRET_KEY"),
        endpoint_url=os.getenv("S3_ENDPOINT"),
    )


def list_geojson_files(s3_bucket: str, s3_prefix: str):
    s3_client = get_s3_client()
    response = s3_client.list_objects_v2(Bucket=s3_bucket, Prefix=s3_prefix)
    geojson_files = [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].endswith('.json')]
    return geojson_files