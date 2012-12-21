# import system modules
import sys, os

# set path
sys.path.append("../")


# initialize project modules
import configuration, directory
from modules import file_management


# go through destination and remove the items that don't need to by synced
# any file / directory that is not in source but in the destination gets deleted
class Sync(object): #pass in a configuration file to be used

	def __init__(self, configuration):
		
		self.configuration = configuration

		# initialize class objects for each directory
		self.source = directory.Directory(self.configuration.source_directory)
		self.destination = directory.Directory(self.configuration.destination_directory)
		
		# need logic here in case the destination does not exist etc
		self.__clean_files()#clean the source from banned files -- but don't delete them
		self.__clean_directories() #clean the source of unnecessary directories -- but don't delete them
		self.__sync_list() #generate the sync list -- this is the list of files that are not in the destination but in the source
		self.__copy_files() #copy all files properly!

		if self.configuration.clean: self.__clean_destination() #cleans the destination

		if self.configuration.permissions: self.__set_permissions() #sets the proper permissions for files based on the configuration

	# removes all banned files from directory objects
	def __clean_files(self):

		# need to go through all banned files and directories with the directory object
		for _file in self.configuration.banned_files:

			self.source.delete_file(_file)

		for _file in self.configuration.banned_global_files:
			
			self.source.delete_file(_file, True)


	# removes all banned directories from the directory objects
	def __clean_directories(self):

		for _directory in self.configuration.banned_directories:

			self.source.delete_directory(_directory)

		for _directory in self.configuration.banned_global_directories:

			self.source.delete_directory(_directory, True)

			#end for
		#end for loop

	def __sync_list(self):

		# foreach relative path in source
		# 	if it doesn't exist -- add a new sync

		# 	if the files are different add a new sync

		self.sync_list = [] # a list 

		for _file in self.source.files:#loop through all of the source files

			_destination = self.destination.path + _file
			_source = self.source.path + _file

			# use the file management compare -- will return if the files don't exist!
			if not file_management.compare_files(_source, _destination):

				_sync = {"destination": _destination, "source": _source}
				self.sync_list.append(_sync)
		# generates a list of different files that need to be synced

	def __copy_files(self): #responsible for synchronizing all the files in the sync list

		if len(self.sync_list) == 0: print "No files to be synchronized."

		for sync in self.sync_list:

			file_management.copy_files(sync['source'], sync['destination'])

			if self.configuration.message:
					print sync['source'] + " ==> " + sync['destination']


	def __clean_destination(self):
		# find out which paths are not in the source but in the destination and flag them for delete!
			
		# foreach file in destination list
		# if not in source, delete!

		# foreach directory in destination_directory
		# if not in source, delete


		for relative, absolute in zip(self.destination.files, self.destination.full_files):

			if relative not in self.source.files and absolute == os.path.join(self.destination.path, relative):

				file_management.remove_file(absolute)
				
				if self.configuration.message:
					print "-f %s" % absolute


		for _directory in self.destination.directories:

			relative = _directory.replace(self.destination.path, "")

			# we need to make sure that this directory does not exist in the source
			if self.source.path + relative not in self.source.directories:

				file_management.remove_directory(_directory)

				if self.configuration.message:
					print "-d %s" % _directory


	def __set_permissions(self):

		print "Permissions functionality unavailable right now"
