import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from src.risk_engine import calculate_risk_score, explain_event

risk_model = joblib.load("models/risk_classifier.pkl")
anomaly_model = joblib.load("models/anomaly_detector.pkl")
threat_model = joblib.load("models/threat_classifier.pkl")

st.set_page_config(
    page_title="AI Security Copilot",
    layout="wide"
)

st.title("AI Security Copilot")

st.write(
    "This dashboard uses machine learning to classify cybersecurity events, "
    "detect anomalies, calculate risk scores, and explain suspicious behavior."
)

st.sidebar.header("Security Event Input")

failed_logins = st.sidebar.slider("Failed Login Attempts", 0, 40, 5)
login_hour = st.sidebar.slider("Login Hour", 0, 23, 12)
country_risk = st.sidebar.slider("Country Risk Score", 1, 5, 2)
device_risk = st.sidebar.slider("Device Risk Score", 1, 5, 2)
bytes_sent = st.sidebar.slider("Bytes Sent", 100, 40000, 3000)
alert_text = st.sidebar.text_area(
    "Security Alert Text",
    "Multiple failed login attempts from same IP"
)

input_data = pd.DataFrame([{
    "failed_logins": failed_logins,
    "login_hour": login_hour,
    "country_risk": country_risk,
    "device_risk": device_risk,
    "bytes_sent": bytes_sent
}])

risk_prediction = risk_model.predict(input_data)[0]
anomaly_prediction = anomaly_model.predict(input_data)[0]
threat_prediction = threat_model.predict([alert_text])[0]

risk_score = calculate_risk_score(
    failed_logins,
    login_hour,
    country_risk,
    device_risk,
    bytes_sent
)

explanations = explain_event(
    failed_logins,
    login_hour,
    country_risk,
    device_risk,
    bytes_sent
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("ML Risk Level", risk_prediction)

with col2:
    st.metric("Risk Score", f"{risk_score}/100")

with col3:
    if anomaly_prediction == -1:
        st.metric("Anomaly Detection", "Anomaly")
    else:
        st.metric("Anomaly Detection", "Normal")
with col4:
    st.metric("NLP Threat Type", threat_prediction)

st.divider()

st.subheader("Analyst Explanation")

for explanation in explanations:
    st.write("- " + explanation)

st.subheader("Input Event Data")
st.dataframe(input_data)
st.subheader("Security Alert Text")
st.info(alert_text)

st.subheader("Risk Score Visualization")

fig, ax = plt.subplots()
ax.bar(["Risk Score"], [risk_score])
ax.set_ylim(0, 100)
ax.set_ylabel("Score")
st.pyplot(fig)

st.subheader("Skills Demonstrated")

st.write("""
- Python programming
- Machine learning classification
- Anomaly detection
- Cybersecurity risk scoring
- Explainable security analysis
- Streamlit dashboard development
""")