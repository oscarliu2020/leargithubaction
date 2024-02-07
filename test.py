import requests
req=requests.get('https://icanhazip.com')
print(req.text)