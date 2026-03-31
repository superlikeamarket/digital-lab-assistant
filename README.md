# Digital Lab Assistant

A command-line tool built in Python to assist with common microbiology lab tasks such as dilution calculations, media preparation, CFU estimation, and protocol timing.

---

## Overview

This project is designed to streamline repetitive laboratory calculations and workflows in a simple terminal-based interface. It focuses on clarity, correctness, and usability.

The tool is modular and built with scalability in mind, allowing future expansion into a GUI or hardware-integrated system.

---

## Features

* **Dilution Calculator**

  * Uses the formula ( C_1 V_1 = C_2 V_2 )
  * Calculates required stock and diluent volumes

* **Media Preparation Calculator**

  * Computes required mass from concentration (g/L)
  * Supports input in mL and L

* **CFU Estimator**

  * Calculates CFU/mL from colony count
  * Accepts dilution formats:

    * decimal (0.0001)
    * exponent (-4)
    * power notation (10^-4)

* **Protocol Timer**

  * Countdown timer with hours, minutes, seconds
  * Terminal-based alerts

* **Structured CLI Interface**

  * Built with `rich` for clean and readable output

---

## Installation

Clone the repository:

```bash
git clone https://github.com/superlikeamarket/digital-lab-assistant.git
cd digital-lab-assistant
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the application:

```bash
python main.py
```

---

## Example Usage

### Dilution Calculator

```text
Stock concentration: 100 mg/mL
Target concentration: 10 mg/mL
Final volume: 50 mL

Result:
Stock volume: 5.00 mL
Diluent volume: 45.00 mL
```

---

### CFU Estimator

```text
Colonies: 132
Plated volume: 0.1 mL
Dilution: 10^-4

Result:
CFU per mL: 1.32e+07
```

---

### Media Preparation

```text
Concentration: 40 g/L
Volume: 500 mL

Result:
Mass needed: 20.00 g
```

---

## Running Tests

Run all tests using:

```bash
pytest
```

---

## Project Structure

```text
digital-lab-assistant/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── lab_assistant/
│   ├── dilution.py
│   ├── media_prep.py
│   ├── cfu.py
│   ├── timer.py
│   ├── menu.py
│   └── utils.py
│
└── tests/
    ├── test_dilution.py
    ├── test_media_prep.py
    └── test_cfu.py
```

---

## Future Improvements

* GUI version (Tkinter or Streamlit)
* Unit conversion system (µL, mg/mL, % solutions)
* Data logging and history tracking
* Multiple concurrent timers
* Voice input for hands-free use
* Integration with Raspberry Pi for lab automation

---

## Notes

* This project is intended for educational and prototyping purposes.
* Calculations should always be verified before use in critical lab settings.

---

## Author

[Your Name]

---

# How to use this

Do not overthink it:

1. Copy this into your `README.md`
2. Replace:

   * `yourusername`
   * `[Your Name]`
3. Commit it:

```bash
git add README.md
git commit -m "added README"
```

---
