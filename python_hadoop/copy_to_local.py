#!/usr/bin/env python

from snakebite.client import Client 

client = Client('localhost', 9000)
for f in client.copyToLocal(['input/haha.txt'], '/tmp'):
	print f