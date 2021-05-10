'''
题干：摆放家具
        需求：
        1）.房子有户型，总面积和家具名称列表
           新房子没有任何的家具
        2）.家具有名字和占地面积，其中
           床：占4平米
           衣柜：占2平面
           餐桌：占1.5平米
        3）.将以上三件家具添加到房子中
        4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
分析：类：房子、家具
      属性：房子户型、总面积、家具列表；家具名字、面积
      方法：给房子添加家具
'''

class House():
    def __init__(self,area,address):
        self.area = area
        self.address = address
        self.sy_area = area
        self.f_list = []

    def __str__(self):
        return f'房子地址是{self.address},总面积是{self.area}平米,家中剩余面积是{self.sy_area},家中有家具{self.f_list}'

    def add_f(self,item):
        if item.area <= self.sy_area:
            print(f'家里添加家具--{item.name}--成功')
            self.f_list.append(item.name)
            self.sy_area -= item.area
        else:
            print(f'家中剩余面积是{self.sy_area}平，不能再添加家具--{item.name}')



class Furniture():
    def __init__(self,name,area):
        self.name = name
        self.area = area


h = House(90,'北京二环')
print(h)

f = Furniture('床',4)
h.add_f(f)
f = Furniture('衣柜',2)
h.add_f(f)
f = Furniture('餐桌',1.5)
h.add_f(f)

print(h)