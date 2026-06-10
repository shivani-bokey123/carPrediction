# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:04:32 2026

@author: ASUS
"""
import streamlit as st
from catboost import CatBoostRegressor
import pandas as pd

# Page setup
st.set_page_config(page_title="Car Price Prediction", layout="wide")
st.markdown("""
    <style>
        /* Default style for all Streamlit buttons */
        div.stButton > button {
            background-color: #1c6dd0 !important;
            color: white !important;
            border-radius: 5px !important;
            font-weight: bold !important;
            border: 2px solid transparent !important;
            transition: all 0.3s ease !important;
            cursor: pointer !important;
        }

        /* Hover effect */
        div.stButton > button:hover {
            border-color: navy !important; /* navy blue border on hover */
            background-color: #1c6dd0 !important;
            color: white !important;
        }

        /* Active (clicked) effect */
        div.stButton > button:active {
            border-color: navy !important; /* navy blue border when clicked */
            background-color: #0b132b !important;
            color: white !important;
            box-shadow: 0 0 10px navy !important; /* optional glow */
        }
    </style>
""", unsafe_allow_html=True)




# Title
st.title("🚗 Car Price Prediction App")
st.markdown("Fill in the car details below and get the predicted selling price instantly!")

# Load trained model
model = CatBoostRegressor()
model.load_model("car_price_model.cbm")

df = pd.read_csv("carData.csv")

# Ensure Car_Name is treated as string
df['Car_Name'] = df['Car_Name'].astype(str)

# Unique car names for dropdown
car_names = df['Car_Name'].unique()

selected_model = st.selectbox("Select Car Model", car_names)
st.caption(f"You selected: {selected_model}")


# --- Input fields for prediction ---
col1, col2 = st.columns(2)

with col1:
  year = st.number_input("Year of Car", min_value=2000, max_value=2026, value=2015)
  kms_driven = st.number_input("Kms Driven", value=27000)
  owner = st.number_input("Number of Previous Owners", min_value=0, max_value=5, value=0)

with col2:
  present_price = st.number_input("Present Price (in lakhs)", value=5.59)
  fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
  seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
  transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# Encode categorical values
fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_map = {"Dealer": 0, "Individual": 1}
trans_map = {"Manual": 0, "Automatic": 1}

input_df = pd.DataFrame({
"Year": [year],
"Present_Price": [present_price],
"Kms_Driven": [kms_driven],
"Fuel_Type": [fuel_map[fuel_type]],
"Seller_Type": [seller_map[seller_type]],
"Transmission": [trans_map[transmission]],
"Owner": [owner]
})

# Prediction button
if st.button("🔮 Predict Price"):
  predicted_price = model.predict(input_df)
  st.markdown(
    f"""
    <div style="background-color:#1c6dd0;padding:20px;border-radius:10px;text-align:center;">
        <h3 style="color:white;">💰 Predicted Selling Price</h3>
        <h2 style="color:#FFD700;">₹ {round(predicted_price[0], 2)} Lakhs</h2>
        <p style="color:white;">Selected Model: {selected_model}</p>
    </div>
    """,
    unsafe_allow_html=True
)
