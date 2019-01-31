#! /usr/bin/python3
import os , sys

##take path of nginx access log as argument
access_log= sys.argv[1]
result={}
if os.path.isfile(access_log):
    f= open(access_log,"r")
    for i in f:
        ip=i.split(' ')[0]
        if ip in result:
            result[ip] +=1
        else:
            result[ip] = 1

    for key , value in result.items():
        print (str(key) + " ==> " + str(value))
else:
    print("No such file or directory")
    
