import streamlit as st
from lab_assistant.dilution import calculate_dilution


def run():
    st.title("Dilution calculator")

    with st.form("dilution_form"):
        stock_conc = st.text_input(
            "Stock concentration",
            placeholder="e.g. 10 g/L or 10 mg/mL, default unit: g/L"
        )
        target_conc = st.text_input(
            "Target concentration",
            placeholder="e.g. 2 g/L or 2 mg/mL, default unit: g/L"
        )
        final_volume = st.text_input(
            "Final volume",
            placeholder="e.g. 0.5 L or 500 mL, default unit: L"
        )

        submitted = st.form_submit_button("Calculate dilution")

        if submitted:
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