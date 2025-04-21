import streamlit as st
def unit_convertors(value:float,unit_from:str, unit_to:str):
    
    # 1kilometer = 1000 meters
    # 1meter = 0.001 kilometers
    #  1kilogram = 1000gram
    # 1 gram = 0.001 kilogram
    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
        return value * 0.001
    elif unit_from == "kilogram" and unit_to == "gram":
        return value * 1000
    elif unit_from == "gram" and unit_to == "kilogram":
        return value * 0.001
    else :
        return "conversion is not supported"


def main():
    st.title("Unit convertor")
    st.write("Welcome to unit convertor")
    value = st.number_input("enter the value you want to convertor:",min_value=0.0)
    unit_from = st.text_input("enter the value you want to convertor from(e.g meters kilometers gram kilogram)")
    unit_to =    st.text_input("enter the value you want to convertor to(e.g meters kilometers gram kilogram)")
    if st.button("Convert"):
      result = unit_convertors(value,unit_from,unit_to)
      st.write(result)

main()