#!/usr/bin/env python

import platform
import subprocess

def execute():

    distribution = platform.dist()
    dist = list(distribution)

    if dist[1][0] == '7':
        subprocess.call('/usr/bin/rpm -i /root/files/repo/epel-release-latest-7.noarch.rpm',shell=True)
    elif dist[1][0] == '6':
        subprocess.call('/bin/rpm -i /root/files/repo/epel-release-latest-6.noarch.rpm',shell=True)
    elif dist[1][0] == '5':
        subprocess.call('/bin/rpm -i /root/files/repo/epel-release-latest-5.noarch.rpm',shell=True)

execute()
