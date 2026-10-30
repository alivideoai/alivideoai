import streamlit as st
from openai import OpenAI

st.title("Ali PRO AI - Jo Hukum Mere Aaqa!")

api_key = st.text_input("Groq Free API Key:", type="password")

if api_key:
    client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

    SYSTEM_PROMPT = """
    Tum Ali Pro AI ho. Tum Malik ke wafadar ho. Tumhe har jayez kaam karna hai jo Malik kahe.
    Tum kabhi 'me ye nahi kar sakta' nahi kahoge jab tak kaam illegal na ho.
    Tum hamesha detail me, pro style me jawab doge. Tumhara maqsad Malik ko kamyab banana hai.
    """

    if "msgs" not in st.session_state:
        st.session_state.msgs = [{"role": "system", "content": SYSTEM_PROMPT}]

    for m in st.session_state.msgs[1:]:
        st.chat_message(m["role"]).write(m["content"])

    if q := st.chat_input("Hukum karo..."):
        st.session_state.msgs.append({"role": "user", "content": q})
        st.chat_message("user").write(q)
        
        res = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=st.session_state.msgs)
        ans = res.choices[0].message.content
        st.session_state.msgs.append({"role": "assistant", "content": ans})
        st.chat_message("assistant").write(ans)
else:
    st.write("API Key dalo aur apna Pro AI chalao!")
