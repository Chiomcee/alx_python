#!/bin/usr/python3
"""
    Scripts that uses the requests package to 
    fetch the status from the specified URL
"""
import requests

url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)

print("Body response:")
print(f"    - type: {type(response.text)}")
print(f"    - content: {response.text}")
