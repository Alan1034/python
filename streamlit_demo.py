import time

import streamlit as st
if "count"not in st.session_state:
    st.session_state["count"] = 1
if "message"not in st.session_state:
    st.session_state["message"] = []
count = 1
st.title("测试标题")

st.divider()

prompt = st.chat_input("请输入您的问题")

# 消息容器
# if prompt:
#     st.chat_message("user").markdown(prompt)
#     with st.spinner("思考中..."):
#         time.sleep(1)
#         st.chat_message("assistant").markdown(f"我不知道{st.session_state["count"]}")
#         st.session_state["count"] += 1

if prompt:
    st.session_state["message"].append({"role":"user", "content":prompt})
    for message in st.session_state["message"]:
        st.chat_message(message["role"]).markdown(message["content"])


    with st.spinner("思考中..."):
        time.sleep(1)
        res=f"我不知道{st.session_state["count"]}"

        # 把AI的回答记录到历史记录中
        st.session_state["message"].append({"role":"assistant", "content":res})
        st.session_state["count"] += 1
        # 渲染
        st.chat_message("assistant").markdown(res)