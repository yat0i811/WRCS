import requests

urllocal = "http://127.0.0.1:8000/raspost"
url = "https://test811.pythonanywhere.com/raspost"

data = {"title":"test-RaspberryPi", "text": "contents"}

#GETメソッド
#rg = requests.get(url)

#POSTメソッド
rp = requests.post(url, data=data)

print(rp)