import boto3,sys
from prettytable import PrettyTable
 
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


#Print all ec2 instances
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
#for instance in instances:
#    print(instance.id, instance.instance_type)
 
# print ec2 instances state
t = PrettyTable(['ID', 'Type','State'])
for inst in ec2.instances.all():
   #print "%s %s %s"%(inst.id,inst.instance_type,inst.state['Name'])
   t.add_row([inst.id,inst.instance_type,inst.state['Name']])

print t
