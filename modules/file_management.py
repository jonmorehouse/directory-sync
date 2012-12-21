# This module is responsible for file management functions
# 1.) Recursive directory list -- returns all files in the directory given it (assume absolute paths)
# 2.) File Compare - Will return true or false if the files are the same
# 3.) Delete file -- will delete a file
# 4.) Copy file -- 
# add logs later!
import os, shutil, re, filecmp



def list_dir(path):

	# validate the path name
	path = path if path[-1:] == "/" else path + "/"

	# make sure the directory actually exists 
	if not os.path.isdir(path): return False

	# initialize the elements
	files = []

	# grab each item 
	for item in os.listdir(path):#get all objects

		# don't include cwd or pwd (current / previous working directories)
		if item == "." or item == "..":
			continue #skip this iteration

		# this is a file
		if not os.path.isdir(path + item): files.append(path + item) #append the file on the back of the list

		# this is a directory
		else: files.extend(list_dir(path + item)) #extend the list with this directories' items
	
	return files

# list all directories in the path!
def get_directories(path):

	path = path if path[-1:] == "/" else path + "/"

	directories = []
	# make sure the directory actually exists 

	try:
		for item in os.listdir(path):

			if os.path.isdir(path + item):
				directories.append(path + item)
				directories.extend(get_directories(path + item))

	except OSError:
		return []

	return directories

	#returns a recursive list of all files that are in the path

def copy_files(source, destination):

	# 
	if not os.path.isfile(source): return

	try:
		# ensure the destination directory exists!
		create_subdirectories(destination)
		shutil.copyfile(source, destination)

	except OSError:
		print "%s => %s copy failed." %(source, destination)

def compare_files(left, right):

	try:
		status = filecmp.cmp(left, right)

	except OSError:
		return False

	return status

def remove_file(path):

	try:
		os.remove(path)
	except OSError:
		print "File could not be found"

def remove_directory(path):
	try:
		shutil.rmtree(path)

	except OSError:
		print "%s not found." %path

def create_subdirectories(path):

	# first seperate the file name from the path
	path = path if path[0] else "/" + path

	# split the directories
	directories = path.split("/")	

	# initialize the new path
	path = ""

	# now loop through and add the proper pieces in
	for piece in directories[1:-1]: 

		path += "/%s" %piece
		if not os.path.isdir(path):#check if the path exists
			os.mkdir(path, 0755)#create the path


