import streamlit as st
from src.utils.uploader import load_pdf
from src.components.chat import display_chat
from src.components.sidebar import sidebar

def initialise():
    if 'knowledge_base' not in st.session_state:
        st.session_state['knowledge_base'] = None
    
    st.image("src/assets/logo.png")

def chat_page():
    initialise()
    st.header('Chat with Tutorial')

    st.session_state['knowledge_base'] = load_pdf()

    if st.session_state['knowledge_base'] is not None:
        display_chat()


