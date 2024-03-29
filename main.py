import os
import streamlit as st
import google.generativeai as gen_ai

# GOOGLE_API_KEY="AIzaSyDj6ZsZUr9TZHUmAR2YXGIPIEspiw2AeYA"

st.set_page_config(
    page_title="Chat with Niranjan",
    page_icon=":brain:",
    layout="centered"
)

gen_ai.configure(api_key="AIzaSyDj6ZsZUr9TZHUmAR2YXGIPIEspiw2AeYA")
model=gen_ai.GenerativeModel('gemini-pro')

def translate_role_for_streamlit(user_role):
    if user_role=='model':
        return "assistant"
    else:
        return user_role
    
if 'chat_session' not in st.session_state:
    st.session_state.chat_session=model.start_chat(history=[])

st.title("Niranjan - ChatBot")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
        
user_prompt=st.chat_input("Ask Niranjan")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    gemini_response=st.session_state.chat_session.send_message(user_prompt)
    
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
