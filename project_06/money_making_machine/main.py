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
        reponse=requests.get("http://127.0.0.1:8000/side_hustles?apikey=12345678")
        if reponse.status_code == 200:
            hustles=reponse.json()
            return hustles["side_hustles"]
        else:
            return ("freelancing")
    except:
        return ("Something went wrong.")
    
st.header("Side Hustles Idaes")
if st.button("Generate Hustle"):
    idea=fetch_side_hustles()
    st.success(idea)

def money_quotes():
    try:
        reponse=requests.get("http://127.0.0.1:8000/money_quotes?apikey=12345678")
        if reponse.status_code == 200:
            quotes=reponse.json()
            return quotes["Money_quotes"]
        else:
            return ("No quotes left")
    except:
        return ("Something went wrong.")

st.header("Money Quotes")
if st.button("Generate Money Quotes"):
    quotes=money_quotes()
    st.success(quotes)
    




