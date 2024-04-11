import streamlit as st

def load_home_page():
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
        Build by Jaydeep Chakrabarty
        """        
    )
