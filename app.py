import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

# Define the app title
st.title("Car Price Prediction")
st.write("Use this app to predict the price of a car based on its features.")

# Input form
def get_user_input():
    company = st.text_input("Car Company", "Maruti")  # Now this is the brand
    name = st.text_input("Car Model Name", "Maruti Suzuki Swift")  # This is now for the car model name
    year = st.number_input("Year", min_value=1900, max_value=2024, value=2019)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, value=100)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])

    user_data = pd.DataFrame({
        'name': [name],  # This represents the model
        'company': [company],  # This represents the brand
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })
    return user_data

# Get user input
data = get_user_input()

# Display input data
st.subheader("User Input:")
st.write(data)

# Predict button
if st.button("Predict Price"):
    try:
        # Perform prediction
        prediction = model.predict(data)
        st.subheader("Predicted Price:")
        st.write(f"₹ {prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
