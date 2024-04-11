import streamlit as st
from src.components.welcome_sidebar import welcome_sidebar
from streamlit_option_menu import option_menu
from src.components.ReferenceChat import chat_page
from src.components.home_page import load_home_page
from src.components.campaign_audios_page import load_audio_page
import time

def main():    
    st.set_page_config(
        page_title="Arkham Horror - The Card Game Companinon",
        page_icon="src/assets/cultist.png",
    )

    selected = option_menu(None, ["Home", "Tutorial Chat", "Campaign Audio"], 
        icons=['house', 'chat-quote-fill', "volume-up-fill"], 
        menu_icon="cast", default_index=0, orientation="horizontal")
    
    if selected == "Home":
        load_home_page()
    elif selected == "Tutorial Chat":
        with st.spinner('Wait for it...'):
            chat_page()
        
    elif selected == "Campaign Audio":
        load_audio_page()

if __name__ == "__main__":
    main()
