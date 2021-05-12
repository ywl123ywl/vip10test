'''
题干：打印小猫爱吃鱼，小猫要喝水
分析：1、类：小猫
      2、属性：无
      3、方法：吃鱼、喝水
'''

class Cat():

    # 方法
    def Eat(self,food):
        print(f'小猫爱吃{food}')

    def Drink(self,drink):
        print(f'小猫要喝{drink}')

cat = Cat()
cat.Eat('鱼')
cat.Drink('水')