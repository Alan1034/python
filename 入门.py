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

# for i in range(1, 6):
#     if i==4:
#         print("已经吃饱了，后面的苹果就不吃了")
#         break
#     print(f"正在吃第{i}个苹果")
#
# for i in range(1, 6):
#     if i==3:
#         print("不好，有大虫，这个苹果不吃了")
#         continue
#     print(f"正在吃第{i}个苹果")

# from random import randint
#
# rand_num = randint(1, 10)
#
# for i in range(3):
#     user_num=int(input("请输入您要猜的数字："))
#     if user_num == rand_num:
#         print("恭喜你，猜对了")
#         break
#     elif user_num>rand_num:
#         print("很抱歉，猜大了")
#     else:
#         print("很抱歉，猜小了")

"""
列表的增删改查
"""
# 查询
list1=[10,20,30]
print(list1[0])

#增加
list1.append(40)
print(list1)

#删除
del list1[1]
print(list1)

#更新
list1[2]=100
print(list1)

# for循环实现列表的遍历操作
for i in list1:
    print(i)

list1=[1,2,3]
list2=[4,5,6]

# 获取列表的长度
print(len(list1))

# 使用+运算符实现列表合并
print(list1+list2)

# 使用*运算符实现列表元素的复制操作
print(list1*4)

# in关键字，判断元素是否出现在列表中
print(3 in list1)

"""
切片
切片三步走：1.看步长 2.绘制图像 3.记口诀
基本语法：
    列表名称[起始索引:结束索引:步长]
1.步长为正则从左向右移动，步长为负，则从右向左移动
2.绘制图像，把列表元素值，与正索引，负索引绘制出来
3.切片其实很简单，只顾头来尾不管，步长为正则正向移动，步长为负则逆向移动
"""
abcd_list=['a','b','c','d']
print(abcd_list[0:3:1])#1代表从左向右移动 ['a', 'b', 'c']
print(abcd_list[0:3]) #['a', 'b', 'c']

print(abcd_list[0:])#从start(0)位置开始截取，一直截取到列表尾部（包含尾部元素）['a', 'b', 'c', 'd']
print(abcd_list[:3])#从0开始截取，截取到stop-1结束 ['a', 'b', 'c']
print(abcd_list[:])#截取整个列表 ['a', 'b', 'c', 'd']
print(abcd_list[::-1]) #倒排['d', 'c', 'b', 'a']

list1=[1,2,3,1]
print(len(list1)) #4

print(max(list1)) #3
print(min(list1))#1

tuple1=(10,20,30)
print(tuple1)#(10, 20, 30)
list2=list(tuple1)
print(list2)#[10, 20, 30]
print(type(list2))#<class 'list'>

count=list1.count(1)
print(count)#2

list1.extend([4,5,6])
print(list1)#[1, 2, 3, 1, 4, 5, 6]

list1.remove(6)
print(list1)#[1, 2, 3, 1, 4, 5]

list2=[10,20,30]
list2.reverse()
print(list2)#[30, 20, 10]

list2.sort(reverse=True)
print(list2)#[30, 20, 10]

