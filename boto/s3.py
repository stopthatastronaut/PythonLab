import boto3

session = boto3.Session(profile_name='stopthatastronaut')

s3 = boto3.client('s3')

resp = s3.list_buckets()

bucketnames = [bucket['Name'] for bucket in resp['Buckets']]

print(bucketnames)