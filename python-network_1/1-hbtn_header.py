#!/usr/bin/python3
"""
    Script use the requests and sys packages to send a request  to a given URL 
    and display the variable value Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    """Get URL from the command line arguments"""
    url = sys.argv[1]
    """Send a GET request to the URL"""
    response = requests.get(url)

    """Check if the request was successful"""
    if response.status_code == 200:
        """Get the value of the 'X-Request-Id' header"""
        request_id = response.headers.get('X-Request-Id')

        """Display the value of 'X-Request-Id'"""
        if request_id:
            print(request_id)
        else:
            print("No 'X-Request-Id' header found in the response.")
    else:
        print(f"Request failed with status code {response.status_code}.")
