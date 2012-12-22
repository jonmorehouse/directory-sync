#!/usr/bin/python
import sys
import os
import json

from modules import *
from classes import *
from global_classes import *

base_path = "/Users/MorehouseJ09/Documents/programs/python/directory_sync"

# this function is responsible for getting the configuration file and exiting if it does not exist
def config():
	# PATH INITIALIZATION -- FOR DATA!

	application_file = os.path.join(base_path, "application.json")

	# validate the application configuration before anything else!
	if not os.path.exists(application_file) or not load.valid_json(application_file):

		# not valid json
		print "Invalid Application Configuration"
		exit()

	else:#application found -- initialize the object of application
		
		_config = load.json_file(application_file)
		_config['base_path'] = base_path
		return _config

# main function -- responsible for loading in either file_controller or mongo_controller
def main(argv = sys.argv):

	# ensure that at least one artgument was passed
	if len(argv) <= 1:
		print "Please give either a file name or module name (mongodb)"
		return

	if argv[1] == "-p":#we're working with a package here -- need to get package documents
		mongo_controller.Mongo_controller(config()).run_package(argv[2])
		print "Package %s synced." % argv[2]

	elif argv[1].find(".json") != -1:
		file_controller.File_controller(argv[1])
		print "JSON module %s synced." % argv[1]

	else: #static file compiler
		mongo_controller.Mongo_controller(config()).run_module(argv[1])
		print "Module %s synced" % argv[1]

	exit()
	#end main method
main(sys.argv)









