import json

# ensures valid json
def valid_json(filename):

	try: #make sure that the file opens properly
		with open(filename, 'r') as raw_data:

			try: #ensure that we are working with valid json
				json.loads(raw_data.read())
				return True

			# catch a value error if not valid json
			except (ValueError, OSError):

				print "Invalid JSON."
				return False

	except OSError:
		print "File not found."
		return False

def json_file(filename):

	if not valid_json(filename): return False

	with open(filename, 'r') as raw_data:

		return json.loads(raw_data.read())

	return False

