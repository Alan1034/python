"""
使用Pytorch完成以下操作:1.导入pytorch包( ) 2.创建一个空的5x3张量( )
3.创建一个随机初始化的5x3张量( )4.创建一个5x3的0张量，类型为long( )
5.直接从数组创建张量( )6.创建一个5x3的单位张量，类型为double()
7.从已有的张量创建相同维度的新张量并目重新定义类型为float()
8,打印一个张量的维度()9.将两个张量相加( )
 10.取张量的第一列( ) 11.将一个4x4的张量resize成-个一维张量()
 12.将一个4x4的张量，resize成一个2x8的张量(
"""

import torch
import numpy as np

# 2
data2=torch.tensor([5,3])
print(data2)
# 3
data3=torch.randn([5,3])
print(data3)
# 4
data4=torch.zeros(5,3,dtype=torch.long)
print(data4)
# 5
data5=torch.from_numpy(np.array([1,2,3]))
print(data5)
# 6
data6=torch.eye(5,3,dtype=torch.double)
print(data6)
#7
data7=data3.new_zeros((5,3),dtype=torch.float)
print(data7)
#8
print(data7.shape)
#9
data9=torch.randn(5,3)
data99=torch.add(data9,data3)
print(data99)
#10
print(data3[:,0])
#11
data11=torch.randn(4,4)
print(data11)
data111=data11.view(-1)
print(data111)
#12
data12=torch.randn(4,4)
print(data12.view(2,8))