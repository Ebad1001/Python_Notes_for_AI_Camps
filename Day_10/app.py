import requests
import json
import streamlit as st

if "exchange_rates" not in st.session_state:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/INR")
    st.session_state.exchange_rates = json.loads(response.text)

st.title("Currency Converter")
amount = st.number_input("Enter the amount:", min_value=0)
convert_from = st.selectbox("Select the currency to convert from:", list(st.session_state.exchange_rates["rates"].keys()))
convert_to = st.selectbox("Select the currency to convert to:", list(st.session_state.exchange_rates["rates"].keys()))
    
response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{convert_from}")
st.session_state.exchange_rates = json.loads(response.text)
multiplier = st.session_state.exchange_rates["rates"][convert_to]
answer = amount * multiplier
st.success(f"{amount:.2f} {convert_from} == {answer:.2f} {convert_to}")
