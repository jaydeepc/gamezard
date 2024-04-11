import streamlit as st

def welcome_sidebar():
    with st.sidebar:
        st.image("src/assets/logo.png")
        st.markdown(
            """
            Dive deep into the cryptic world of Arkham Horror with 
            "Arkham Horizons." Whether you're a novice investigator baffled by 
            intricate rules or a seasoned player yearning for atmospheric 
            voiceovers to enhance your campaign experiences, we've got you covered. 
            Let our intuitive chat interface guide you through the maze of gameplay 
            queries in natural language, ensuring that you spend less time flipping 
            through rulebooks and more time uncovering the secrets of the cosmos.
            Plus, immerse yourself in our AI-generated voice narrations, bringing each 
            campaign to life in rich auditory detail. 

            Welcome to "Arkham Horizons" - where mysteries unfold, and answers await
            """
        )
        st.markdown("---")