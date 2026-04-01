import streamlit as st
from lab_assistant.cfu import calculate_cfu


def run():
    st.title("CFU estimator")

    colonies = st.number_input("Number of colonies", min_value=1, step=1)
    plated_volume = st.text_input(
        "Plated volume",
        placeholder="e.g. 0.1 mL or 100 uL, default unit: mL"
    )
    dilution = st.text_input(
        "Dilution",
        placeholder="e.g. 0.0001, -4, or 10^-4"
    )

    if st.button("Calculate CFU"):
        try:
            cfu_ml = calculate_cfu(int(colonies), plated_volume, dilution)
            st.success("Calculation complete")
            st.write(f"**CFU per mL:** {cfu_ml:.2e}")

            if colonies < 30:
                st.warning("Fewer than 30 colonies may be unreliable.")
            elif colonies > 300:
                st.warning("More than 300 colonies may be overcrowded.")

        except ValueError as e:
            st.error(str(e))