import streamlit as st
from src.components.welcome_sidebar import welcome_sidebar
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(
        page_title="Arkham Horror - The Card Game Companinon",
        page_icon="src/assets/cultist.png",
    )

    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", 'Settings'], 
            icons=['house', 'gear'], menu_icon="cast", default_index=1)
        selected
    
    # welcome_sidebar()
    st.image("src/assets/logo.png")
    st.markdown(
        "> # Welcome to Arkham Horizons  \n\n"
        "> Unraveling the mysteries of Arkham Horror through the prowess of _EldritchTech_ and _DeepLore Language Engines_."
    )
    st.markdown("---")
    st.markdown (
        "### Key Features\n\n"
        "- **Intuitive Natural Language Chat with Tutorial**: Lost in the enigma of Arkham Horror rules? Our advanced chat interface understands your queries in plain language, guiding both novices and experts with clarity and precision. Say goodbye to constant rulebook referencing and let EldritchTech simplify the complexities, letting you focus on the game.\n\n"

        "- **Voice Narration for Immersive Campaign Experiences**: Dive deeper into the chilling stories of Arkham with our AI-generated voice narrations. Each campaign is brought to life with rich auditory details, setting the mood and elevating your gameplay. Feel every suspense, tension, and triumph as the tales unfold audibly, immersing you into the heart of Arkham's mysteries.\n\n"
        
        "### How to Use\n\n"
        "- Navigate to the desired section – be it the chat tutorial or voice campaigns.\n"
        "- For chat assistance, simply type or speak your query in natural language.\n"
        "- For voice narrations, select your desired campaign and press play to start the auditory journey."
    )

    st.markdown("---")

    st.caption(
        """
        Crafted with innovation, "Arkham Horizons" blends generative AI capabilities with a user-centric design, ensuring a seamless and enhanced Arkham Horror gaming experience. Whether it's rule clarification or atmospheric narration, embark on an unparalleled journey through the arcane streets of Arkham with us.
        """        
    )

if __name__ == "__main__":
    main()
