import requests,json

url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-773058962040428-shentong-KUAIDI1621064626268.html'

r = requests.get(url=url)

print(r.json())
print(r.json()['data'][0]['context'])