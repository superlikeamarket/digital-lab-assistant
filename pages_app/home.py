import streamlit as st


def run():
    st.title("Digital Lab Assistant")
    st.write("A simple lab utility app for dilution, media prep, and CFU calculations.")

    st.subheader("Available tools")
    st.markdown(
        """
        - **Dilution calculator**
        - **Media preparation calculator**
        - **CFU estimator**
        - **Protocol timer** *(coming soon as a separate page)*
        """
    )

    with st.expander("About this app", expanded=True):
        st.markdown(
            """
            **Digital Lab Assistant** is a small web app for common microbiology and lab-prep calculations.

            It is intended for:
            - students learning laboratory methods
            - interns in microbiology or quality-control labs
            - laboratory staff who want quick calculation support

            The app currently provides:
            - dilution calculations using **C1V1 = C2V2**
            - media preparation calculations using **mass = concentration × volume**
            - CFU estimation using **CFU/mL = colonies / (plated volume × dilution)**
            - a simple protocol timer

            This app is meant for **educational and workflow support**.
            It does **not** replace laboratory SOPs, supervisor instructions, validation procedures, or official QC documentation.

            Always verify calculations before using them in real lab work.
            """
        )