
import requests,json

#POST请求
urlstr = 'https://www.wanandroid.com/user/login'
payload = {'username':'ywl0730','password':'ywl850730'}
header = {'User-Agent':'Mozilla/5.0'}
#通过json.dumps方法将python字符串转换为json类型
# payload = json.dumps(payload)
r = requests.post(url=urlstr,data=payload,headers=header)

print(r.text)
#返回为json类型，通过r.json()方法查看结果

errorCode = r.json()['errorCode']
sta_code = r.status_code

try:
    username = r.json()['data']['username']
    if sta_code == 200:
        if errorCode == 0 and username =='ywl0730':
            print('恭喜，登录成功！')
except Exception as msg:
    print('登录失败:',msg)