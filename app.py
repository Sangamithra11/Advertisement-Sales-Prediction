import streamlit as st
import numpy as np
import joblib

model=joblib.load('advertisement_model.pkl')

st.title("Advertisement Sales Prediction")

TV=st.number_input("TV Advertisement Cost",0.0,300.0,230.1)
Radio=st.number_input("Radio Advertisement Cost",0.0,50.0,37.8)
Newspaper=st.number_input("New Paper Advertisement Cost",0.0,120.0,69.2)

input_data=np.array([[TV,Radio,Newspaper]])
if st.button("Predict Sales"):
    prediction=model.predict(input_data)
    st.success(f"The predicted sales is {prediction[0]:.2f}")