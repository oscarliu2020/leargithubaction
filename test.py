import requests
req=requests.get('https://ifconfig.me/all',headers={'User-Agent':'Mozilla/5.0 (X11; U; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/114.0.5776.207 Chrome/114.0.5776.207 Safari/537.36'})
print(req.text)
