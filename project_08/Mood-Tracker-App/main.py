import streamlit as st  #For creating web interface
import pandas as pd     #for data manipulation
import datetime         #for handling dates
import csv              #For reading and writing CSV file
import os               #for files operations
#Define the file name for storing the mood data
MOOD_FILE="mood_log.csv"
#Function to read mood data from the CSV file 
def load_mood_data():
    # Check if the file exists
    if not os.path.exists(MOOD_FILE):
        # If no file,create a DataFrame with columns
        return pd.DataFrame(columns=["Date","Mood"])
    # Read and return Existing mood data
    return pd.read_csv(MOOD_FILE)
# Function to add or append new mood entry to Csv file
def save_mood_data(date,mood):
    # File open in to append mode
    with open(MOOD_FILE,"a",) as file:
        # create a CSV writer
        writer=csv.writer(file)
        # Add new mood entry
        writer.writerow([date,mood])
st.set_page_config(page_icon="😊",page_title="Mood-Tracker-App")
# Streamlit Title
st.title("Mood Tracker 😊")
# Get's today's date
today=datetime.date.today()
# Create a sub-header
st.subheader("How are you feeling today?")
# Create a dropdown mood selection
mood=st.selectbox("Select Your Mood",["Happy","Sad","Angry","Neutral"])
# Create a Log_Mood Button
if st.button("Log_Mood"):
    # Save Mood Data when button is clicked
    save_mood_data(today,mood)
    # Show Suceesful Message 
    st.success("Mood Logged Sucessfully!")
# Load Existing Data
data=load_mood_data()
# If data not empty then display
if not data.empty:
    # Create sub-header
    st.subheader("Mood Trends Over Time")
    # Convert datetime string to datetime Object
    data["Date"]=pd.to_datetime(data["Date"])
    # Count Frequency of each Mood
    mood_counts=data.groupby("Mood").count()["Date"]
    # Create bar chart of mood frequency
    st.bar_chart(mood_counts)

    st.write("Bulid with ❤ By [Muhammad Daniyal](https://github.com/Danii9790) ")







