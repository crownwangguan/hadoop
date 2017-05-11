#!/usr/bin/python

import sys

# line = '10.190.174.142 - - [03/Dec/2011:13:28:09 -0800] "GET /assets/img/home-logo.png HTTP/1.1" 200 3892'
for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
	    ip, _, _, _, _, _, _, _, _, _ = data
	    print "{0}\t{1}".format(ip, 1)