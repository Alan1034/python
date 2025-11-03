
# from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler #特征处理 标准化
from sklearn.model_selection import train_test_split #数据集划分
from sklearn.linear_model import LinearRegression #正规方程回归模型
from sklearn.linear_model import SGDRegressor #梯度下降回归模型
from sklearn.metrics import mean_squared_error #均方误差评估

# datas=load_boston()
import pandas as pd
import numpy as np

data_url="http://lib.stat.cmu.edu/datasets/boston"
raw_df=pd.read_csv(data_url,sep="\\s+",skiprows=22,header=None)
print(f"raw_df：{raw_df}")
data=np.hstack([raw_df.values[::2,:],raw_df.values[1::2,:2]])
target=raw_df.values[1::2,2]

print(f"特征：{data[:5]}")
print(f"标签：{target[:5]}")