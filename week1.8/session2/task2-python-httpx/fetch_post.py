"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"

response = httpx.get(url)   # httpx object, get() method, returns a response object
print(response)

if response.status_code == 200:
    print(response.json())      # response object, json() method
else:
    print("There is an error")