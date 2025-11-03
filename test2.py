import pandas as pd
# sex=int(input("请输入您的性别，1：男，2：女"))
# height=int(input("请输入您的身高"))
# weight=int(input("请输入您的体重"))
# visionR=float(input("请输入您的右眼视力"))
# visionL=float(input("请输入您的左眼视力"))
#
# if (sex==1)&(height>160)&(weight>=60)&(weight<90)&(visionR>4.6)&(visionL>4.5):
#     print("通过")
# else:
#     print("不通过")

# scores=[80,90,85,95,70]
#
# def calculate_total(scores_inner):
#     return pd.Series(scores_inner).sum()
#
# def calculate_average(scores_inner):
#     to_sum=calculate_total(scores_inner)
#     return to_sum/len(scores_inner)
#
# print(calculate_total(scores))
# print(calculate_average(scores))

# def print_info(**kwargs):
#     print(kwargs)
#     print("姓名：",kwargs['name'])
#     print("年龄：",kwargs['age'])
#     print("城市：",kwargs.get('city',"未知"))
#     print("性别：",kwargs.get('sex',"未知"))
#
# print_info(name="Alan",age=18,sex="男")

# prices=[80,90,85,95,70]
# prices.sort()
# print(prices)
# prices.sort(reverse=True)
# print(prices)
# print(pd.Series(prices).mean())
# print(min(prices))

# import pandas as pd
#
# s4 = pd.Series([i for i in range(6)], index=[i for i in 'ABCDEF'])
#
# # Series和数值型变量计算
# print(s4 * 5)
#
#
#  # 索引完全相同的两个Series对象进行计算
# print(s4)
# # 构造与s4索引相同的s对象
# s5 = pd.Series([10] * 6, index=[i for i in 'ABCDEF'])
# print(s5)
# # 两个索引相同的s对象进行运算
# print(s4 + s5)
#
# # 索引不同的两个s对象运算
# print(s4)
# # 注意s6的最后一个索引值和s4的最后一个索引值不同
# s6 = pd.Series([10]*6, index=[i for i in 'ABCDEG'])
# print(s6)
# print(s4 + s6)

# import pandas as pd
#
# # 使用默认自增索引
# s2 = pd.Series([1, 2, 3])
# print(s2)
# # 自定义索引
# s3 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
# print(s3)
#
# import pandas as pd
#
# # 使用元组
# tst = (1, 2, 3, 4, 5, 6)
# s1 = pd.Series(tst)
# print(s1)
# print(type(s1))
#
# # 使用字典：
# dst = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}
# s2 = pd.Series(dst)
# print(s2)
# print(type(s2))



