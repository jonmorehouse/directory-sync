# This program is useful for running the synchronization with files 
# Responsible for knowing the name of the config location and any other data
# Uses JSON to load in a config file

import base_controller

class File_controller(base_controller.Base_controller):

	def __init__(self, global_config, module):

		print "HELLO FROM FILE CONTROLLER"

