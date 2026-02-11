import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Srivarshini's AI", page_icon="🌟")
st.title("🌟 Srivarshini's AI")

# Secrets check
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        
        # Ikkada 'gemini-1.5-flash-latest' ani marchamu
        # Idhi kachithanga v1beta error ni fix chesthundhi
        model = genai.GenerativeModel("gemini-1.5-flash-latest")

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
        st.error(f"Error logic check: {e}")
else:
    st.warning("Dashboard Secrets lo 'GEMINI_API_KEY' petti save cheyandi.")
