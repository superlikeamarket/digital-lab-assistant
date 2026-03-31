import streamlit as st

from lab_assistant.dilution import calculate_dilution
from lab_assistant.media_prep import calculate_mass_from_concentration
from lab_assistant.cfu import calculate_cfu

st.set_page_config(page_title="Digital Lab Assistant", page_icon="🧪", layout="centered")

st.title("Digital Lab Assistant")
st.write("A simple lab utility app for dilution, media prep, and CFU calculations.")

tool = st.sidebar.radio(
    "Choose a tool",
    ["Dilution calculator", "Media preparation", "CFU estimator"]
)

if tool == "Dilution calculator":
    st.header("Dilution calculator")

    stock_conc = st.text_input("Stock concentration", placeholder="e.g. 10 g/L or 10 mg/mL")
    target_conc = st.text_input("Target concentration", placeholder="e.g. 2 g/L or 2 mg/mL")
    final_volume = st.text_input("Final volume", placeholder="e.g. 0.5 L or 500 mL")

    if st.button("Calculate dilution"):
        try:
            stock_volume_l, diluent_volume_l = calculate_dilution(
                stock_conc, target_conc, final_volume
            )

            stock_volume_ml = stock_volume_l * 1000
            diluent_volume_ml = diluent_volume_l * 1000

            st.success("Calculation complete")
            st.write(f"**Stock volume:** {stock_volume_ml:.2f} mL")
            st.write(f"**Diluent volume:** {diluent_volume_ml:.2f} mL")

        except ValueError as e:
            st.error(str(e))

elif tool == "Media preparation":
    st.header("Media preparation calculator")

    concentration = st.text_input("Desired concentration", placeholder="e.g. 40 g/L")
    volume = st.text_input("Desired volume", placeholder="e.g. 500 mL or 0.5 L")

    if st.button("Calculate mass"):
        try:
            mass = calculate_mass_from_concentration(concentration, volume)
            st.success("Calculation complete")
            st.write(f"**Mass needed:** {mass:.2f} g")
        except ValueError as e:
            st.error(str(e))

elif tool == "CFU estimator":
    st.header("CFU estimator")

    colonies = st.number_input("Number of colonies", min_value=1, step=1)
    plated_volume = st.text_input("Plated volume", placeholder="e.g. 0.1 mL or 100 uL")
    dilution = st.text_input("Dilution", placeholder="e.g. 0.0001, -4, or 10^-4")

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