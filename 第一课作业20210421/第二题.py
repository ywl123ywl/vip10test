'''
题干：小明爱跑步，爱吃东西。
      1）小明体重75.0公斤
      2）每次跑步会减肥0.5公斤
      3）每次吃东西体重会增加1公斤
      4）小美的体重是45.0公斤
分析：类：人
      属性：名字、体重
      方法：跑步，吃
'''

class Person():

    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __str__(self):
       return f'{self.name}体重是{self.weight}公斤'

    def Run(self):
        self.weight = self.weight - 0.5
        print(f'{self.name}运动后体重减少0.5公斤')

    def Eat(self):
        self.weight = self.weight + 1
        print(f'{self.name}吃饭后体重增加1公斤')

p1 = Person('xiaoming',75)
print(p1)
p1.Eat()
print(p1)
p1.Run()
print(p1)

p2 = Person('xiaoei',45)
print(p2)
p2.Eat()
print(p2)
p2.Run()
print(p2)