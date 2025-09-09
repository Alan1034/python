# 单行注释
"""
多行注释
换行
"""
print('hello world')

"""
变量=变量的值
print()函数实现对变量的引用
"""

name = 'Tom'
age = 23
address = '北京市昌平区'
print(name)
print(age)
print(address)
print(name, age, address)

"""
数据类型
"""
a = 10
print(a)
print(type(a))

b = 9.88
print(b)
print(type(b))

c = False
print(c)
print(type(c))

d = 'Hello Python!'
print(d)
print(type(d))

num1 = 9
num2 = 4

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)  # 返回类型为Floot浮点类型
print(num1 // num2)  # 返回类型为Int整数类型
print(num1 ** num2)  # 返回9的4次方
print(num1 % num2)

"""
输入

"""
#
# password=input("请输入您的银行卡密码：")
# print(password)
# print(type(password))
#
# num1=int(input('请输入一个整数'))
# print(num1)
# print(type(num1))
#
# num2=float(input('请输入一个浮点数：'))
# print(num2)
# print(type(num2))

"""
输出
"""

print("变量或者内容", "Sun", sep="（分隔符）", end="（结束符）")

name = 'Rose'
age = 19
print(f'我的名字叫做{name}，今年{age}岁了！')

goods_name = '胡萝卜'
goods_price = 5.5
print(f'今天蔬菜特价了，{goods_name}只要{goods_price:.2f}元/斤')

# age = int(input('请输入您的年龄：'))
# if 60 > age >= 18:
#     print('您已满18岁，可以正常上网')
# elif age >= 60:
#     print("退休年龄")
# else:
#     print('未满18岁，禁止未成年人上网！')


# proof=int(input('请输入车辆驾驶员每100ml血液中酒精含量：'))
#
# if proof>=20:
#     # pass
#     if proof >= 80:
#         print("涉嫌醉驾！")
#     else:
#         print("涉嫌酒驾")
# else:
#     print("不构成酒驾")


# from random import randint
#
# player = int(input('请输入您的出拳信息（1-石头、2-剪刀、3-布）'))
#
# computer = randint(1, 3)
#
# if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
#     print('玩家获胜')
# elif player == computer:
#     print("平局")
# else:
#     print("电脑获胜")

str1 = 'simple'
for i in str1:
    print(i)

# 从1循环到100累加
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

for i in range(1, 6):
    if i==4:
        print("已经吃饱了，后面的苹果就不吃了")
        break
    print(f"正在吃第{i}个苹果")

for i in range(1, 6):
    if i==3:
        print("不好，有大虫，这个苹果不吃了")
        continue
    print(f"正在吃第{i}个苹果")