import streamlit as st
import pandas as pd
import pickle

def load_model():
    try:
        with open('App.py/random_forest_model.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None
    
def load_encoder():
    try:
        with open('App.py/encoder.pkl', 'rb') as file:
            encoder = pickle.load(file)
        return encoder
    except Exception as e:
        st.error(f"Error loading encoder: {e}")
        return None

# Load your dataset
df = pd.read_csv('App.py/database.csv')

def pred_page():
    with st.expander("My DataFrame"):
        st.dataframe(df)
    
    with st.sidebar:
        st.subheader('Input Features') 
        
        # Input fields
        latitude = st.slider("Latitude", min_value=df["Latitude"].min(), max_value=df["Latitude"].max(), value=df["Latitude"].mean())
        longitude = st.slider("Longitude", min_value=df["Longitude"].min(), max_value=df["Longitude"].max(), value=df["Longitude"].mean())
        Type = st.selectbox('Select Disaster Type', options=df['Type'].unique().tolist())
        Depth = st.slider('Depth', min_value=int(df['Depth'].min()), max_value=int(df['Depth'].max()), value=int(df['Depth'].mean()))
        Magnitude = st.slider('Magnitude', min_value=float(df['Magnitude'].min()), max_value=float(df['Magnitude'].max()), value=float(df['Magnitude'].mean()))
        Magnitude_Type = st.selectbox('Select Magnitude Type', options=df['Magnitude Type'].unique().tolist())
        Root_Mean_Square = st.slider('Root Mean Square', min_value=int(df['Root Mean Square'].min()), max_value=int(df['Root Mean Square'].max()), value=int(df['Root Mean Square'].mean()))
        Source = st.selectbox('Select Source', options=df['Source'].unique().tolist())
        
        # Prepare input data
        input_data = pd.DataFrame({
            "Latitude": [latitude],
            "Longitude": [longitude],
            "Type": [Type],
            "Depth": [Depth],
            "Magnitude": [Magnitude],
            "Magnitude Type": [Magnitude_Type],
            "Root Mean Square": [Root_Mean_Square],
            "Source": [Source]
        })
        
        encoder = load_encoder()
        if encoder is None:
            return  # Early exit if encoder couldn't be loaded
        
        # Encode the categorical features
        encoded_features = encoder.transform(input_data[['Type', 'Magnitude Type', 'Source']])
        encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(['Type', 'Magnitude Type', 'Source']))
        
        # Combine encoded features with the original input data
        input_data = pd.concat([input_data.drop(['Type', 'Magnitude Type', 'Source'], axis=1), encoded_df], axis=1)
        st.dataframe(input_data)

        model = load_model()
        if model is not None and st.button("Predict"):
            try:
                prediction = model.predict(input_data)
                if prediction.ndim > 1:
                    st.success(f'Prediction: {prediction.argmax()}')
                else:
                    st.success(f'Prediction: {prediction[0]}')
            except Exception as e:
                st.error(f"Error making prediction: {e}")

# Call the prediction page function