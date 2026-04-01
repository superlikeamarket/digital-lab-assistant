import streamlit as st
from lab_assistant.media_prep import calculate_mass_from_concentration


def run():
    st.title("Media preparation calculator")

    concentration = st.text_input(
        "Desired concentration",
        placeholder="e.g. 40 g/L, default unit: g/L"
    )
    volume = st.text_input(
        "Desired volume",
        placeholder="e.g. 500 mL or 0.5 L, default unit: L"
    )

    if st.button("Calculate mass"):
        try:
            mass = calculate_mass_from_concentration(concentration, volume)
            st.success("Calculation complete")
            st.write(f"**Mass needed:** {mass:.2f} g")
        except ValueError as e:
            st.error(str(e))