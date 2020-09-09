#!/usr/bin/env python
import requests

traget_page = "[URL in action]"

try_data= {"username":"admin", "password":"Passw0rd!", "login":"submit"}

resp = requests.post(traget_page, data=try_data)
print(reps.content)