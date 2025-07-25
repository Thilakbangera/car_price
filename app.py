import streamlit as st
import pandas as pd
import pickle
import os

# Load the trained model safely
if not os.path.exists("LinearRegressionModel.pkl"):
    st.error("❌ Model file 'LinearRegressionModel.pkl' not found.")
    st.stop()

try:
    with open('LinearRegressionModel.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

# Load the dataset
data_file = 'Cleaned_car.csv'
if not os.path.exists(data_file):
    st.error("❌ Dataset 'Cleaned_car.csv' not found.")
    st.stop()

car_data = pd.read_csv(data_file)

# Group car models by company
company_to_models = car_data.groupby('company')['name'].unique().to_dict()

# App title
st.title("🚗 Car Price Prediction")
st.write("Use this app to predict the price of a car based on its features.")

# Initialize session state for prediction history
if 'predictions' not in st.session_state:
    st.session_state['predictions'] = []

# Input form
def get_user_input():
    company = st.selectbox("Select Car Company", ["--Select--"] + list(company_to_models.keys()))

    if company != "--Select--":
        models = company_to_models.get(company, [])
        model_name = st.selectbox("Select Car Model", ["--Select--"] + list(models))
    else:
        model_name = ""

    year = st.number_input("Year", min_value=1900, max_value=2024, value=2019)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, value=100)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])

    user_data = pd.DataFrame({
        'name': [model_name],
        'company': [company],
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })
    return user_data

# Get input
data = get_user_input()

# Display user input
if data['company'][0] and data['name'][0] != "--Select--":
    st.subheader("User Input:")
    st.write(data)

# Predict button
if st.button("Predict Price"):
    try:
        prediction = model.predict(data)
        predicted_price = f"\u20B9 {prediction[0]:,.2f}"

        st.session_state['predictions'].append({
            'Company': data['company'][0],
            'Model': data['name'][0],
            'Year': data['year'][0],
            'Kilometers Driven': data['kms_driven'][0],
            'Fuel Type': data['fuel_type'][0],
            'Predicted Price': predicted_price
        })

        st.subheader("Predicted Price:")
        st.write(predicted_price)
    except Exception as e:
        st.error(f"❌ Prediction Error: {e}")

# Show prediction history
if st.session_state['predictions']:
    st.subheader("📊 Previous Predictions:")
    st.write(pd.DataFrame(st.session_state['predictions']))
    
