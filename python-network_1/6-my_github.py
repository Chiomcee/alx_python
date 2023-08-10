#!/usr/bin/python3
"""
    script that takes your GitHub credentials (username and password) 
    and uses the GitHub APIto display your id
"""
import requests
import sys

"""Get the username and password from command line arguments"""
username = sys.argv[1]
password = sys.argv[2]

"""Set the URL to access user information"""
url = "https://api.github.com/user"

"""Set the headers with Basic Authentication using the username and password"""
headers = {'Authorization': 'token {}'.format(password)}

"""Send a GET request to the URL with Basic Authentication headers"""
response = requests.get(url, headers=headers)

"""Check if the request was successful"""
if response.status_code == 200:
    """Retrieve the user id from the response"""
    user_id = response.json().get('id')

    """Display the user id"""
    if user_id:
        print(user_id)
    else:
        print("User ID not found in the response.")
else:
    """Display None if the request failed"""
    print("None")