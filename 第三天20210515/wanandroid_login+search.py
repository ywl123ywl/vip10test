import requests

#POST请求
urlstr1 = 'https://www.wanandroid.com/user/login'
urlstr2 = 'https://www.wanandroid.com/lg/todo/list/0'
payload = {'username':'ywl0730','password':'ywl850730'}


# # 第一种方法（携带cookie请求）
# # s = requests.session()
# # s.post(url=urlstr1,data=payload)
# # r1 = s.get(url=urlstr2)
# #
# # print(r1.text)

# # 第二种方法（重新拼接cookie发起请求）
# # r = requests.post(url=urlstr1,data=payload)
# # cookie = {
# #     'JSESSIONID': r.cookies['JSESSIONID']
# # }
# # r1 = requests.get(url=urlstr2,cookies=cookie)
# # print(r1.text)
# # print(r.cookies)


# # 第三种方法(cookie放在header中请求)
# r = requests.post(url=urlstr1,data=payload)
# header = {
#     'cookie':'JSESSIONID=' + r.cookies['JSESSIONID']
# }
# r1 = requests.get(url=urlstr2,headers=header)
# print(r1.text)


# 第四种方法（获取cookie并传入发起请求）
r = requests.post(url=urlstr1,data=payload)
cookie = r.cookies
r1 = requests.get(url=urlstr2,cookies=cookie)
print(r1.text)
