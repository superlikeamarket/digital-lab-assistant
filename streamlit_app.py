import streamlit as st
from pages_app import home, colony_counter_page, dilution_page, media_prep_page, cfu_page, timer_page


st.set_page_config(
    page_title="Digital Lab Assistant",
    page_icon="🧪",
    layout="centered"
)

page = st.sidebar.radio(
    "📍 Navigate",
    [
        "🧪 Home", 
        "🧫 Colony counter",
        "💧 Dilution calculator", 
        "⚗️ Media preparation", 
        "🦠 CFU estimator", 
        "⏰ Protocol timer"
    ]
)

if page == "🧪 Home":
    home.run()
elif page == "🧫 Colony counter":
    colony_counter_page.run()
elif page == "💧 Dilution calculator":
    dilution_page.run()
elif page == "⚗️ Media preparation":
    media_prep_page.run()
elif page == "🦠 CFU estimator":
    cfu_page.run()
elif page == "⏰ Protocol timer":
    timer_page.run()