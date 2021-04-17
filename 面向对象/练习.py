

#类
class Teacher():
    # 属性
    def __init__(self,name,sex,course):
        self.name = name
        self.sex = sex
        self.course = course
    # 方法
    def teach(self):
        print(f'{self.name}老师，性别是{self.sex}，教{self.course}课')
# 实例化
teacher = Teacher('Tom','男','中文')
# 调用类方法
teacher.teach()