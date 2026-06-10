import requests
import json
import streamlit as st

# Check if exchange rates are cached in session state; if not, initialize them using INR
# This initial fetch is done to get a list of all available currency codes for the dropdown menus
if "exchange_rates" not in st.session_state:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/INR")
    st.session_state.exchange_rates = json.loads(response.text)

# Render the application title
st.title("Currency Converter")

# Input field for the amount to be converted (minimum value set to 0)
amount = st.number_input("Enter the amount:", min_value=0)

# Dropdown selection for the source and target currencies
convert_from = st.selectbox("Select the currency to convert from:", list(st.session_state.exchange_rates["rates"].keys()))
convert_to = st.selectbox("Select the currency to convert to:", list(st.session_state.exchange_rates["rates"].keys()))
    
# Fetch latest exchange rates for the chosen base currency (convert_from)
response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{convert_from}")
st.session_state.exchange_rates = json.loads(response.text)

# Extract the conversion rate for the target currency (convert_to)
multiplier = st.session_state.exchange_rates["rates"][convert_to]

# Calculate the converted currency amount
answer = amount * multiplier

# Display the conversion result to the user, formatted to 2 decimal places
st.success(f"{amount:.2f} {convert_from} == {answer:.2f} {convert_to}")
