# 1.定义一个学生类
class Student(object):
    def __init__(self, age=23, value=1):
        self.age = age
        self.data = value

    def __call__(self, x):
        return self.data + x

    # 2.定义属性和方法
    def eat(self):
        # self也是Python内置的关键字之一，其指向了类实例对象本身
        print(self)  # <__main__.Student object at 0x000001A56E338EC0>
        print('I can eat food')

    def drink(self):
        print('I can drink warter')


# 3.实例化Student类，获取S1对象
s1 = Student()
s1.eat()
s1.drink()

s2 = Student()
s2.eat()
s2.drink()

# 设置属性
s1.name = 'Tom'

# 获取属性
print(s1.name)

# __init__()魔术方法
s3 = Student(32)
print(s3.age)

# __call__()魔术方法

s4 = Student()
print(s4(1))

# 定义一个Apprentice子类
class Apprentice(Student):
    #     super()调用父类属性和方法
    def __init__(self, age=23, value=1,level=0):
        super().__init__(age, value)
        self.level = level
    # 重写
    def drink(self):
        print('I can drink juice')


# 实例化子类对象
s5=Apprentice(63)
print(s5.age)
s5.drink()

s6=Apprentice(63,level=3)
print(s6.level)
