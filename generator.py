# """
# 括号()代表这是一个生成器，不是元组
# 括号()里面写的是数据的生成规则，返回一个对象
# """
#
# my_generator=(i*2 for i in range(5))
# print(my_generator)
#
# # # next获取生成器下一个值
# value=next(my_generator)
# print(value)
#
# # # 遍历生成器
# for value in my_generator:
#     print(value)
import math
# batch_size每批次的数据条数
def dataset_loader(batch_size):
    with open("./1.txt","r",encoding="utf-8") as src_f:
        data_lines=src_f.readlines() #一次性读取所有行，放到列表中
    # line_count总条数
    line_count=len(data_lines)
    # batch_count总批次数量
    batch_count=math.ceil(line_count/batch_size)
    for batch_id in range(batch_count):
        yield data_lines[batch_id*batch_size:(batch_id+1)*batch_size]
if __name__=="__main__":
    my_generator=dataset_loader(5)
    print(next(my_generator))
    print(next(my_generator))
    for batch_value in my_generator:
        print(batch_value)