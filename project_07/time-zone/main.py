import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

Time_Zones=[
     "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

st.title("Time Zone App")
selected_timezone=st.multiselect("Select Time Zone",Time_Zones,default=["Asia/Karachi","UTC"])
st.subheader("selected_timezone")
for tz in selected_timezone:
    current_time=datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d  %I %H:%M:%S %p")
    st.write(f"**{tz}** : {current_time}")

st.subheader("Convert Time Between Timezones")
current_time=st.time_input("Current time ",value=datetime.now().time())
from_tz =st.selectbox("From Timezones ",Time_Zones,index=0)
to_tz=st.selectbox("To Timezone ",Time_Zones,index=1)
if st.button("Convert"):
    dt=datetime.combine(datetime.today(),current_time,tzinfo=ZoneInfo(from_tz))
    converted_time=dt.astimezone(ZoneInfo(to_tz)).strftime("%Y %m %d %I %H:%M:%S %p")
    
    st.success(f"Converted time into {to_tz} : {converted_time}")

