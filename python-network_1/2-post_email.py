#!/usr/bin/python3
"""
    Sends a POSt request to a given URL with email
    address as a parameter
"""
import requests
import sys

"""Get the URL and email address from command line arguments"""
url = sys.argv[1]
email = sys.argv[2]

"""Create a dictionary to hold the email as a parameter"""
data = {'email': email}

"""Send a POST request to the URL with the email as a parameter"""
response = requests.post(url, data=data)

"""Obtain the response body"""
response_body = response.text

"""Display the response body"""
print(response_body)