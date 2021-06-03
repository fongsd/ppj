#!/usr/bin/python3

import os
import re
import sys

try:
    f = open("text.txt", "r")
    content = f.read()
except:
    exit("ne postji fajl")

f.close()

rb = '^([0-9]:) ((([A-Z]\.[ ]*)+([A-Z][a-z ]+)(and|,|\.| )*))+. ([^.]+.) ([^.]+([0-9]+).)'

s = re.compile(rb, re.M)

for i in s.finditer(content):
    print(i.group(9))
