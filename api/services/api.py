import os
from base64 import b64encode

class ApiService(object):
	
	def createApiKey(self, user):
		print('Create api key for: [{}][{}]'.format(user['mail'], user['id']))
		random_bytes = os.urandom(24)
		apiKey = str(b64encode(random_bytes).decode('utf-8'))
		print('Api Key for: [{}][{}]'.format(user['id'], apiKey))

		return apiKey