import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction")

longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
age = st.slider("Housing Median Age", 1, 50, 20)
rooms = st.number_input("Total Rooms", 100, 10000, 1000)
bedrooms = st.number_input("Total Bedrooms", 50, 5000, 200)
population = st.number_input("Population", 100, 10000, 1000)
households = st.number_input("Households", 50, 5000, 300)
income = st.slider("Median Income", 0.0, 15.0, 5.0)
ocean = st.selectbox("Ocean Proximity", 
                     ["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"])


if st.button("Predict Price"):
    data = pd.DataFrame([{
        "longitude": float(longitude),
        "latitude": float(latitude),
        "housing_median_age": int(age),
        "total_rooms": float(rooms),
        "total_bedrooms": float(bedrooms),
        "population": float(population),
        "households": float(households),
        "median_income": float(income),
        "ocean_proximity": str(ocean)
    }])

    # ✅ Ensure same column order as training
    data = data[model.feature_names_in_]

    prediction = model.predict(data)[0]

    # ✅ Extra safety fix (your question)
    if not np.isfinite(prediction):
        st.error("Prediction failed. Try different values.")
    else:
        st.success(f"💰 Predicted Price: ${round(prediction, 2)}")