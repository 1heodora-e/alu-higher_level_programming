#!/usr/bin/python3
'''
This script fetches the status information from a URL and prints the results
in a formatted way.

Usage:
    python fetch_status.py

Dependencies:
    - requests library (install using "pip install requests")

Example Output:
    Body response:
        - type: <class 'bytes'>
        - content: b'OK\n'
        - utf8 content: OK
'''
import urllib.request

if __name__ == "__main__":
    '''
    This script fetches the status information from different URLs and
    prints the results in a formatted way.
    '''
    urls = ['https://alu-intranet.hbtn.io/status', 'http://0.0.0.0:5050/status']

    for url in urls:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            data = response.read()
            info = f"Body response for {url}:\n\t- type: {type(data)}\n\t- \
content: {data}\n\t- utf8 content: {data.decode('utf-8')}"
            print(info)
