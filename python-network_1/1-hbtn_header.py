#!/usr/bin/python3
"""
    Script use the requests and sys packages to send a request  to a given URL 
    and display the variable value Request-Id in the response header
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
