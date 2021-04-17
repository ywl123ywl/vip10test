class washer():

    def __init__(self,width,height,brand):
        self.width = width
        self.height = height
        self.brand = brand

    def wash(self):
        print(f'haier洗衣机的宽度是{self.width}')
        print(f'haier洗衣机的高度是{self.height}')
        print(f'haier洗衣机的品牌度是{self.brand}')

    def __str__(self):
        return f'测试{haier.brand}'

    def __del__(self):
        print('我被删除了')

haier = washer(200,600,'西门子')
haier.wash()

haier1 = washer(100,900,'haier')
haier1.wash()

print(haier)

del haier