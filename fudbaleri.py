#!/usr/bin/python3

import sys
import re
import os
#print(sys.argv[1])
if len(sys.argv) <=1 or str(sys.argv[1]).endswith(".csv") == False:
    exit("arg or file failed")
    
try: 
    f = open(sys.argv[1], "r")
    content = f.read()
except:
    exit("file doesnt exist")
 
 
r1 = r'^([A-Z][a-zA-Z ]*\s*){1,3},'

s1 = re.compile(r1, re.M)
imena = {}
for i in s1.finditer(content):
    print(i.group(1))
