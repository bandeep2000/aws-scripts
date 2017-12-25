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

""" This functions get the bucket list and takes region as input, default is us-east-1"""

DEFAULT_REGION = 'us-east-1'
def getBucketList(region = DEFAULT_REGION) :         
        
        logging.info("Getting bucket list for region '%s'"%region)
        print " "

	s3 = boto3.resource('s3',region_name= region)
	
	try:
	   for bucket in s3.buckets.all():
	      print(bucket.name)
	except botocore.exceptions.EndpointConnectionError:
           error_msg = "Not able to connect to region '%s'"%region
           error_msg = error_msg + ", please make sure it is passed correctly"
           logging.error(error_msg)
           raise

        return 0
    
#getBucketList()

#for region in ['us-east-1', 'us-east-22']:
  #getBucketList(region)
  #print region

