import streamlit as st
import google.generativeai as genai

# Page settings
st.set_page_config(page_title="Srivarshini's AI", page_icon="🌟")
st.title("🌟 Srivarshini's World-Class AI")

# Sidebar for API Key
with st.sidebar:
    st.write("### Settings")
    user_api_key = st.text_input("Gemini API Key ikkada pettu:", type="password")
    st.info("API Key lekapothe [Google AI Studio](https://aistudio.google.com/) ki velli kothadhi create cheyandi.")

if user_api_key:
    try:
        # Configuration
        genai.configure(api_key=user_api_key)
        
        # Universal Stable Model
       model = genai.GenerativeModel("gemini-1.5-flash")

        # Chat history setup
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display old messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if prompt := st.chat_input("Adagandi..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate response
            response = model.generate_content(prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
    except Exception as e:
        # Clear error message
        st.error(f"Error vachindi: {e}")
        st.warning("Pai error 'API_KEY_INVALID' ani unte, kotha key create cheyandi.")
else:
    st.info("AI matladalante sidebar lo API Key pettandi.")

