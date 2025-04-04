import streamlit as st

def convert_units(value,unit_from,unit_to):
    conversions={
        "meter_kilometer" : 0.001, # 1 meter =0.001 kilometer
        "kilometer_meter" : 1000, # 1 kilometer = 1000 meter
        "grams_kilograms" :0.001, # 1 grams = 0.001 kilograms
        "kilograms_grams" :1000  # 1 kilograms = 1000 grams
    }
    key=(f"{unit_from}_{unit_to}")
    if key in conversions:
        conversion=conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"
    
st.set_page_config(page_title="unit-converter" ,page_icon="💡")
st.title("Unit Converter ↔")
value=st.number_input("Enter a Value : ",min_value=0)
unit_from=st.selectbox("Convert from : ",["meter","kilometer","grams","kilograms"])
unit_to=st.selectbox("Convert to :" ,["meter","kilometer","grams","kilograms"])
if st.button("Convert"):
    result=convert_units(value,unit_from,unit_to)
    st.write(f"Converted value : {result}")


