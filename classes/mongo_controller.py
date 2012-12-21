import base_controller

from global_classes import mongo
from classes import configuration, sync

class Mongo_controller(base_controller.Base_controller):

	def __init__(self, global_config):


		super(Mongo_controller, self).__init__(global_config) #call parent -- immediately derived class
		self.mongo = mongo.Mongo(self.global_config['mongo']) #initialize the mongo connection
		self.sync_config = self.mongo.collection.find_one({"module": "global_config"})

		if self.sync_config == None:

			print "Mongo Application not configured properly. Please upload a global_config module or edit mongo_controller.py if you know what you are doing."
			exit()		

	def run_package(self, package):

		documents = list(self.mongo.collection.find({"package": package}))

		if len(documents) <= 0: 
			print "No modules available for package %s" % package
			exit()

		self.__run(documents)


	def run_module(self, module):

		# get all lists
		documents = list(self.mongo.collection.find({"module": module}))

		if len(documents) <= 0: 
			print "Module not found %s" % module
			exit()
			
		self.__run(documents)

	# RUN FILES
	def __run(self, documents):

		for document in documents: 

			self.__sync(document) #create the config item and then run the synchronization file


	def __sync(self, module):#send in a module result from the mongodb

		# generate proper configuration
		config = configuration.Configuration(self.sync_config).set(module) #this gives the sync global config dict and then sends a module to it as well

		# ensure that copy worked properly
		if not config: return

		sync.Sync(config) #run the sync
		del config #delete the object



		





	



		