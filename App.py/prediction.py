import streamlit as st
import pandas as pd
import pickle
import datetime


def load_model():
    with open('model.pkl', 'rb') as file:  # Use 'rb' to read the model
        model = pickle.load(file)
    return model

# Load your dataset
df = pd.read_csv('database.csv')

def pred_page():
    with st.expander("My DataFrame"):
        st.dataframe(df)
    
    with st.sidebar:
        st.subheader('Input Features') 
        
        selected_date = st.date_input("Select a date", datetime.date.today())

        selected_time = st.time_input("Select a time", datetime.time(12, 0))

        selected_datetime = datetime.datetime.combine(selected_date, selected_time)

        # Extract year, month, and day
        year = selected_datetime.year
        month = selected_datetime.month
        day = selected_datetime.day
        
        # Input fields for longitude and latitude
        longitude = st.number_input('Enter Longitude', value=0.0)
        latitude = st.number_input('Enter Latitude', value=0.0)

        Type = st.selectbox('Enter the Disaster Type', options=['Earthquake', 'Nuclear Explosion', 'Explosion', 'Rock Burst'])
        Depth = st.slider('Depth', min_value=int(df['Depth'].min()), max_value=int(df['Depth'].max()), value=int(df['Depth'].mean()))
        Magnitude = st.slider('Magnitude', min_value=float(df['Magnitude'].min()), max_value=float(df['Magnitude'].max()), value=float(df['Magnitude'].mean()))

        input_data = pd.DataFrame({
            "Longitude": [longitude],
            "Latitude": [latitude],
            "Disaster Type": [Type],
            "Depth": [Depth],
            "Magnitude": [Magnitude],
            "Year": [year],
            "Month": [month],
            "Day": [day]
        })
        
        # Load the model
        model = load_model()

        # Example of making a prediction (you need to adapt this to your model)
        if st.button("Predict"):
            prediction = model.predict(input_data)  # Make sure your model has a predict method
            st.success(f'Prediction: {prediction}')

pred_page()
