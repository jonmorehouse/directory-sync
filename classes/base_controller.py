# PYTHON LIBRARIES
import json, sys

# append to the system path
sys.path.append("../")

# initialize project libraries
import configuration, directory
from modules import file_management

# initialize class
class Base_controller(object):

	def __init__(self, global_config):

		self.global_config = global_config
		# load global configuration
		self.modules = [] #this is the 

	def __load_lists(self, data):#takes in objects and will extend them

		# keys = ["banned_directories", "banned_global_directories", "banned_files"]
		if type(data) is not dict: return

		# responsible for loading in the global lists given the data object
		if "banned_directories" in data:
			self.banned_directories.extend(data["banned_directories"])

		if "banned_files" in data:
			self.banned_files.extend(data["banned_files"])		

		if "banned_global_files" in data:
			self.banned_global_files.extend(data["banned_global_files"])

		if "banned_global_directories" in data:
			self.banned_global_directories.extend(data["banned_global_directories"])


	def load_project(self, filename):

		data = self.__load_json(filename)

		self.__load_lists(data)
		# load in project specifc elements
		self.source_directory = data['source_directory']
		self.destination_directory = data['destination_directory']
		



