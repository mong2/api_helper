import requests
import json
import base64

class APIToken:
	def __init__(self, api_hostname) :
		self.api_url = api_hostname
		return None

	def get_token(self, key_id, secret_key):
		url = "oauth/access_token?grant_type=client_credentials"
		base64str = base64.b64encode(key_id + ':' + secret_key)
		endpoint = self.api_url + '/' + url
		headers = {"Authorization": str("Basic " + base64str)}
		try:
			resp = requests.post(endpoint, headers=headers)
			if not resp.raise_for_status():
				data = resp.json()
				return data["access_token"]
		except requests.HTTPError as e:
			print e



