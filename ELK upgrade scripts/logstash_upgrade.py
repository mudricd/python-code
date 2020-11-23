#!/usr/bin/env python3

import subprocess

# Logstash upgrade
subprocess.call('systemctl stop logstash',shell=True)
print("Service has been stopped successfuly")

subprocess.call('wget https://artifacts.elastic.co/downloads/logstash/logstash-7.9.2.rpm',shell=True)
print("The package was downloaded successfully")

subprocess.call('rpm -Uvh logstash-7.9.2.rpm',shell=True)
print("Logstash was upgraded successfully")

# Start Logstash service
subprocess.call('systemctl start logstash',shell=True)
print("Service was started successfuly")
subprocess.call('systemctl status logstash.service',shell=True)

# Update Logstash plugins
subprocess.call('sudo /usr/share/logstash/bin/logstash-plugin update',shell=True)
print("Plugins updated successfully")







