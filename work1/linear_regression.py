# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt
#
# plt.rcParams['font.sans-serif'] = ['SimHei', 'FangSong', 'Microsoft YaHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# path = './data.xlsx'
# df = pd.read_excel(path)
#
# x=df[['电视广告数（x)']].values.tolist()
# y=df['汽车销售数（y）'].tolist()
# # 2 实例化 线性回归模型 estimator
# estimator = LinearRegression()
# # 3 训练 线性回归模型fit() h(w) = w1x1 + w2x2 + b
# estimator.fit(x, y)
#
# print('斜率_-->', estimator.coef_)
# print('截距_-->', estimator.intercept_)
#
# # 可视化
# plt.figure(figsize=(8, 6))
# plt.scatter([item[0] for item in x], y, color='blue', alpha=0.7, label='样本点')
#
# x_line = np.linspace(min([item[0] for item in x]), max([item[0] for item in x]), 200).reshape(-1, 1)
# y_line = estimator.predict(x_line)
# plt.plot(x_line[:, 0], y_line, color='red', linewidth=2,
#          label=f'回归线: y = {estimator.coef_[0]:.4f}x + {estimator.intercept_:.4f}')
# # 修正x_col和y_col
# plt.xlabel('电视广告数（x)')
# plt.ylabel('汽车销售数（y）')
# plt.title('电视广告数 vs 汽车销售数 线性回归')
# plt.legend()
# plt.grid(True)
# plt.show()

from sklearn.linear_model import LinearRegression

x_train=[[160],[166],[172],[174],[180]]
y_train=[56.3,60.6,65.1,68.5,75]
es=LinearRegression()
es.fit(x_train,y_train)
x_test=[[176]]
y_predict=es.predict(x_test)
print(f"预测值为{y_predict}")

print(f"权重（斜率）：{es.coef_}")
print(f"偏置（截距）：{es.intercept_}")