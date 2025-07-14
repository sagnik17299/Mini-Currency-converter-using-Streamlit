import streamlit as st
import requests

def catalogue(base_currency):
    return f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

st.title("Currency Converter")
st.markdown("Subject to the fluctuations of global market :dollar:")
options = ["INR", "JPY", "EUR", "RUB", "GBP", "USD"]
base_currency = st.selectbox("Converting from:", options)
target = st.selectbox("Converting to:", options)
amount = st.number_input("Enter the amount:", min_value=1)

if st.button("Convert :cat:"):
    url = catalogue(base_currency)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target]
        conv_amt = rate * amount
        st.success(f"Converted amount is {conv_amt:.2f} {target}")
    else:
        st.error("There was an error converting it")
