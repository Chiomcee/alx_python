#!/usr/bin/python3
"""
    Script that takes in aletter and sends 
    a post request with letter as parameter
"""
import requests
import sys

"""Get the letter from command line arguments or set as empty string"""
letter = sys.argv[1] if len(sys.argv) > 1 else ""

"""Set the URL"""
url = "http://0.0.0.0:5000/search_user"

"""Set the parameter 'q' as the letter"""
params = {'q': letter}

"""Send a POST request to the URL with the letter as a parameter"""
response = requests.post(url, data=params)

try:
    """Try to parse the response as JSON"""
    json_data = response.json()
    if json_data:
        """Display the id and name if JSON is properly formatted and not empty"""
        print("[{}] {}".format(json_data['id'], json_data['name']))
    else:
        """Display 'No result' if JSON is empty"""
        print("No result")
except ValueError:
    """Display 'Not a valid JSON' if JSON is invalid"""
    print("Not a valid JSON")