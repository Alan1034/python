import torch
import torch.nn as nn
import math

from input import *
import copy

def attention(query, key, value, mask=None, dropout=None):
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
    if mask is not None:
        scores = scores.masked_fill(mask==0, -1e9)
    p_attn = torch.softmax(scores, dim=-1)
    if dropout is not None:
        attn = dropout(p_attn)
    output = torch.matmul(p_attn, value)
    return torch.matmul(p_attn,value), p_attn

def clones(module, N):
    return nn.ModuleList([copy.deepcopy(module) for _ in range(N)])

class MultiHeadedAttention(nn.Module):
    def __init__(self, head, embedding_dim, dropout_p=0.1):
        super(MultiHeadedAttention, self).__init__()
        assert embedding_dim % head == 0,'embedding_dim不能head被整除'
        self.d_k=embedding_dim // head
        self.head = head
        self.linears = clones(nn.Linear(embedding_dim, embedding_dim), 4)
        self.attn=None
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, query, key, value, mask=None):
        batch_size=query.size()[0]
        myoutptlist_data=[]
        for model,x in zip(self.linears,(query,key,value)):
            myoutput=model(x)
            tmpmyoutput=myoutput.view(batch_size, -1, self.head, self.d_k).transpose(1,2)
            myoutptlist_data.append(tmpmyoutput)
        query,key,value=myoutptlist_data
        c,self.attn=attention(query, key, value, mask=mask, dropout=self.dropout)
        x=c.transpose(1,2).contiguous().view(batch_size, -1, self.d_k*self.head)
        return self.linears[-1](x)

class PositionwiseFeedForward(nn.Module):
    def __init__(self, d_model, d_ff, dropout_p=0.1):
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)
        self.linear2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, x):
        return self.linear2(self.dropout(torch.relu(self.linear1(x))))

class SublayerConnection(nn.Module):
    def __init__(self, size, dropout_p=0.1):
        super().__init__()
        self.size = size
        self.dropout_p = dropout_p
        self.norm = nn.LayerNorm(size)
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, x, sublayer):
        return self.norm(x + self.dropout(sublayer(x)))
class EncoderLayer(nn.Module):
    def __init__(self, size, self_attn, feed_forward, dropout_p):
        super(EncoderLayer, self).__init__()
        self.self_attn = self_attn
        self.feed_forward = feed_forward
        self.size = size
        self.dropout_p = dropout_p
        self.sublayer = clones(SublayerConnection(self.size, self.dropout_p), 2)

    def forward(self, x, mask):
        x = self.sublayer[0](x, lambda x: self.self_attn(x, x, x, mask))
        x = self.sublayer[1](x, self.feed_forward)
        return x

class Encoder(nn.Module):
    def __init__(self, layer, N):
        super(Encoder, self).__init__()
        self.layers = clones(layer, N)

    def forward(self, x, mask):
        for layer in self.layers:
            x = layer(x, mask)
        return x
