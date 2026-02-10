import streamlit as st
import pickle
import numpy as np
import datetime

# ================= LOAD TRAINED MODEL =================
with open("car_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

# ================= TITLE =================
st.title("🚗 Car Price Prediction App")
st.write("Predict the **selling price of a used car** based on basic details")

st.markdown("---")

# ================= USER INPUTS =================
car_name = st.text_input(
    "🚘 Car Name (optional)",
    placeholder="Eg: Hyundai Creta, Maruti Swift"
)

year = st.number_input(
    "📅 Car Manufacturing Year",
    min_value=2000,
    max_value=datetime.datetime.now().year,
    value=2018
)

kms_driven = st.number_input(
    "🛣️ Kilometers Driven",
    min_value=0,
    max_value=500000,
    value=40000
)

owner = st.selectbox(
    "👤 Number of Previous Owners",
    [0, 1, 2, 3]
)

# ================= FEATURE ENGINEERING =================
current_year = datetime.datetime.now().year
car_age = current_year - year

# ================= PREDICTION =================
st.markdown("---")

if st.button("🔮 Predict Car Price"):
    # Model expects: [model_year, kms, owner, Car_Age]
    input_data = np.array([[year, kms_driven, owner, car_age]])

    prediction = model.predict(input_data)

    if car_name.strip():
        st.success(
            f"🚗 **Car Name:** {car_name}\n\n"
            f"💰 **Estimated Selling Price:** ₹ {round(prediction[0], 2)}"
        )
    else:
        st.success(
            f"💰 **Estimated Selling Price:** ₹ {round(prediction[0], 2)}"
        )

# ================= FOOTER =================
st.markdown("---")
st.caption("Built with ❤️ using Machine Learning & Streamlit")
