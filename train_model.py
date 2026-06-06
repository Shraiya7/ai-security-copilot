import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.metrics import accuracy_score, classification_report

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/security_logs.csv")

features = [
    "failed_logins",
    "login_hour",
    "country_risk",
    "device_risk",
    "bytes_sent"
]

X = df[features]
y = df["risk_level"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

risk_model = RandomForestClassifier(
    n_estimators=150,
    random_state=42
)

risk_model.fit(X_train, y_train)

risk_predictions = risk_model.predict(X_test)

print("Risk Classifier Accuracy:")
print(accuracy_score(y_test, risk_predictions))
print(classification_report(y_test, risk_predictions))

joblib.dump(risk_model, "models/risk_classifier.pkl")

anomaly_model = IsolationForest(
    contamination=0.15,
    random_state=42
)

anomaly_model.fit(X)

joblib.dump(anomaly_model, "models/anomaly_detector.pkl")

print("Models saved successfully!")