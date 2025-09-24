from numpy.f2py.auxfuncs import throw_error

with open ('./1.txt','w',encoding='utf-8') as dest_f:
     dest_f.write("Python高级阶段\n")
     dest_f.write("Python高级阶段2")
try:
    with open('./1.txt','r',encoding='utf-8') as src_f:
        data= src_f.read()
        print(data)
except Exception as e:
    print(e)

listStr='[1,2,3,4]'
list1=eval(listStr)
print(list1)

# i=1
# while i<11:
#
#   if i%2==1:
#       print(i)
#   i=i+1;
# else:
#   print("已完成")

# list1=[1,2,3,4,5,6,7,8,9,10]
# to_sum=0
# for i in list1:
#     to_sum= to_sum + i
# print(to_sum/len(list1))
#
# employee_records={}
# employee_records['1001']={'name':"Alice",'age':25,'position':'Manager'}
# employee_records['1002']={'name': 'Bob','age': 30,'position': 'Engineer'}
#
# while True:
#     handle = int(input("请输入您的操作:1、查询；2、增加；3、删除；4、退出"))
#     # 3.每次要判断用户猜的数和底数大小,并给出提示
#     if handle== 1:
#       try:
#           record_num= input("请输入要查询的编号：")
#           print(employee_records[record_num])
#       except KeyError:
#           print("没有此编号")
#     elif handle== 2:
#
#       record_num= input("请输入要添加的编号：")
#       try:
#
#           if employee_records[record_num]:
#               print("编号已存在")
#               continue
#       except Exception as e:
#           print("添加失败",e)
#       employee_records[record_num]={}
#       employee_records[record_num]['name']=input("请输入要添加的姓名：")
#       employee_records[record_num]['age']=input("请输入要添加的年龄：")
#       employee_records[record_num]['position']=input("请输入要添加的职位：")
#       print(employee_records)
#
#     elif handle== 3:
#         record_num= input("请输入要删除的编号：")
#         try:
#             del employee_records[record_num]
#             print("删除成功")
#         except Exception as e:
#             print("删除失败",e)
#
#     elif handle== 4:
#         print("已退出")
#         break
#     else:
#         print("输入错误")

# score = int(input("请输入您的成绩："))
# if score >= 90:
#     print("优秀")
# elif score >= 80:
#     print("良好")
# elif score >= 70:
#     print("合格")
# elif score >= 60:
#     print("及格")
# elif score <= 0:
#     print("输入错误")
# else:
#     print("输入错误")

# day=int(input("请输入今天的日期："))
# if day in [6,7]:
#     print("周末")
# elif day>7 or day<1:
#     print("输入错误")
# else:
#     print("工作日")

# i=1
# factorial=1
# while i<6:
#     factorial=factorial*i
#     i=i+1
#
# print(factorial)

# str1="helloworldhellopythonhelloc++hellojava"
#
# def findall(str1,substr):
#     list1=[]
#
#     while str1.find(substr)!=-1:
#         index=str1.find(substr)
#         if len(list1)>0:
#
#           list1.append(index+list1[-1]+len( substr))
#         else:
#           list1.append(index)
#         str1=str1[index+len( substr):]
#
#     return tuple(list1)
#
# print(findall(str1,"hello"))
import random

names =['A','B','C','D','E','H']
list1=[[],[],[]]
for i in names:
    list1[random.randint(0,2)].append(i)
print(list1)
