import streamlit as st
from google import genai

# Website Title
st.set_page_config(page_title="Srivarshini's AI", page_icon="🌟")
st.title("🌟 Srivarshini's World-Class AI")

# Sidebar for Key
with st.sidebar:
    user_api_key = st.text_input("Gemini API Key ikkada pettu:", type="password")

if user_api_key:
    # Gemini 2.0 connection
    client = genai.Client(api_key=user_api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Adagandi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Gemini 2.0 Generation
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.info("Please enter your API Key in the sidebar to start!")



