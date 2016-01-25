# api_helper

Contain files:
* api.py : home of API requests function (get, post, put, delete)
* oauth.py : dealing with getting API token
* sample_auth_file : This is a sample auth file. Please modify it accordingly 
* test.py : Contains an example on how to use api_helper. Including GET, POST, PUT, DELETE

----
More on test.py - How to make API calls:

1. Get Request: 
..* this function can deal with both v1 and v2 endpoints. Simply the version number in api_endpoint.
..* ex: v1/servers, v2/issues
```python
self.api.get(api_endpoint)
```

Note:
