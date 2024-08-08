import streamlit as st
import pickle
import sklearn
import numpy as np

pipe = pickle.load(open('Titanic.pkl','rb'))

def Predictions(sex,ticket,fare,age):
    inputs = np.array([sex, ticket, fare,age],dtype=object).reshape(1,4)
    return pipe.predict(inputs)

def highlight_text(text):
    return f"<span style='color:red'>{text}</span>"




st.title("Welcome to Titanic Survival Prediction")

st.header("Welcome to Titanic Survival Prediction")

sex = st.radio("Select your gender",['male','female'])

if sex == "female":
    sex = 0
else:
    sex = 1    

Ticket = st.text_input("Enter your Ticket Number from (2.0) to (844240.875)")

Age = st.number_input("Enter your age from (0.17) to (62.8)",min_value=1, max_value=62)

fare = st.number_input("Enter your Fare (0.0) to (66.8)",min_value=0, max_value=66)

button =  st.button("Predict", type="primary")
if button:  
    missing_fields = []
    
    if not Ticket:
        missing_fields.append("Ticket")
        
    if not fare:
        missing_fields.append("Fare")
    
    if not Age:
        missing_fields.append("Age")

    if missing_fields:
        st.markdown(f"**Please fill out the required fields:** {', '.join(missing_fields)}")
        
        if not Ticket:
            st.markdown(highlight_text("Name field is required!"), unsafe_allow_html=True)
        if not fare:
            st.markdown(highlight_text("Age field is required!"), unsafe_allow_html=True)
        if not Age:
            st.markdown(highlight_text("Name field is required!"), unsafe_allow_html=True)   
    else:
        result = Predictions(sex,Ticket,Age,fare)
        if result == 0:
            st.success("You will not be survied")
        else:
            st.success("You will survied")
