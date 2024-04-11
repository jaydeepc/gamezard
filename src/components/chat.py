import streamlit as st
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import LLMChain
from langchain.chains import RetrievalQA
from src.modules.models import load_chat_model
from src.prompt.engine import summary_prompt, question_answer_prompt

model_name = "gpt-4"

def initialise():
    if "is_placeholder" not in st.session_state:
        st.session_state.is_placeholder = True    

    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if 'summary_memory' not in st.session_state:
        st.session_state['summary_memory'] = None

    if "qa_chain" not in st.session_state:
        search_index = st.session_state['knowledge_base']
        llm = load_model()
        QA_PROMPT = question_answer_prompt()
        load_qa = load_qa_chain(llm=llm, chain_type="stuff", prompt=QA_PROMPT, verbose=True)
        qa_chain = RetrievalQA(combine_documents_chain=load_qa, retriever=search_index.as_retriever(), return_source_documents=True, verbose=True)  
        st.session_state.qa_chain = qa_chain

    if "summary_chain" not in st.session_state:
        SUMMARY_PROMPT = summary_prompt()
        llm = load_chat_model(model_name)
        summary_chain = LLMChain.from_string(llm=llm, template=SUMMARY_PROMPT)
        st.session_state.summary_chain = summary_chain

def set_placeholder_false():
    st.session_state.is_placeholder = False

def load_model():
    print ("**************" + model_name + "**************")
    llm = load_chat_model(model_name)
    return llm

def display_source(document):
    metadata_list = [{**doc[0].metadata, "score":doc[1]} for doc in document]
    
    with st.expander("Source Documents"):
        col1, col2, col3, col4 = st.columns(4)
        col1.markdown("**Page: " + str(metadata_list[0]["page"]) + "** *" + metadata_list[0]["file"] + "*" + " Score: " + str(metadata_list[0]["score"]))
        col2.markdown("**Page: " + str(metadata_list[1]["page"]) + "** *" + metadata_list[1]["file"] + "*" + " Score: " + str(metadata_list[1]["score"]))
        col3.markdown("**Page: " + str(metadata_list[2]["page"]) + "** *" + metadata_list[2]["file"] + "*" + " Score: " + str(metadata_list[2]["score"]))
        col4.markdown("**Page: " + str(metadata_list[3]["page"]) + "** *" + metadata_list[3]["file"] + "*" + " Score: " + str(metadata_list[3]["score"]))

def display_chat():
    initialise()

    if st.session_state.messages == [] and st.session_state.is_placeholder:
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
             st.image("src/assets/ghoul_priest.png", use_column_width="auto")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if message["role"] == "assistant":
                    if message["source"] is not None:
                        display_source(message["source"])

    if prompt := st.chat_input("Enter you question...", on_submit=set_placeholder_false):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        response, source = generate_response(prompt)

        with st.chat_message("assistant"):
            st.markdown(response)
            display_source(source)
        st.session_state.messages.append({"role": "assistant", "content": response, "source": source})


def generate_response(message):
    query = message
    # if st.session_state['memory']:
    #     query = "\nConversation Summary: " + st.session_state['summary_memory']  + "\nQuestion: " + message 

    source_document = st.session_state['knowledge_base'].similarity_search_with_score(query)
    ai_response = st.session_state.qa_chain(query)

    # if st.session_state['memory']:
    #     summary = "\nConversation Summary: " + st.session_state['summary_memory']  + "\nUser: " + message + "\nAI: " + ai_response['result']
    #     st.session_state['summary_memory'] = st.session_state.summary_chain.predict(input=summary)

    return ai_response['result'], source_document
