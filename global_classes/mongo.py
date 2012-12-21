# python modules
import pymongo

# THIS CLASS IS RESPONSIBLE FOR A LONG STANDING PYMONGO CONNECTION
# parameters = {
	
# 	'host': 
# 	'port':
#	'auth' :
# 	'username':
# 	'password':
#	'databases'
#	'collection'
# }

class Mongo(object):

	def __init__(self, config):

		self.config = config

		self.__connect()

	def __delete__(self):

		try:
			self.connection.disconnect() #end connect

		except all:

			print "No connection to disconnect from"

	def __connect(self):	

		try:

			# initialize the database
			self.connection = pymongo.Connection(self.config['host'], self.config['port']) #connection to elements
			self.database = self.connection[self.config['database']]#use the proper database
			if self.config["authenticate"]: self.database.authenticate(self.config['username'], self.config['password']) #authenticate against the database
			self.collection = self.database[self.config['collection']] #collection 

		except all:

			print "Unable to connect to mongo with current credentials. Please edit application.json or global_modules.py (if you know what you are doing)"
			exit() #end the program
		#end method


