import boto3,sys
import botocore
from Variables import regions
 
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


def getBucketList(region = 'us-east-11') :         
	s3 = boto3.resource('s3',region_name= region)
	
	try:
	   for bucket in s3.buckets.all():
	      print(bucket.name)
	except botocore.exceptions.EndpointConnectionError:
           print "Not able to connect to region '%s'"%region
           raise
    

#getBucketList()

for region in regions:
  print region

