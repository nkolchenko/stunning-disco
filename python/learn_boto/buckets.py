import boto3
import uuid

bucket_prefix = "test-"
def create_bucket_name(bucket_prefix):
    bkt = ''.join([bucket_prefix, str(uuid.uuid4())])
    # 3 to 63 chars, Aa-Zz, 0-9, periods and dashes
    if len(bkt) < 3 or len(bkt) > 63:
        print("inavlid bucketname length")
        bkt = ''
    else:
        print(len(bkt))
#    return ''.join([bucket_prefix, str(uuid.uuid4())])
    return bkt

print(create_bucket_name(bucket_prefix))

