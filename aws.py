# import boto3
# import os
# from dotenv import load_dotenv

# load_dotenv()

# s3 = boto3.client(
#     "s3",
#     aws_access_key_id=os.getenv("AKIATK2AJUCMMUSEPHFD"),
#     aws_secret_access_key=os.getenv("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"),
#     region_name=os.getenv("ap-southeast-1")
# )

# def upload_file(file, filename):
#     bucket = os.getenv("secure-cloud-docs-kunal-2026")

#     s3.upload_fileobj(
#         file,
#         bucket,
#         filename
#     )

#     return f"https://{bucket}.s3.amazonaws.com/{filename}"
# import boto3
# import os
# from dotenv import load_dotenv

# # Load variables from .env
# load_dotenv()

# # Create S3 Client
# s3 = boto3.client(
#     's3',
#     aws_access_key_id=os.getenv('AKIATK2AJUCMMUSEPHFD'),
#     aws_secret_access_key=os.getenv('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'),
#     region_name=os.getenv('ap-southeast-1')
# )

# print("S3 Connected Successfully!")
# import boto3
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Create S3 client
# s3 = boto3.client(
#     "s3",
#     aws_access_key_id=os.getenv("AKIATK2AJUCMMUSEPHFD"),
#     aws_secret_access_key=os.getenv("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"),
#     region_name=os.getenv("ap-southeast-1")
# )

# # Upload file to S3
# def upload_file(file, filename):
#     bucket = os.getenv("S3_BUCKET")

#     s3.upload_fileobj(
#         file,
#         bucket,
#         filename
#     )

#     file_url = f"https://{bucket}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{filename}"

#     return file_url
import boto3
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET")

# Create S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def upload_file(file, filename):
    s3.upload_fileobj(file, S3_BUCKET, filename)

    return f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{filename}"
def upload_file(file, filename):
    try:
        print("===== DEBUG =====")
        print("Bucket:", S3_BUCKET)
        print("Region:", AWS_REGION)
        print("Filename:", filename)
        print("Access Key Loaded:", AWS_ACCESS_KEY is not None)

        s3.upload_fileobj(
            Fileobj=file,
            Bucket=S3_BUCKET,
            Key=filename
        )

        print("✅ File uploaded successfully!")

        file_url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{filename}"
        print("URL:", file_url)

        return file_url

    except Exception as e:
        print("❌ Upload Error:", repr(e))
        return None