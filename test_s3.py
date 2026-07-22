from aws import s3

try:
    response = s3.list_buckets()

    print("✅ Connected Successfully")

    for bucket in response["Buckets"]:
        print(bucket["Name"])

except Exception as e:
    print("❌ Error")
    print(e)