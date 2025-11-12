
import torch.nn as nn
import torch

class GRUTimeSeriesPredictor(nn.Module):
    def __init__(self,input_size: int,       # 输入特征维度
                 hidden_size: int,      # GRU隐藏层维度
                 num_layers: int = 1,   # GRU层数
                 batch_size: int = 3,
                 ):  # 输出维度
        super().__init__()

    # 创建GRU层
        self.gru=nn.GRU(input_size=input_size,hidden_size=hidden_size,num_layers=num_layers)
            # 初始化隐藏状态
        self.h0=torch.randn(num_layers,batch_size,hidden_size)
    def forward(self, x: torch.Tensor):

        output,hn = self.gru(x,self.h0)
        print(output, hn)
        return {"output_size":output.shape,"batch_size":hn.shape}


if __name__ == '__main__':
    input_size = 5       # 每个时间步的输入特征数
    hidden_size = 32     # GRU隐藏层维度
    num_layers = 2       # GRU层数
    output_size = 1      # 预测输出的维度
    batch_size=3

    # 实例化模型
    model = GRUTimeSeriesPredictor(
        input_size=input_size,
        hidden_size=hidden_size,
        num_layers=num_layers
    )

    x_test = torch.randn(size=(1, batch_size, input_size))
    y_pred = model(x_test)
    print(y_pred)