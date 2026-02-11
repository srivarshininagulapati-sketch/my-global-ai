import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Srivarshini's AI", page_icon="🌟")
st.title("🌟 Srivarshini's World-Class AI")

# Secrets nunchi key ni teesukuntundhi
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        
        # 'models/' prefix ni motham teeyasamu
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
else:
    st.warning("Secrets lo 'GEMINI_API_KEY' ledhu. Dashboard ki velli add cheyandi.")
