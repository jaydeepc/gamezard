import streamlit as st
import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import PyPDF2
import tiktoken

tiktoken.encoding_for_model('gpt-4')
tokenizer = tiktoken.get_encoding('cl100k_base')

# create the length function
def tiktoken_len(text):
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)

def load_pdf():
    load_dotenv()

    pdfs = [f for f in os.listdir("reference_pdfs") if f.endswith(".pdf")]
    uploaded_files = []
    for pdf in pdfs:
        with open(os.path.join("reference_pdfs", pdf), "rb") as f:
            uploaded_files.append(f)

    if uploaded_files:
        text = []
        metadatas = []
        for file in uploaded_files:
            with open(file.name, "rb") as f:
                pdf_reader = PyPDF2.PdfReader(f)
                page_number = 1
                for page in pdf_reader.pages:
                    text.append(page.extract_text())
                    metadatas.append({ "page": page_number, "file": file.name })
                    page_number += 1
            
                text_splitter = RecursiveCharacterTextSplitter(
                        chunk_size=2000,
                        chunk_overlap=20,
                        length_function=tiktoken_len,
                        separators=["\n\n", "\n", " ", ""]
                    )
                
        chunks = text_splitter.create_documents(text, metadatas=metadatas)
        openai_api_key = st.session_state.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

        return FAISS.from_documents(chunks, embeddings)