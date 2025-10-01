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

prices=[80,90,85,95,70]
prices.sort()
print(prices)
prices.sort(reverse=True)
print(prices)
print(pd.Series(prices).mean())
print(min(prices))