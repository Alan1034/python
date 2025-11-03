import torch
import torch.nn as nn
from torch import optim

data=torch.tensor([[0,0],[0,1],[1,0],[1,1.]],requires_grad= True)
target=torch.tensor([[0],[0],[1],[1.]],requires_grad= True)

model=nn.Linear(2,1)

def train():
    opt=optim.SGD(params= model.parameters(),lr=0.1)
    for iter in range (20):
        # 消除之前的梯度（如果存在）
        opt.zero_grad()
        # 预测
        pred=model(data)
        # 计算损失
        loss=((pred-target)**2).sum()
        # 指出那些导致损失的参数,反向传播
        loss.backward()
        for name,param in model.named_parameters():
            print(name,param.data,param.grad)

        # 更新参数
        opt.step()
        print(iter,loss.data)

if __name__=='__main__':
    train()