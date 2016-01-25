	import json
import ConfigParser
from api import Api
from oauth import APIToken



class Test:
	def __init__(self):
		config = ConfigParser.ConfigParser()
		# Replace config.conf with your own auth_file name
		config.read('config.conf')

		key_id = config.get('client','key_id')
		secret_key = config.get('client', 'secret_key')

		api_hostname = config.get('client', 'api_hostname')

		oauth = APIToken(api_hostname)
		token = oauth.get_token(key_id, secret_key)

		self.api = Api(token)
		return None

	def test_get(self):
		resp = self.api.get("v1/servers")
		if not resp.raise_for_status():
			data = resp.json()
			print data
		return None

	def test_post(self):
		body = {
			"policy": {
				"name": "Testing-hlee",
				"platform": "linux"
			}
		}
		resp = self.api.post("v1/policies", body)
		if not resp.raise_for_status():
			data = resp.json()
			policy_id = data["policy"]["id"]
			return policy_id

	def test_put(self):
		body = {
			"policy": {
				"name": "Update-hlee"
			}
		}
		# got the policy id from test_post. you can definitely add an argument to pass in the policy
		# instead of hard coded in the below url.
		resp = self.api.put("v1/policies/15be2cbec3a511e5a01759521d1a9f69", body)
		resp.raise_for_status()
		return None

	def test_delete(self):
		resp = self.api.delete("v1/policies/15be2cbec3a511e5a01759521d1a9f69")
		resp.raise_for_status()
		return None

# Ask the script to run
if __name__ == "__main__":
	# setup the initial requirements, including API Token
	initial = Test()

	#example on how to call the test_get function
	initial.test_get()

	# More examples:
	# initial.test_post()
	# initial.test_put()
	# initial.test_delete()