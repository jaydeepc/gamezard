import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain import OpenAI
import os
from langchain.llms import LlamaCpp

def load_chat_model(model_name):
    load_dotenv()
    openai_api_key = st.session_state.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
    temperature = 0.9
    max_tokens = 1000
    model_name = model_name

    llm = ChatOpenAI(openai_api_key=openai_api_key, model_name=model_name, temperature=temperature, max_tokens=max_tokens)
    return llm