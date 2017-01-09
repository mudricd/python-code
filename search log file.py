
#!/usr/bin/python

with open('/var/log/carestream_search/haproxy.log-20160905','r') as jabber:		#open log file in read only mode
    for line in jabber:									#open loop 
        if 'Carestream' in line:							#search for string Carestream
            with open('/var/log/carestream_search/halogs.txt','a') as file:		#open file where you are going to save the output in append mode
                file.write(line)							#write in a file and close it
