#!/usr/bin/env python

from snakebite.client import Client 

client = Client('localhost', 9000)
for p in client.mkdir(['/foo/bar', '/dumbinput'], create_parent=True):
	print p