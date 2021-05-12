

class Dog():
    def work(self):
        print('指哪打哪')

class ADog(Dog):
    def work(self):
        print('追击犯人')

class DDog(Dog):
    def work(self):
        print('查找毒品')

class Person():
    def zhishi(self,d_work):
        d_work.work()

ad = ADog()
dd = DDog()

p = Person()
p.zhishi(ad)
p.zhishi(dd)