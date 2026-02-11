import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Srivarshini's AI", page_icon="🌟")
st.title("🌟 Srivarshini's World-Class AI")

# Secrets check
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        
        # ఇక్కడ మోడల్ పేరును అత్యంత సరళంగా "gemini-1.5-flash" అని ఇస్తున్నాం
        # ఇది v1beta సమస్యను సాధ్యమైనంత వరకు తగ్గిస్తుంది
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

            # మోడల్ నుండి సమాధానం
            response = model.generate_content(prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
    except Exception as e:
        # Error వస్తే అది ఏంటో స్పష్టంగా చూపిస్తుంది
        st.error(f"System Message: {e}")
else:
    st.warning("Dashboard Secrets lo 'GEMINI_API_KEY' petti save cheyandi.")


