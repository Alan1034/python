import copy
import torch
import torch.nn as nn
import math

from transformer.Encoder import clones, SublayerConnection, MultiHeadedAttention, PositionwiseFeedForward, test_encoder


class DecoderLayer(nn.Module):
    def __init__(self, size, self_attn, src_attn, feed_forward, dropout_p):
        super(DecoderLayer, self).__init__()
        self.size = size
        self.self_attn = self_attn
        self.src_attn = src_attn
        self.feed_forward = feed_forward
        self.sublayer = clones(SublayerConnection(size, dropout_p), 3)
    def forward(self, x, memory, source_mask, target_mask):
        x=self.sublayer[0](x, lambda x: self.self_attn(x, x, x, target_mask))
        x=self.sublayer[1](x, lambda x: self.src_attn(x, memory, memory, source_mask))
        x=self.sublayer[2](x, self.feed_forward)
        return x

class Decoder(nn.Module):
    def __init__(self, layer, N):
        super(Decoder, self).__init__()
        self.layers=clones(layer, N)

    def forward(self, x, memory, source_mask, target_mask):
        for layer in self.layers:
            x=layer(x, memory, source_mask, target_mask)
        return x
