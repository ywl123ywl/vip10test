# try:
#     print(num)
# except Exception as msg:
#     print(msg)


try:
    f = open('test.txt','r')
except:
    f = open('test.txt','w')
# else:
#     print('很开心没有错误')
finally:
    print('到此结束')