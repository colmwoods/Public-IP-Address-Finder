import requests as req

url: str = 'https://checkip.amazonaws.com'
requests = req.get(url)
ip: str = requests.text

print("IP:", ip, end="")