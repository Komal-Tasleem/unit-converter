import streamlit as st

def convert_units(value, from_unit, to_unit, category):
    conversions = {
        "Length": {
            "Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001, "Mile": 1609.34,
            "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254
        },
        "Weight": {
            "Kilogram": 1, "Gram": 0.001, "Milligram": 0.000001, "Pound": 0.453592, "Ounce": 0.0283495
        },
        "Temperature": {
            "Celsius": lambda x: x, 
            "Fahrenheit": lambda x: (x * 9/5) + 32, 
            "Kelvin": lambda x: x + 273.15
        }
    }
    
    if category == "Temperature":
        if from_unit == "Fahrenheit":
            value = (value - 32) * 5/9
        elif from_unit == "Kelvin":
            value = value - 273.15
        return conversions[category][to_unit](value)
    else:
        return value * (conversions[category][to_unit] / conversions[category][from_unit])

st.set_page_config(page_title="Unit Converter", page_icon="⚙️", layout="centered")

st.markdown(
    """
    <style>
        .stApp { background-color: black; color: white; font-family: Arial, sans-serif; }
        .title { color: #A32CC4; text-align: center; font-size: 40px; font-weight: bold; }
        .stSelectbox label, .stNumberInput label { color: grey; font-weight: bold; font-size: 16px; }
        .stSelectbox div[data-baseweb="select"] > div, .stNumberInput input { color: black; font-weight: bold; background: #f0f0f0; border-radius: 5px; }
        .stButton > button { background-color: purple; color: white; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 8px; transition: 0.3s; }
        .stButton > button:hover { background-color: #c77dff; }
        .stButton > button span { font-weight: bold; }
        .stAlert { background-color: #d9a7ff; color: black; font-weight: bold; font-size: 18px; padding: 10px; border-radius: 8px; }
        .footer { text-align: center; margin-top: 20px; color: grey; font-size: 14px; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>🔄 Unit Converter App</h1>", unsafe_allow_html=True)
st.markdown(" WELCOME! select a category, enter a value, and get the converted value in the desired unit.")
category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"], key="category")

units = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Weight": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}[category]

from_unit = st.selectbox("From Unit", units, key="from_unit")
to_unit = st.selectbox("To Unit", units, key="to_unit")
value = st.number_input("Enter Value", format="%.6f", key="value")

if st.button("**Convert**"):
    result = convert_units(value, from_unit, to_unit, category)
    st.markdown(f"<div class='stAlert'>✅ Converted Value: {result:.6f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>KOMAL TASLEEM</div>", unsafe_allow_html=True)