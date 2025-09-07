import time

import streamlit as st

st.title("测试标题")
st.write("你好")
st.divider()

# 输入框
name = st.chat_input("请输入您的名字")
if name:
    st.write(f"你好：{name}")

# 等待
with st.spinner("思考中"):
    time.sleep(5)
    st.write("思考完成")

    # 消息容器
    # 角色支持：user、assistant、ai、human
st.chat_message("user").markdown("你是谁")
st.chat_message("assistant").markdown("我是聊天机器人")