import requests


sonc= requests.get('https://www.kariyer.net/is-ilanlari/#&kw=python')
print(sonc.text)
