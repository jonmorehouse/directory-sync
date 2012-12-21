from modules import file_management
import re

# 1.) Take in a path -- this is loaded from a sync controller
# 2.) Get all list items
# 3.) Get file -- this will return a path for a file name
# 4.) Delete file -- this will remove a list of the file
class Directory(object):

	def __init__(self, path):

		# initialize and validate the path
		self.path = path if path[-1:] == "/" else path + "/"

		# file initiation function
		self.file_init()
		self.directory_init()

	def file_init(self):

		self.full_files = file_management.list_dir(self.path)
		self.files = []

		if not self.full_files:

			self.full_files = []
			return 
		# 
		
		if self.full_files and len(self.full_files) > 0:
			
			for filename in self.full_files:

				filename = filename.replace(self.path, "")
				self.files.append(filename)
		#END METHOD

	def directory_init(self):

		self.directories = file_management.get_directories(self.path)

	def list_files(self, _list = "both"): #responsible for listing all elements

		for full, _file in zip(self.full_files, self.files):

			if _list == "both" or _list == "full": print full

			if _list == "both" or _list == "file": print _file


	def get_file(self, file_name):#will look through all elements
			
		for index, _file in enumerate(self.files):

			if file_name == _file:
				return index

		return False

	def delete_file(self, filename, _global = False):

		# check for period replacements
		filename = filename.replace(".", "\.")

		# regex statement
		regex = re.compile('.*%s.*' %filename)
		
		self.full_files = [_file for _file in self.full_files if not re.match(regex, _file)] #include the file if it is not a match

		self.files = [_file for _file in self.files if not re.match(regex, _file)]

	def delete_directory(self, directory, _global = False):

		# this expects a directory and will delete all elements that have this!
		directory = directory if directory[0] != "/" else directory[1:]

		directory = directory if directory[-1:] == "/" else directory + "/"

		# ensure that we have this directory to delete later
		# self.directories.remove(directory)

		# regex search
		if not _global:
			regex_relative = re.compile('^%s/*' %directory)
			regex_absolute = re.compile('.*%s/.*' %directory)

		else: #global search 
			regex_relative = re.compile('.*%s.*' %directory)
			regex_absolute = re.compile('.*%s.*' %directory)

		# now need to delete all the files with this directory!
		self.full_files = [_file for _file in self.full_files if not re.match(regex_absolute, _file)]
		self.files = [_file for _file in self.files if not re.match(regex_relative, _file)]

		# now need to delete the folder from the directory list
		self.directories = [_directory for _directory in self.directories if not re.match(regex_absolute, _directory + "/")]


	def clean(self):

		for _file in self.original_full_files:

			if _file not in self.full_files:

				file_management.remove_file(_file)

		for _directory in self.deleted_directories:

			file_management.remove_directory(_directory)