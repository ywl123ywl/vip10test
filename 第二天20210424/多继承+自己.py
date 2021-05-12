class shifu(object):

    def __init__(self):
        self.kongfu = '五香煎饼果子制作秘籍'

    def make(self):
        print(f'使用{self.kongfu}制作出正宗煎饼果子')

class shcool(object):

    def __init__(self):
        self.kongfu = '香辣煎饼果子制作秘籍'

    def make(self):
        print(f'使用{self.kongfu}制作出正宗煎饼果子')

class tudi(shcool,shifu):

    def __init__(self):
        self.kongfu = '清真煎饼果子制作秘籍'

    def make(self):
        self.__init__()
        print(f'使用{self.kongfu}制作出正宗煎饼果子')

    def shifu_make(self):
        shifu.__init__(self)
        shifu.make(self)

    def shcool_make(self):
        shcool.__init__(self)
        shcool.make(self)

class tusun(tudi):
    pass

xm = tusun()

xm.make()
xm.shcool_make()
xm.shifu_make()