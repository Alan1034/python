"""

请用pytorch实现加性注意力机制
实现步骤参考:
第一步: 根据注意力计算规则,对Q，K，V进行相应的计算,
第二步:根据第一步采用的计算方法,如果是拼接方法，则需要将Q与第二步的计算结果再进行拼接,如果是转置点积,一般是自注意力,Q与V相同
则不需要进行与Q的拼接.
第二步:最后为了使整个attention机,制按照指定尺寸输出,使用线性层作用在第二步的结果上做一个线性变换,得到最终对Q的注意力表示
"""
import torch
import torch.nn as nn

class AdditiveAttention(nn.Module):
    def __init__(self,query_size, key_size, hidden_size, output_size):
        super(AdditiveAttention, self).__init__()
        self.query_size = query_size
        self.key_size = key_size
        self.hidden_size = hidden_size
        self.output_size = output_size

#         线性层1
        self.attn1 = nn.Linear(query_size+key_size, hidden_size)
        # 线性层2
        self.attn2 = nn.Linear(hidden_size, 1)
        self.attn_combine=nn.Linear(hidden_size*2,output_size)
    def forward(self,x,Q,K,V):
        # print('V--->', V.shape, V)
        expand_Q = Q.transpose(0,1).expand(-1,K.shape[1],-1)
        attn_score=self.attn2(torch.tanh(self.attn1(torch.cat(tensors=[expand_Q,K],dim=-1)))).squeeze(-1)
        attn_weight=torch.softmax(attn_score,dim=-1).unsqueeze(dim=1)
        attn_applied=torch.bmm(attn_weight,V)
        output=torch.cat(tensors=[x,attn_applied],dim=-1)
        output=self.attn_combine( output)
        return output,attn_weight

if __name__ == '__main__':
    query_size = 32
    key_size = 32
    seq_len = 32 # 32个单词
    hidden_size = 32 # 32个特征
    output_size = 32

    x = torch.randn(1, 1, hidden_size)
    Q = torch.randn(1, 1, query_size)
    K = V = torch.randn(1, seq_len, hidden_size)

    myattobj = AdditiveAttention(query_size, key_size, hidden_size, output_size)
    output, attn_weights = myattobj.forward(x,Q, K, V)
    print('查询张量q的注意力结果表示output--->', output.shape, output)
    print('查询张量q的注意力权重分布attn_weights--->', attn_weights.shape, attn_weights)