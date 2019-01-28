#! /usr/bin/python3
import socket
#create file if it doesn't exist and truncate it's content if not empty
o = open ("output.txt","w")
f = open("Domains.txt", "r")
for line in f:
    y=line.strip()
    try:
        x = socket.gethostbyname(y)
    except socket.gaierror:
        o.write(y + " Not a valid Domain"+'\n')
        continue

    o.write(y + "  ==> " + x + '\n')
