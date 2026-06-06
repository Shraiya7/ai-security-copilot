# AI Security Copilot

AI-powered cybersecurity risk analysis dashboard built with Python, Scikit-Learn, and Streamlit.

## High-Risk Security Event

![High Risk Event](screenshots/high-risk-event.png)

## Normal User Activity

![Normal Activity](screenshots/dashboard-normal.png)

## Features

- Machine learning risk classification
- Anomaly detection using Isolation Forest
- Custom cybersecurity risk scoring
- Explainable analyst-style security explanations
- Interactive Streamlit dashboard

## Technologies Used

- Python
- Pandas
- Scikit-Learn
- Streamlit
- Matplotlib
- Joblib

## How It Works

The dashboard takes security event inputs such as failed login attempts, login time, country risk, device risk, and bytes sent.

It uses a Random Forest model to classify the event as Low, Medium, or High risk. It also uses an Isolation Forest model to detect anomalies and a custom risk engine to explain why an event may be suspicious.

## How to Run

```bash
pip install -r requirements.txt
python create_data.py
python train_model.py
python -m streamlit run app.py
