# import random
#
# str1 = "0123456789abcdefghijklmnopqrstuvWxyZABCDEFGHIKLMNOPQRSTUVWXYZ";
# ranList = [];
# x = 0;
# while x < 4:
#     x += 1;
#     ranList.append(str1[random.randint(1, len(str1))]);
#
# print(ranList);

# defUser="admin"
# defPassword="admin888";
#
# times=0
#
#
# while times<3:
#     user=input('请输入用户名：')
#     password=input("请输入密码：");
#     if user==defUser and password==defPassword:
#         print("登陆成功");
#         break;
#     else:
#         print("用户名或密码输入错误");
#         times=times+1;

# class BankAccount(object):
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         self.balance -= amount
#     def __str__(self):
#         return "Name: {}, Balance: {}".format(self.name, self.balance);
# a1=BankAccount("Alan", 100);
# a1.deposit(100);
# print(a1);

# str="hello world"
# dict={}
# for text in str:
#     try:
#         dict[text]
#     except KeyError:
#         dict[text]=0
#
#     if dict[text]>0:
#         dict[text]=dict[text]+1
#     else:
#         dict[text]=1
# print(dict)
b=-0.5
print(type(b))
a=float("123456")
print(type(a))