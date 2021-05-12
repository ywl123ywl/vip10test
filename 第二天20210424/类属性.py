

class Dog():
    tooth = 10

xiaohei = Dog()
xiaohuang = Dog()

print(xiaohei.tooth)
print(xiaohuang.tooth)

Dog.tooth = 15
xiaohei.tooth = 20

print(Dog.tooth)
print(xiaohei.tooth)
print(xiaohuang.tooth)