import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Srivarshini's AI", page_icon="🌟")
st.title("🌟 Srivarshini's World-Class AI")

with st.sidebar:
    user_api_key = st.text_input("Gemini API Key ikkada pettu:", type="password")

if user_api_key:
    try:
        genai.configure(api_key=user_api_key)
        # Directly using the model name without prefix if models/ failed
        model = genai.GenerativeModel("gemini-1.5-flash")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Adagandi..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # API Call with error handling
            response = model.generate_content(prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
    except Exception as e:
        st.error(f"Oka chinna error vachindi: {e}")
        st.info("Tip: Google AI Studio lo kotha API key create chesi chudandi.")
else:
    st.info("Please enter your API Key in the sidebar to start!")



