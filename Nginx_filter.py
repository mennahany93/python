#! /usr/bin/python3
import os , sys

##take path of nginx access log as argument
access_log= sys.argv[1]
ip_list=[]
if os.path.isfile(access_log):
    f= open(access_log,"r")
    s= open(access_log,"r").read()
    for i in f:
        ip=i.split(' ')[0]
        if ip not in ip_list:
            ip_list.append(ip)
            s= open(access_log,"r").read()
            print(str(ip) + " occured " + str(s.count(ip)) + " times.")
else:
    print("No such file or directory")
