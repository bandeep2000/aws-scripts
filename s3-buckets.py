import boto3,sys
 
"""
Please make sure you have config file present to initialize your credentials
for aws and region
 ~/.aws/config
Example:
sudo cat ~/.aws/config 
[profile eb-cli]
aws_access_key_id = AKIAI7BMHSAF
aws_secret_access_key = 97frWubKtgnW2Gbi/acCI

[default]
region = us-east-1

"""

# print all buckets
s3 = boto3.resource('s3')
 
for bucket in s3.buckets.all():
    print(bucket.name)
