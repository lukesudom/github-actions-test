#!/bin/python3

import requests
import os
from json import dumps

if  __name__ == "__main__":
    TOKEN = os.getenv('API_KEY')
    print("key ends in: ")
    print(TOKEN[:10])
    
    url = '<https://api.thecatapi.com/v1/images/0XYvRd7oD'
    headers = {
        'x-api-key' : TOKEN
    }
    cat_info = requests.get(url, headers)
    print(dumps(cat_info.json(), indent = 1))
