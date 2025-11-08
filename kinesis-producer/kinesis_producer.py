import boto3, json, uuid, time

k = boto3.client('kinesis')
stream_name= "retail-clickstream"

for i in range(5):
    event= {
        "event_id": str(uuid.uuid4()),
        "user_id": f"user_{i}",
        "product_id": f"P_{i}",
        "event_type": "view",
        "time": time.time()
    }

    k.put_record(StreamName= stream_name, Data= json.dumps(event), PartitionKey= "user")
    print(f"Sent: {event}")