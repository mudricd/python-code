#!/usr/bin/env python3

import subprocess

# Elasticsearch upgrade
subprocess.call('systemctl stop elasticsearch',shell=True)
print("Service has been stopped successfuly")

subprocess.call('wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.9.2-x86_64.rpm',shell=True)
print("The package was downloaded successfully")

subprocess.call('rpm -Uvh elasticsearch-7.9.2-x86_64.rpm',shell=True)
print("Elasticsearch was upgraded successfully")

## jvm.options changes
# Open and read a file
with open('/etc/elasticsearch/jvm.options', 'r') as file :
  filedata = file.read()

# Replace the target strings
for r in (("XX:+UseConcMarkSweepGC", "XX:+UseG1GC"), ("XX:CMSInitiatingOccupancyFraction=75", "XX:G1ReservePercent=25"), ("XX:+UseCMSInitiatingOccupancyOnly", "XX:InitiatingHeapOccupancyPercent=30")):
    filedata = filedata.replace(*r)

# Write the file out again
with open('/etc/elasticsearch/jvm.options', 'w') as file:
  file.write(filedata)

# Upgrade plugins
subprocess.call('/usr/share/elasticsearch/bin/elasticsearch-plugin remove repository-s3',shell=True)
subprocess.run(["/usr/share/elasticsearch/bin/elasticsearch-plugin", "install", "repository-s3"], capture_output=True, text=True, input="y")

subprocess.call('/usr/share/elasticsearch/bin/elasticsearch-plugin remove discovery-ec2',shell=True)
subprocess.run(["/usr/share/elasticsearch/bin/elasticsearch-plugin", "install", "discovery-ec2"], capture_output=True, text=True, input="y")

# Start elasticsearch service
subprocess.call('systemctl start elasticsearch',shell=True)
print("Service was started successfuly")
subprocess.call('systemctl daemon-reload',shell=True)
subprocess.call('systemctl status elasticsearch.service',shell=True)

