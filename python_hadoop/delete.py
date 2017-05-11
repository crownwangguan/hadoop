#!usr/bin/env python

from snakebite.client import Client 

client = Client('localhost', 9000)
for p in client.delete(['/foo', '/dumbinput'], recurse=True):
	print p