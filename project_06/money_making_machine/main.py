import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1,1000)

st.header("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your Money...")
    time.sleep(2)
    amount=generate_money()
    st.success(f"you made ${amount}!")

def fetch_side_hustles():
    try:
        response=requests.get("https://fastapi-eosin-iota.vercel.app/side_hustles")
        if response.status_code == 200:
            data=response.json()
            return data.get("side_hustle","Side_hustles not found.")
        else:
            return ("No Side_hustles left.")
    except Exception as e:
        return f"Something went wrong: {e}"
    
st.header("Side Hustles Idaes")
if st.button("Generate Hustle"):
    idea=fetch_side_hustles()
    st.success(idea)

def money_quotes():
    try:
        response = requests.get("https://fastapi-eosin-iota.vercel.app/money_quotes")
        if response.status_code == 200:
            data = response.json()
            return data.get("money_quote", "Quote not found.")
        else:
            return f"Server returned status code: {response.status_code}"
    except Exception as e:
        return f"Something went wrong: {e}"

st.header("Money Quotes")
if st.button("Generate Money Quotes"):
    quotes=money_quotes()
    st.success(quotes)
    




