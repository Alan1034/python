
def print_info(fn_name):
    def inner(a,b):
        print("正在努力计算中...")
        fn_name(a,b)
    return inner

def logging(flag):
    def print_info(fn_name):
        def inner(a,b):
            if flag=='+':
               print("正在努力计算 加法 中...")
            if flag=='-':
               print("正在努力计算 减法 中...")
            fn_name(a,b)
        return inner
    return print_info


# @print_info
@logging("+")
def add(a,b):
    result = a + b
    print(result)

# @print_info
@logging("-")
def substract(a,b):
    result = a - b
    print(result)

if __name__ == '__main__':
    add(11,233)
    substract(11,233)

def func_out():
    a=100
    def func_inner():
        # 声明变量
        nonlocal a
        a=a+1
        print(a)
    return func_inner

number=func_out()
number()

def check(fn):
    def inner():
        print("登录验证")
        fn()
    return inner

def comment():
    print("发表评论")

comment=check(comment)
comment()