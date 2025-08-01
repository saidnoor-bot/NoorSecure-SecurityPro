import boto3
from botocore.exceptions import ClientError

bucket_name = 'noorshare-user-uploads'
object_name = 'uploads/my-photo.jpg'  # Customize path
expiration = 3600  # 1 hour

def create_presigned_url(bucket, object_name, expiration=3600):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url(
            'put_object',
            Params={'Bucket': bucket, 'Key': object_name},
            ExpiresIn=expiration
        )
    except ClientError as e:
        print(e)
        return None
    return response

url = create_presigned_url(bucket_name, object_name, expiration)
if url:
    print("Upload your file using this URL:")
    print(url)

