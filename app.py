import streamlit as st
import google.generativeai as genai

# Page settings
st.set_page_config(page_title="Srivarshini's AI", page_icon="🌟")
st.title("🌟 Srivarshini's World-Class AI")

# Secrets nunchi API Key teesukovadam
try:
    # Ee line Secrets lo nuvvu pettina GEMINI_API_KEY ni vethukuthundi
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Model name ni "models/" lekunda chala simple ga petta
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

        response = model.generate_content(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

except Exception as e:
    st.error(f"Error: {e}")
    st.info("Oka vela 'KeyError' vasthe, Streamlit Dashboard Secrets lo 'GEMINI_API_KEY' petti save cheyandi.")


