import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data/security_alerts.csv")

X = df["alert_text"]
y = df["threat_type"]

nlp_model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

nlp_model.fit(X, y)

joblib.dump(
    nlp_model,
    "models/threat_classifier.pkl"
)

print("NLP model trained successfully!")