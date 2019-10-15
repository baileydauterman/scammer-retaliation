import json
import random
import requests
import string
import os
import datetime

x = "fakeuserdata.json"

y = json.loads(open(x).read())

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://rebosao.blogspot.com/'
k = 0
while k < 10000:
    i = random.randint(0,10998)
    j = random.randint(0,10998)
    d = datetime.datetime.now()
    
    username = y[i]["email"]
    password = y[j]["password"]
    
    requests.post(url, allow_redirects=False, data={
        'e': username,
        'p': password
    })
    k = k + 1
    print(f'{d} {k}: sending username {username} and password {password}')