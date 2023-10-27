import petName_LangchainHelper as lch
import streamlit as st

st.title("Pet Name Generator")

# Get user input]
animal_type = st.sidebar.text_input("Enter your pet type: ")  

animal_color = st.sidebar.text_input("Enter your pet color: ")


if animal_type and animal_color:
    response= lch.generate_pet_name(animal_type, animal_color)
    st.text(response['pet_name'].strip())
    

 
    #st.write("Restaurant Name according to",user_input)
   
# Generate pet name
