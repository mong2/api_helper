import os
import sys
import json
import ConfigParser
from api import Api
from oauth import APIToken

class Get:
	def __init__(self):
		config = ConfigParser.ConfigParser()
		# Replace config.conf with your own auth_file name
		config.read(os.path.abspath('./api_helper/config.conf'))
		key_id = config.get('api_key_pair','key_id')
		secret_key = config.get('api_key_pair', 'secret_key')

		api_hostname = config.get('api_key_pair', 'api_hostname')

		oauth = APIToken(api_hostname)
		token = oauth.get_token(key_id, secret_key)

		self.api = Api(token)


	def get_endpoint(self):
		endpoint = sys.argv[1]
		resp=self.api.get(endpoint)
		data = resp.json()
		print json.dumps(data, indent=2)

if __name__ == "__main__":
	initial = Get()
	initial.get_endpoint()