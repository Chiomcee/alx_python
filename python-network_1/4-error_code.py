#!/usr/bin/python
"""
    Script that handles the error case correctly
"""
import requests
import sys

"""Get the URL from command line arguments"""
url = sys.argv[1]

"""Send a GET request to the URL"""
response = requests.get(url)

"""Check if the request was successful"""
if response.status_code >= 400:
    """Display the error code"""
    print("Error code: {}".format(response.status_code))
else:
    """Display the response body"""
    print(response.text)