#!/usr/bin/python

import sys
import json

# change path
sys.path.append("../")

from global_classes import *
from modules import *
# BEGIN TESTING

def main():

	with open("../application.json", 'r') as raw_data:

		config = json.loads(raw_data.read())

	test = mongo.Mongo(config['mongo'])
	print list(test.collection.find())

main()
