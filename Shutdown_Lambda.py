
#!/usr/bin/env python
#Stop instances

import boto3
region = 'ap-southeast-2'
ec2 = boto3.client('ec2', region_name=region)
tag_filter = [{
    'Name':'tag:ime',
    'Values': ['dole']}]

response = ec2.describe_instances(Filters=tag_filter)

listid=[]
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        iid=instance["InstanceId"]
        listid.append(iid)
        
def lambda_handler(event, context):
    for ec2instance in listid:
        ec2.stop_instances(InstanceIds=listid)
        print('Stopped instance: ' + str(ec2instance))

#!/usr/bin/env python
#Start instances

import boto3
region = 'ap-southeast-2'
ec2 = boto3.client('ec2', region_name=region)
tag_filter = [{
    'Name':'tag:ime',
    'Values': ['dole']}]

response = ec2.describe_instances(Filters=tag_filter)

listid=[]
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        iid=instance["InstanceId"]
        listid.append(iid)
        
def lambda_handler(event, context):
    for ec2instance in listid:
        ec2.start_instances(InstanceIds=listid)
        print('Started instance: ' + str(ec2instance))




#!/usr/bin/env python
#Stop instances and autoscaling suspend
import boto3
region = 'ap-southeast-2'
ec2 = boto3.client('ec2', region_name=region)
client = boto3.client('autoscaling')

state_filter = [
        {
    'Name':'instance-state-name',
    'Values': ['terminated']
    }
        ]
status = ec2.describe_instances(Filters=state_filter)

liststatus=[]
for reservation in status['Reservations']:
    for instance in reservation['Instances']:
        iid=instance["InstanceId"]
        liststatus.append(iid)
print(liststatus)

tag_filter = [{
    'Name':'tag:es_cluster',
    'Values': ['LPS-ELK-NP-DM']}]

response = ec2.describe_instances(Filters=tag_filter)

listid=[]
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        iid=instance["InstanceId"]
        listid.append(iid)
print(listid)

ec2list = list(set(liststatus)^set(listid))

def lambda_handler(event, context):

    client.suspend_processes(
    AutoScalingGroupName='LPS-ELK-NP-DM-KibanaAutoscalingGroup',
    ScalingProcesses=[
        'Launch','Terminate'
    ]
)

    client.suspend_processes(
     AutoScalingGroupName='LPS-ELK-NP-DM-LogstashAutoscalingGroup',
     ScalingProcesses=[
         'Launch','Terminate'
    ]
)

    client.suspend_processes(
     AutoScalingGroupName='LPS-ELK-NP-DM-ElasticAutoscalingGroup',
     ScalingProcesses=[
         'Launch','Terminate'
    ]
)
    for ec2instance in ec2list:
        ec2.stop_instances(InstanceIds=ec2list)
        print('Stopped instance: ' + str(ec2instance))


#!/usr/bin/env python
#Start instances and autoscaling resume
import boto3
import time
region = 'ap-southeast-2'
ec2 = boto3.client('ec2', region_name=region)
client = boto3.client('autoscaling')

state_filter = [
        {
    'Name':'instance-state-name',
    'Values': ['terminated']
    }
        ]
status = ec2.describe_instances(Filters=state_filter)

liststatus=[]
for reservation in status['Reservations']:
    for instance in reservation['Instances']:
        iid=instance["InstanceId"]
        liststatus.append(iid)
print(liststatus)

tag_filter = [{
    'Name':'tag:es_cluster',
    'Values': ['LPS-ELK-NP-DM']}]

response = ec2.describe_instances(Filters=tag_filter)

listid=[]
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        iid=instance["InstanceId"]
        listid.append(iid)
print(listid)

ec2list = list(set(liststatus)^set(listid))

for reservation in status['Reservations']:
    for instance in reservation['Instances']:
        iid=instance["InstanceId"]
        try:
            ec2list.remove(iid)
            break
        except ValueError:
            pass
        
mytext="This is a final list: "
print( mytext + ', '.join(ec2list))

def lambda_handler(event, context):

    for ec2instance in ec2list:
        ec2.start_instances(InstanceIds=ec2list)
        print('Started instance: ' + str(ec2instance))
    time.sleep(150)

    client.resume_processes(
    AutoScalingGroupName='LPS-ELK-NP-DM-KibanaAutoscalingGroup',
    ScalingProcesses=[
        'Launch','Terminate'
    ]
)

    client.resume_processes(
     AutoScalingGroupName='LPS-ELK-NP-DM-LogstashAutoscalingGroup',
     ScalingProcesses=[
         'Launch','Terminate'
    ]
)

    client.resume_processes(
     AutoScalingGroupName='LPS-ELK-NP-DM-ElasticAutoscalingGroup',
     ScalingProcesses=[
         'Launch','Terminate'
    ]
)
