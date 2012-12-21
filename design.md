Synchronization Program
=

High Level
-

-	Synchronize directories (one way sync)
-	Read configuration files from json or mongodb -- ability to put in a filename for temp purposes
-	Syncs files from left to right, and will delete files that should not exist
-	Banned global files and directories -- keep driectories and files from being deleted (ie: ".git in any directory")
-	Absolute path files and directories -- keep a specific file such as Documents/git from syncing

Implementation
-

Modules
-

-	Json (External - used to parse json)
-	os, sys, shutil (external, used to help with system integration and commands)
-	file_management - my own module. Used to implement all system level commands into an abstracted layer to be used by my program classes

Classes
-

-	Configuration -- responsible for returning a config setup
	-	directories, banned files / directories / global settings
-	Directory -- this represents a master directory in the sync program
	-	various files to be used by the sync class
	-	lists (absolute path / relative path)
	-	add / remove directory etc
-	Sync -- this is the controller of the sync
	-	responsible for taking in a config object and using this to work on the two directories

Version 2.0
-

-	Want the ability to control output based on configuration file
-	Want to send a ".json" config file for general purposes
-	Send in a project name and it will run the general application
-	Main file -- that will run the sync for each -- this is the base class
