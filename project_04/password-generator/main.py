import streamlit as st
import random 
import string

def generate_password(length,use_digit,use_special_char):
    characters=string.ascii_letters
    if use_digit:
        characters +=string.digits
    if use_special_char:
        characters += string.punctuation
    return ''.join(random.choice(characters)for _ in range(length))
st.set_page_config(page_title="Password generator",page_icon="😉")
st.title("Password Generator 😉")
lenth=st.slider("Password Length ",min_value=6,max_value=32,value=12)
use_digit=st.checkbox("Include Digits")
use_special_char=st.checkbox("Include Special Characters")

if st.button("Generate"):
    password=generate_password(lenth,use_digit,use_special_char)
    st.write(f"Generate password : {password}")
    
st.write("----------------------------------")
st.write("Made with ❤ by [Muhammad Daniyal](https://github.com/Danii9790)")
