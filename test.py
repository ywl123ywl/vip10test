'''
python的数据类型：
    整数、浮点数、字符串、元组、列表、eval()
'''

x = 'True'
eval(x)
print(type(eval(x)))

s = 'abcdefgde bc'
print(s[:2:-1])
print(s.find('bc'))
print(s.rfind('gd'))
print(s.count('bc'))
print(s.replace('bc','##'))
s1 = '1,2,3,4,5,6'
print(s1.split(',',2))
print(type(s1.split(',',2)))
print(''.join(s1.split(',',2)))

str1 = '   hello   world   '
print(str1.capitalize())
print(str1.title())
print(str1.upper())
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())
print(str1.center(50,'@'))
print(str1.ljust(50,'@'))
print(str1.rjust(50,'@'))

print(s.startswith("ab",0,10))
print(s.endswith("de",0,5))
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.isspace())