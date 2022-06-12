#!/root/PYTHON-Scripts/bin/python3

import requests
import json
try:
    res = requests.get('https://api.github.com/users/gitbilla')
    print(res.url)
    assert res.status_code == 200
    js = json.loads(res.text)
    name = js.get('login')
    print(f'Name: {name}')
    num = js.get('public_repos')
    print(f'Public Repos : {num}')
    follow = js.get('followers')
    print(f'Follows: {follow}')
except AssertionError as e:
        print("url is incorrect")
