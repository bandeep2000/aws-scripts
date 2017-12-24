import boto3,sys
import botocore
import logging 
from Variables import regions
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
#logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

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
        
        logging.info("Getting bucket list for region '%s'"%region)
        print " "
        #return 0

	s3 = boto3.resource('s3',region_name= region)
	
	try:
	   for bucket in s3.buckets.all():
	      print(bucket.name)
	except botocore.exceptions.EndpointConnectionError:
           error_msg = "Not able to connect to region '%s'"%region
           error_msg = error_msg + ", please make sure it is passed correctly"
           print error_msg
           raise
    

#getBucketList()

for region in regions:
  getBucketList(region)
  #print region

