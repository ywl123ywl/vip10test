# class Dog():
#     __tooth = 10
#     # 类方法
#     @classmethod
#     def get_tooth(cls):
#         return cls.__tooth
#
#
# xiaohei = Dog()
# print(xiaohei.get_tooth())



class Dog():
    # 静态方法
    @staticmethod
    def info_print():
        print('这是一个狗类')

xiaohei = Dog()
xiaohei.info_print()
Dog.info_print()