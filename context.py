"""
with语法功能之所以那么强大，底层用到的就是：上下文管理器
with管理的就是上下文管理器对象

__enter__()会在with语句前执行，一般用于：初始化对象
__exit__()会在with语句后执行，一般用于：释放
"""

class MyFile(object):
    def __init__(self,file_name,file_model):
        self.file_name = file_name
        self.file_model = file_model
        self.file_content = None #初始化

    # 上文管理器，即__enter__()会在with前，自动执行，一般用于初始化：对象
    def __enter__(self):
        self.file_content = open(self.file_name,self.file_model,encoding='utf-8')
        return self
        # return self.file_content

    # 下文管理器，即：__exit__()，会在with语句后，自动执行
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        self.file_content.close()
        print("文件对象已被释放！")

# 在main方法中测试
if __name__ == '__main__':
    with MyFile("./2.txt","w") as self_obj:
        self_obj.file_content.write('我是上下文管理器对象')