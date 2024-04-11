import streamlit as st

def load_audio_page():
    st.image("src/assets/logo.png")
    st.header('Experience the campaigns', divider='rainbow')
    selected = st.selectbox("Select a campaign", ["Select", "The Night of the Zealot"])
   
    if selected == "The Night of the Zealot":
        col1, col2, col3 = st.columns([4, 2, 4])
        with col1:
            st.text("The Ghouls Hunger . . .")
        with col3:
            st.image("src/assets/nightofthezealot.png", use_column_width="auto")
            st.audio("src/assets/audio/TheGhoulsHunger.mp3")    
        scenario = st.selectbox("Select a scenario", ["Choose", "The Gathering", "The Midnight Masks", "The Devourer Below"])
        if scenario == "The Gathering":
            col1, col2, col3 = st.columns([4, 2, 4])
            with col1:
                st.text("Part 1 - The Campaign Log")
            
                
            with col3:
                st.image("src/assets/thegathering.jpeg", use_column_width="auto")
                st.audio("src/assets/audio/part1gathering.mp3")