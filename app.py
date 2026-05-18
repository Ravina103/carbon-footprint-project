import streamlit as st

# Title
st.title("🌍 Carbon Footprint Calculator")

st.write("Calculate your annual carbon footprint based on your lifestyle.")

# User Inputs
transport = st.selectbox(
    "Choose your Transportation",
    ["Car", "Bike", "Public Transport"]
)

energy = st.selectbox(
    "Choose your Energy Usage",
    ["Low", "Medium", "High"]
)

diet = st.selectbox(
    "Choose your Diet",
    ["Vegetarian", "Meat and Dairy"]
)

waste = st.selectbox(
    "Choose your Waste Production",
    ["Low", "Medium", "High"]
)

# Score Calculation
score = 0

# Transportation Score
if transport == "Car":
    score += 4
elif transport == "Bike":
    score += 1
else:
    score += 2

# Energy Score
if energy == "High":
    score += 4
elif energy == "Medium":
    score += 2
else:
    score += 1

# Diet Score
if diet == "Meat and Dairy":
    score += 3
else:
    score += 1

# Waste Score
if waste == "High":
    score += 3
elif waste == "Medium":
    score += 2
else:
    score += 1

# Button
if st.button("Calculate Carbon Footprint"):
    result = score * 1.2

    st.success(f"Your annual carbon footprint is {result} tons CO₂")

    # Suggestions
    if result > 10:
        st.warning("Try using public transport and saving energy.")
    else:
        st.info("Great! Your carbon footprint is comparatively lower.")