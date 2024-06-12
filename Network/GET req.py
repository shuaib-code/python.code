# -*- coding: utf-8 -*-
import requests

url = 'https://ilman-naafian.vercel.app/readlist'

response = requests.get(url)

if response.status_code == 200:  # Check if the request was successful
    data = response.json()  # Parse the response data as JSON
    for d in data:
        print(f"[{d["_id"]}]")
else:
    print(f"Request failed with status code {response.status_code}")
