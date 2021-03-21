import requests

import json



sonc= requests.get('https://api.github.com/users')
#print(sonc.text)

sonc1=json.loads(sonc.text)

print(sonc1[1]['login'])

for i in sonc1:
    print(i['login'],'   ',i['node_id'],'    ',i['avatar_url'])
