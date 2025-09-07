import ollama;

import streamlit as st
client = ollama.Client(host='http://localhost:11434')

if "message"not in st.session_state:
    st.session_state["message"] = []

st.title("聊天机器人")
st.divider()
prompt = st.chat_input("请输入您的问题")

if prompt:
    st.session_state["message"].append({"role":"user", "content":prompt})
    for message in st.session_state["message"]:
        st.chat_message(message["role"]).markdown(message["content"])
    with st.spinner("AI思考中..."):
        res = client.chat(model="deepseek-r1:8b", messages=[{
            "role": "user",
            "content": prompt
        }])
        st.session_state["message"].append({"role": "assistant", "content": res['message']['content']})

#     渲染
        st.chat_message("assistant").markdown(res['message']['content'])
