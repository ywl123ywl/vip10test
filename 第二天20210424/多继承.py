class shifu(object):

    def __init__(self):
        self.kongfu = '五香煎饼果子制作秘籍'

    def make(self):
        print(f'使用{self.kongfu}制作出正宗煎饼果子')

class shcool(object):

    def __init__(self):
        self.kongfu = '香辣煎饼果子制作秘籍'

    # def make(self):
    #     print(f'使用{self.kongfu}制作出正宗煎饼果子')

class tudi(shcool,shifu):
    pass

t = tudi()

# print(t.kongfu)
t.make()