from sklearn.neighbors import KNeighborsClassifier
def dme3():
    x=[[39,0,31],[3,2,65],[2,3,55],[9,38,2],[8,34,17],[5,2,57],[21,17,5],[45,2,9]]
    y=[0,1,2,2,2,1,0,0]
    estimator =KNeighborsClassifier(n_neighbors=5)
    estimator.fit(x,y)
    mypre =estimator.predict([[23,3,17]])
    print(f"预测结果为：{mypre}")
dme3()


from sklearn.neighbors import KNeighborsRegressor
def dm_02():
    estimator=KNeighborsRegressor(n_neighbors=2)
    x=[[0,0,1],[1,1,0],[3,10,10],[4,11,12]]
    y=[0.1,0.2,0.3,0.4]
    estimator.fit(x,y)
    myrtle=estimator.predict([[3,11,10]])
    print('myrtle-->',myrtle)

dm_02()

import numpy as np
from sklearn.preprocessing import MinMaxScaler

def dm_min_max_scaler():
    # 1.准备数据
    data=[[90,2,10,40],[60,4,15,45],[75,3,13,46]]

    # 2.初始化归一化对象
    transformer = MinMaxScaler()

    # 3.对原始特征进行变换
    data=transformer.fit_transform(data)

    # 4.打印归一化后的结果
    print(data)
dm_min_max_scaler()

from sklearn.preprocessing import StandardScaler
def dm_standard_scaler():
    # 1.准备数据
    data= [[90, 2, 10, 40],[60, 4, 15, 45],[75, 3, 13, 46]]

    # 2.初始化标准化对象
    transformer = StandardScaler()

    # 3.对原始特征进行变换
    data=transformer.fit_transform(data)

    # 4.打印标准化的结果
    print(data)

    # 5.打印每一列数据的标准值和标准差
    print('transfer.mean_',transformer.mean_)
    print('transfer.car_',transformer.var_)
dm_standard_scaler()