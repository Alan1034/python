
# s="2022china"
# print(s[-1]+s[2]*2)

# import pandas as pd
# df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
# print(df.loc[0,'A'])
# print(df.iloc[0,0])
# print(df.at[0,'A'])
# print(df.iat[0,0])

# import pandas as pd
# import numpy as np
# data = pd.DataFrame(np.random.randn(3,3))
# print(data.shape)

# import numpy as np
# # 创建3行2列的数组，填充1-6的整数
# arr = np.arange(1,  7).reshape(3, 2)
# # 打印结果
# print(arr)

# class Phone:
#   def __init__(self, brand, price):
#     self.brand = brand
#     self.price = price
#
# new = Phone("Apple", 999)
# print(new.brand)
# print(new.price)

# class SweetPotato:
#     def __init__(self):
#         self.condiments=[]
#     def add_condiment(self,condiment):
#         self.condiments.append(condiment)
#     def __str__(self):
#         return "添加的调料有：%s"%(str(self.condiments))
#
# sp=SweetPotato()
# sp.add_condiment("番茄酱")
# sp.add_condiment("芥末")
# print(sp)

# import numpy as np
# nda =np.ndarray(shape=(3,4), dtype=int)
# # print(nda)
# print(nda.shape)
# print(nda.size)
# print(nda.dtype)
# print(nda.ndim)
# print(nda.strides)

# # 输入三条边长
# a = float(input("请输入第一条边长: "))
# b = float(input("请输入第二条边长: "))
# c = float(input("请输入第三条边长: "))
#
# # 判断是否能构成三角形
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("这是一个等边三角形。")
#     elif a == b or b == c or a == c:
#         print("这是一个等腰三角形。")
#     else:
#         print("这是一个普通三角形。")
# else:
#     print("输入的边长不能构成三角形。")

# 下面是一个简洁的循环计算器示例：用户反复输入两个数字和运算符（\+，\-，\*，/），输入 `q` 可退出；包含输入校验与除零处理。
#
# ```python
# python
# def to_float(s):
#     try:
#         return float(s)
#     except ValueError:
#         return None
#
# def calc(a, b, op):
#     if op == '+':
#         return a + b
#     if op == '-':
#         return a - b
#     if op == '*':
#         return a * b
#     if op == '/':
#         if b == 0:
#             raise ZeroDivisionError("除数不能为零")
#         return a / b
#     raise ValueError("未知的运算符")
#
# def main():
#     while True:
#         s = input("请输入第一个数字（输入 q 退出）: ").strip()
#         if s.lower() == 'q':
#             print("已退出。")
#             break
#         a = to_float(s)
#         if a is None:
#             print("无效的数字，重试。")
#             continue
#
#         op = input("请输入运算符（+ - * /，输入 q 退出）: ").strip()
#         if op.lower() == 'q':
#             print("已退出。")
#             break
#         if op not in ('+', '-', '*', '/'):
#             print("不支持的运算符，重试。")
#             continue
#
#         t = input("请输入第二个数字（输入 q 退出）: ").strip()
#         if t.lower() == 'q':
#             print("已退出。")
#             break
#         b = to_float(t)
#         if b is None:
#             print("无效的数字，重试。")
#             continue
#
#         try:
#             result = calc(a, b, op)
#         except ZeroDivisionError:
#             print("错误：除以零。")
#             continue
#         except ValueError as e:
#             print(f"错误：{e}")
#             continue
#
#         print(f"结果: {a} {op} {b} = {result}")
#
# if __name__ == "__main__":
#     main()


# # 定义元组并拆包
# student = ("张三", 20, "男")
# name, age, gender = student
#
# # 输出结果
# print("姓名:", name)
# print("年龄:", age)
# print("性别:", gender)

# 使用 \`lambda\` 和 \`map\` 对列表中每个字符串调用 \`.upper()\` 转为大写。
# string_list = ["hello", "world", "python"]
# uppercase_list = list(map(lambda s: s.upper(), string_list))
# print(uppercase_list)  # 输出: ['HELLO', 'WORLD', 'PYTHON']
#
# # 可封装为一个 lambda 函数
# to_upper_list = lambda lst: list(map(lambda s: s.upper(), lst))
# print(to_upper_list(["a", "b", "c"]))  # 输出: ['A', 'B', 'C']
#
# uppercase_list1=list(map(lambda a:a.upper(),string_list))

# 下面先简要说明：先用 `reverse()` 将列表反转，再用 `sort(key=lambda s: s[2], reverse=True)` 按成绩降序排序，计算平均年龄并输出前三名（若不足三名则输出全部）。

# students = [('Alice', 20, 85), ('Bob', 19, 92), ('catherine', 21, 78), ('David', 20, 95), ('Emily', 19, 88)]
#
# # 反转列表
# students.reverse()
#
# # 按成绩从高到低排序（第三个元素是成绩）
# students.sort(key=lambda s: s[2], reverse=True)
#
# # 计算平均年龄
# avg_age = sum(s[1] for s in students) / len(students) if students else 0
#
# # 输出结果
# print(f"平均年龄: {avg_age}")
# top_n = students[:3]
# print("前三名学生信息（姓名, 年龄, 成绩）:")
# for name, age, score in top_n:
#     print(name, age, score)
#

# 下面的程序从文件 `numbers.txt` 逐行读取、去除空白并把每行转换为整数，累加求和并输出总和；如果文件不存在会提示错误，若遇到非整数字行会记录警告并跳过。


# def main():
#     filename = 'numbers.txt'
#     total = 0
#     try:
#         with open(filename, 'r', encoding='utf-8') as f:
#             for lineno, line in enumerate(f, start=1):
#                 s = line.strip()
#                 if s == '':
#                     continue
#                 try:
#                     total += int(s)
#                 except ValueError:
#                     print(f"警告：第{lineno}行不是整数，已跳过: {s}")
#         print(f"总和: {total}")
#     except FileNotFoundError:
#         print(f"错误：找不到文件 {filename}")
#
# if __name__ == '__main__':
#     main()


# 函数说明：`greet` 接受可选参数 `name`（默认值为 `朋友`），使用 f-string 返回格式化的问候语，并包含文档字符串。
#
# ```python
# def greet(name="朋友"):
#     return f"你好，{name}!欢迎使用聊天机器人。"
#
# print(greet())
# print(greet("小明"))

# tuple1 = ('DNA'), (['DNA','RNA','AA','peptide'])
# tuple2 =('DNA') + (['DNA','RNA','AA','peptide'])
#
# print(tuple1)
# print(tuple2)

numbers = [1, 2, 3, 4, 5, 6]
filtered_numbers = [number for index, number in enumerate(numbers) if index % 2 == 0]
print(filtered_numbers)