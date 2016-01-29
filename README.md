

# api_helper

Contain files:
* api.py : home of API requests function (get, post, put, delete)
* oauth.py : dealing with getting API token
* sample_auth_file : This is a sample auth file. Please modify it accordingly 
* test.py : Contains an example on how to use api_helper. Including GET, POST, PUT, DELETE

    *note: the default name for auth_file is config.conf. you can change the default auth_file name in test.py*

---

More on test.py - How to make API calls:

These functions can deal with both v1 and v2 endpoints. Simply add the version number in api endpoint

1. Get Request Example: 
    * api_endpoint: v1/servers, v2/issues
    
        ```python
        self.api.get(api_endpoint)
        ```
2. Post Request Example: 
    * api_endpoint: v1/policies, v2/policies
    * update body:
    
        ```
        body = {
            "policy": {
                "name": "test_policy"
            }
        }
         ```
        ```python
        self.api.post(api_endpoint, body)
        ```
3. Put Request Example: 
    * api_endpoint: v1/policies/{policy_id}, v2/policies/{policy_id}
    * update body:
    
        ```
        body = {
            "policy": {
                "name": "update_policy"
            }
        }
        ```
        ```python
        self.api.put(api_endpoint, body)
        ```
4. Delete Request Example: 
    * api_endpoint: v1/policies/{policy_id}, v2/policies/{policy_id}
    
        ```python
        self.api.delete(api_endpoint)
        ```

----

**Setting up get.py**

1. ```
    vim ~/.bash_profile
    
    alias get='python ~/{where you store api_helper}/get.py'
    #save and quit#
    source ~/.bash_profile
    ```
2. open get.py
    ```
    config.read(os.path.abspath('./api_helper/config.conf'))
    #make sure the above path is where you store your api_helper#
    ```
3. go to one directory above /api_helper and type in **get {endpoint}** in the terminal. This should return all the API output of that endpoint. 


