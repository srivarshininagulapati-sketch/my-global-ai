import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Srivarshini's AI", page_icon="🌟")
st.title("🌟 Srivarshini's World-Class AI")

with st.sidebar:
    user_api_key = st.text_input("Gemini API Key ikkada pettu:", type="password")

if user_api_key:
    # Stable version setup
    genai.configure(api_key=user_api_key, transport='rest') # transport='rest' adds stability
model = genai.GenerativeModel("models/gemini-1.5-flash") # Add 'models/' prefix

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Adagandi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            # Stable generation call
            response = model.generate_content(prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error vachindi: {e}")
else:
    st.info("Please enter your API Key in the sidebar to start!")




