class shifu(object):

    def __init__(self):
        self.kongfu = '五香煎饼果子制作秘籍'

    def make(self):
        print(f'使用{self.kongfu}制作出正宗煎饼果子')

class shcool(shifu):

    def __init__(self):
        self.kongfu = '香辣煎饼果子制作秘籍'

    def make(self):
        print(f'使用{self.kongfu}制作出正宗煎饼果子')

    def old_make(self):
        super().__init__()
        super().make()

class tudi(shcool):

    def __init__(self):
        self.kongfu = '清真煎饼果子制作秘籍'
        # 私有属性
        self.__money = 200000

    def get_money(self):
        return self.__money

    def set_money(self,much):
        if much > 0:
            self.__money = much

    # 私有方法
    def __info(self):
        print('我还会敲代码！！！')


    def make(self):
        self.__init__()
        print(f'使用{self.kongfu}制作出正宗煎饼果子')

    def old_make(self):
        super().__init__()
        super().make()

class tusun(tudi):
    pass


# td = tudi()
# print(td.get_money())
# td.set_money(0)
# print(td.get_money())


ts = tusun()
print(ts.get_money())
ts.set_money(100)
print(ts.get_money())