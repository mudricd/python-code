#!/usr/bin/env python3

import subprocess

# Kibana upgrade
subprocess.call('systemctl stop kibana',shell=True)
print("Service has been stopped successfuly")

subprocess.call('wget https://artifacts.elastic.co/downloads/kibana/kibana-7.9.2-x86_64.rpm',shell=True)
print("The package was downloaded successfully")

subprocess.call('rpm -Uvh kibana-7.9.2-x86_64.rpm',shell=True)
print("Kibana was upgraded successfully")

# Start kibana service
subprocess.call('systemctl start kibana',shell=True)
print("Service was started successfuly")
subprocess.call('systemctl status kibana.service',shell=True)