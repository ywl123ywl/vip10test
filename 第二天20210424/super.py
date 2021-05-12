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

    def make(self):
        self.__init__()
        print(f'使用{self.kongfu}制作出正宗煎饼果子')

    def old_make(self):
        super().__init__()
        super().make()

class tusun(tudi):
    pass

ts = tusun()
ts.make()
ts.old_make()


s = shcool()
s.make()
s.old_make()
