# 导入包
import requests,json


# # 发送GET请求
# urlstr = 'http://www.wanandroid.com/article/query'
# payload = {'k':'Android'}
# r = requests.get(url=urlstr,params=payload)

# print(r.text)
# print(r.content)
# print(r.status_code)
# print(r.headers)
# print(r.json())
# print(r.cookies)
# print(r.raw)
# print(r.url)
# print(r.encoding)
# print(r.raise_for_status())



#POST请求
urlstr = 'http://httpbin.org/post'
payload = {'qq群名':'selenium+jmeter+loadrunner','qq群号':'106014970'}
#通过json.dumps方法将python字符串转换为json类型
payload = json.dumps(payload)
r = requests.post(url=urlstr,json=payload)

print(r.text)
#返回为json类型，通过r.json()方法查看结果
print(r.json())