import json

class Configuration(object):

	clean = False #whether or not we should remove the files that are not synced
	permissions = False #not built in yet
	message = False #whether or not messages should be printed

	# default is the global application data
	def __init__(self, default = False):

		# initialize the objects
		self.banned_directories = [] #banned absolute directory
		self.banned_files = [] #banned absolute path relative to the directory
		self.banned_global_files = [] #anywhere this file is loaded will not be copied
		self.banned_global_directories = [] #anything with this in the name will be deleted!

		# load the global file and application specific file
		if default: self.set(default)

		# return self

	def __delete__(self):

		pass

	def set(self, input_dict):
		
		if input_dict['module'] != "global_config":
			self._set_module(input_dict)

		# loop through all keys
		for key in input_dict:

			function = "_set_%s" %key

			# call proper setter methods!
			if function != "_set_module" and hasattr(self, function):

				getattr(self, function)(input_dict[key])

			# loop through and grab other values
			if key in ["clean", "permissions", "message"]:

				self._set_boolean(key, input_dict[key])

		return self


	def _set_module(self, module):

		try:

			self.source_directory = module['source_directory']
			self.destination_directory = module['destination_directory']
			self.module = module['module']

		except KeyError:

			print "Invalid Configuration file. Directory, Source and Module are required."
			exit()


	def _set_banned_directories(self, directories):

		if type(directories) is list:
			self.banned_directories.extend(directories)

	def _set_banned_global_directories(self, directories):


		if type(directories) is list:
			self.banned_global_directories.extend(directories)


	def _set_banned_files(self, files):


		if type(files) is list:
			self.banned_files.extend(files)

	def _set_banned_global_files(self, files):

		if type(files) is list:
			self.banned_global_files.extend(files)

	def _set_boolean(self, key, value):

		# make sure the element has the value and then if it is a boolean value, set the value properly
		if hasattr(self, key) and type(value) is bool:

			setattr(self, key, value)



