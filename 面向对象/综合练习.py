
# 创建房子类
class House():

    def __init__(self,mj,address):
        self.address = address
        self.mj = mj
        self.s_mj = self.mj
        self.j_list = []

    def __str__(self):
        return f'房子总面积{self.mj},剩余面积{self.s_mj},房子内的家具有{self.j_list}'

    def add_jj(self,item):
        if self.s_mj > item.j_mj:
            self.j_list.append(item.name_j)
            self.s_mj = self.s_mj - item.j_mj
        else:
            print('家具太大，已经放不下了')
# 创建家具类
class Jiaju():
    def __init__(self,j_mj,name_j):
        self.name_j = name_j
        self.j_mj = j_mj


bed = Jiaju(4,'床')
house = House(100,'北京二环')
print(house)
house.add_jj(bed)
print(house)