'''
题干：士兵开枪
        需求：
        1）.士兵瑞恩有一把AK47
        2）.士兵可以开火(士兵开火扣动的是扳机)
        3）.枪 能够 发射子弹(把子弹发射出去)
        4）.枪 能够 装填子弹 --增加子弹的数量
分析：类：士兵、枪
      属性：士兵名字，枪的名字、子弹数
      方法：扣动扳机、开火、装弹
'''

class Shibing():

    def __init__(self,name):
        self.name = name

    def fire(self,item):
        if item.zidan_count > 0 :
            print(f'{self.name}可以进行射击操作')
            item.shot()
        else:
            print(f'{item.name}子弹数量不足，需要装弹')
            item.add_zidan()


class Gun():

    def __init__(self,name):
        self.name = name
        self.zidan_count = 0

    def __str__(self):
        return f'{self.name}初始子弹数为{self.zidan_count}'

    def add_zidan(self):
        self.zidan_count += 20
        print(f'{self.name}每次装弹{self.zidan_count}发')

    def shot(self):
        self.zidan_count -= 1
        print(f'每次发射1发子弹后剩余{self.zidan_count}发')

g = Gun('AK47')
print(g)
g.add_zidan()
g.shot()
p = Shibing('瑞恩')
p.fire(g)