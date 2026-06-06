import pandas as pd
import random
import os

os.makedirs("data", exist_ok=True)

logs = []

for _ in range(400):
    logs.append({
        "failed_logins": random.randint(0, 3),
        "login_hour": random.randint(8, 18),
        "country_risk": random.randint(1, 2),
        "device_risk": random.randint(1, 2),
        "bytes_sent": random.randint(100, 3000),
        "risk_level": "Low"
    })

for _ in range(300):
    logs.append({
        "failed_logins": random.randint(4, 10),
        "login_hour": random.choice([0, 1, 2, 3, 21, 22, 23]),
        "country_risk": random.randint(2, 4),
        "device_risk": random.randint(2, 4),
        "bytes_sent": random.randint(3000, 9000),
        "risk_level": "Medium"
    })

for _ in range(300):
    logs.append({
        "failed_logins": random.randint(11, 40),
        "login_hour": random.choice([0, 1, 2, 3, 4]),
        "country_risk": random.randint(4, 5),
        "device_risk": random.randint(4, 5),
        "bytes_sent": random.randint(9000, 40000),
        "risk_level": "High"
    })

df = pd.DataFrame(logs)
df.to_csv("data/security_logs.csv", index=False)

print("Dataset created successfully!")
print(df.head())