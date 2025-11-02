import streamlit as st
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

# -----------------------------
# 🔗 FastAPI endpoint
# -----------------------------

API_URL = os.getenv("API_URL")



# -----------------------------
# 🖤 Page Config
# -----------------------------
st.set_page_config(
    page_title="Customer Prosperity Prediction",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -----------------------------
# 🎨 Custom Dark Theme
# -----------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
    color: #f0f6fc;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.stApp {
    background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
}
.css-1d391kg {
    background-color: #21262d;
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
    border: 1px solid #30363d;
}
.stButton button {
    background: linear-gradient(135deg, #58a6ff 0%, #1f6feb 100%);
    color: white;
    border-radius: 8px;
    border: none;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: bold;
    transition: all 0.3s ease;
}
.stButton button:hover {
    background: linear-gradient(135deg, #1f6feb 0%, #388bfd 100%);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(88, 166, 255, 0.3);
}
h1, h2, h3 { color: #f0f6fc; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 📘 Sidebar
# -----------------------------

with st.sidebar:
    st.header("📊 How to Use This Dashboard")
    st.write("""
    **Lets Travel – Customer Targeting Dashboard**  

    This tool helps your team identify customers **most likely to purchase** the new **Wellness Tourism Package**.  

    **Steps for Use:**
    1. Enter customer details in the form.
    2. Click **Predict** to get likelihood of purchase.
    3. Review **confidence scores** and probability distribution.
    4. Focus marketing efforts on high-probability customers to reduce costs.

    **Benefits for Your Team:**
    - Target potential buyers efficiently
    - Optimize marketing campaigns
    - Reduce unnecessary expenditure
    - Make data-driven business decisions
    """)


# -----------------------------
# 💼 Main Page
# -----------------------------
st.title("💼 Customer Prosperity Modelling")
st.markdown("<p style='text-align:center;color:#c9d1d9;'>Predict whether a customer is likely to buy based on their profile.</p>", unsafe_allow_html=True)

# -----------------------------
# 🧾 Input Form
# -----------------------------
with st.form("prediction_form"):
    st.subheader("📝 Enter Customer Details")

    col1, col2 = st.columns(2)
    with col1:
        Age = st.number_input("Age", 18, 80, 30)
        TypeofContact = st.selectbox("Type of Contact", ["Self Enquiry", "Company Invited"])
        CityTier = st.selectbox("City Tier", [1, 2, 3])
        DurationOfPitch = st.number_input("Duration of Pitch (minutes)", 0, 60, 20)
        Occupation = st.selectbox("Occupation", ["Salaried", "Small Business", "Large Business", "Other"])
        Gender = st.selectbox("Gender", ["Male", "Female"])
        NumberOfPersonVisiting = st.number_input("No. of Persons Visiting", 0, 10, 2)
        NumberOfFollowups = st.number_input("No. of Followups", 0, 10, 2)
        ProductPitched = st.selectbox("Product Pitched", ["Basic", "Deluxe", "Standard", "Super Deluxe", "King"])

    with col2:
        PreferredPropertyStar = st.selectbox("Preferred Property Star", [3, 4, 5])
        MaritalStatus = st.selectbox("Marital Status", ["Married", "Unmarried", "Divorced"])
        NumberOfTrips = st.number_input("No. of Trips", 0, 20, 1)
        Passport = st.selectbox("Passport", ["Yes", "No"])
        PitchSatisfactionScore = st.slider("Pitch Satisfaction Score", 1, 5, 3)
        OwnCar = st.selectbox("Own Car", ["Yes", "No"])
        NumberOfChildrenVisiting = st.number_input("No. of Children Visiting", 0, 10, 0)
        Designation = st.selectbox("Designation", ["Executive", "Manager", "Senior Manager", "AVP", "VP"])
        MonthlyIncome = st.number_input("Monthly Income", 10000, 200000, 50000)

    submitted = st.form_submit_button("🔍 Predict Prosperity")

# -----------------------------
# -----------------------------
# 🚀 API Integration
# 🚀 Prediction Logic
# -----------------------------
# -----------------------------

if submitted:
    payload = {
        "Age": Age,
        "TypeofContact": TypeofContact,
        "CityTier": CityTier,
        "DurationOfPitch": DurationOfPitch,
        "Occupation": Occupation,
        "Gender": Gender,
        "NumberOfPersonVisiting": NumberOfPersonVisiting,
        "NumberOfFollowups": NumberOfFollowups,
        "ProductPitched": ProductPitched,
        "PreferredPropertyStar": PreferredPropertyStar,
        "MaritalStatus": MaritalStatus,
        "NumberOfTrips": NumberOfTrips,
        "Passport": Passport,
        "PitchSatisfactionScore": PitchSatisfactionScore,
        "OwnCar": OwnCar,
        "NumberOfChildrenVisiting": NumberOfChildrenVisiting,
        "Designation": Designation,
        "MonthlyIncome": MonthlyIncome
    }

    with st.spinner("Analyzing Customer Profile... ⏳"):
        try:
            response = requests.post(API_URL, json=payload)
            result = response.json()

            if "prediction" in result:
                pred = result["prediction"]
                conf = result.get("confidence", 0)

                # Display main prediction
                st.success(f"### 🧭 Prediction: {pred}")
                st.write(f"**Confidence:** {conf:.2f}")
                st.progress(int(conf * 100))

                # Display probabilities nicely
                st.subheader("📈 Purchase Probability Distribution")
                probabilities = result.get("probabilities", {})

                # Convert to percentages and sort by probability
                sorted_probs = dict(sorted(probabilities.items(), key=lambda x: x[1], reverse=True))
                for label, prob in sorted_probs.items():
                    st.write(f"**{label}:** {prob*100:.2f}%")
                    st.progress(prob)

            else:
                st.error(f"⚠️ Error: {result.get('error', 'Unknown issue')}")

        except Exception as e:
            st.error(f"❌ Could not connect to API — check if it's running. Error: {e}")














# st.set_page_config(page_title="Customer Prosperity Prediction", page_icon="💰", layout="centered")


# # -----------------------------
# # 🎨 Page title
# # -----------------------------

# st.title("💼 Customer Prosperity Modelling")
# st.write("Predict whether a customer is **likely to buy** based on their profile.")

# # -----------------------------
# # 🧾 Input Form
# # -----------------------------
# with st.form("input_form"):
#     st.subheader("Enter Customer Details")

#     col1, col2 = st.columns(2)

#     with col1:
#         Age = st.number_input("Age", min_value=0, max_value=120, value=30)
#         TypeofContact = st.selectbox("Type of Contact", ["Self Enquiry", "Company Invited"])
#         CityTier = st.selectbox("City Tier", [1, 2, 3])
#         DurationOfPitch = st.number_input("Duration of Pitch (minutes)", min_value=0, value=20)
#         Occupation = st.selectbox("Occupation", ["Salaried", "Small Business", "Large Business", "Other"])
#         Gender = st.selectbox("Gender", ["Male", "Female"])
#         NumberOfPersonVisiting = st.number_input("Number of Persons Visiting", min_value=0, value=2)
#         NumberOfFollowups = st.number_input("Number of Followups", min_value=0, value=2)
#         ProductPitched = st.selectbox("Product Pitched", ["Basic", "Deluxe", "Standard", "Super Deluxe", "King"])

#     with col2:
#         PreferredPropertyStar = st.selectbox("Preferred Property Star", [3, 4, 5])
#         MaritalStatus = st.selectbox("Marital Status", ["Married", "Unmarried", "Divorced"])
#         NumberOfTrips = st.number_input("Number of Trips", min_value=0, value=1)
#         Passport = st.selectbox("Passport", ["Yes", "No"])
#         PitchSatisfactionScore = st.slider("Pitch Satisfaction Score", 1, 5, 3)
#         OwnCar = st.selectbox("Own Car", ["Yes", "No"])
#         NumberOfChildrenVisiting = st.number_input("Number of Children Visiting", min_value=0, value=0)
#         Designation = st.selectbox("Designation", ["Executive", "Manager", "Senior Manager", "AVP", "VP"])
#         MonthlyIncome = st.number_input("Monthly Income", min_value=0, value=50000)

#     submitted = st.form_submit_button("🔍 Predict")

# # -----------------------------
# # 🚀 Prediction Logic
# # -----------------------------

# if submitted:
#     # Prepare payload for FastAPI
#     payload = {
#         "Age": Age,
#         "TypeofContact": TypeofContact,
#         "CityTier": CityTier,
#         "DurationOfPitch": DurationOfPitch,
#         "Occupation": Occupation,
#         "Gender": Gender,
#         "NumberOfPersonVisiting": NumberOfPersonVisiting,
#         "NumberOfFollowups": NumberOfFollowups,
#         "ProductPitched": ProductPitched,
#         "PreferredPropertyStar": PreferredPropertyStar,
#         "MaritalStatus": MaritalStatus,
#         "NumberOfTrips": NumberOfTrips,
#         "Passport": Passport,
#         "PitchSatisfactionScore": PitchSatisfactionScore,
#         "OwnCar": OwnCar,
#         "NumberOfChildrenVisiting": NumberOfChildrenVisiting,
#         "Designation": Designation,
#         "MonthlyIncome": MonthlyIncome
#     }

#     with st.spinner("Predicting... ⏳"):
#         try:
#             response = requests.post(API_URL, json=payload)
#             result = response.json()

#             if "prediction" in result:
#                 st.success(f"### 🧭 Prediction: {result['prediction']}")
#                 st.write(f"**Confidence:** {result['confidence']:.2f}")

#                 # Probability visualization
#                 st.progress(int(result['confidence'] * 100))

#                 st.write("### Probability Distribution:")
#                 st.json(result["probabilities"])
#             else:
#                 st.error(f"Error: {result.get('error', 'Unknown issue')}")

#         except Exception as e:
#             st.error(f"❌ Could not connect to API: {e}")













