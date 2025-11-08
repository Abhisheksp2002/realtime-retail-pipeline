import json, boto3, requests, os
from datetime import datetime

s3= boto3.client("s3")
bucket_name = os.environ["BUCKET_NAME"]
url = os.environ["URL"]

def lambda_handler(event, context):

    print(f"fetching data from {url}")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json"
    }
    
    data= requests.get(url, headers= headers).json()
    ts= datetime.utcnow().strftime("%Y%m%d%T%H%M%S")
    key= f"raw/products/products_{ts}.json"
    s3.put_object(Bucket=bucket_name, Key=key, Body=json.dumps(data))
    return {"status": "ok", "file": key}