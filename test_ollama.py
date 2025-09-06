import ollama;

client = ollama.Client(host='http://localhost:11434')

# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello("Ollama")
# list列出有哪些可用模型
# print(client.list())

# # 查看模型详情
# print(client.show("deepseek-r1:8b"))

# # 查看哪些模型在运行中
# print(client.ps())

# 和模型对话
while True:
    prompt = input("请输入问题：")
    res = client.chat(model="deepseek-r1:8b", messages=[{
        "role": "user",
        "content": prompt
    }])

    print(res['message']['content'])
