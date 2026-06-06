import pandas as pd

data = [
    ["Multiple failed login attempts from same IP", "Brute Force"],
    ["Repeated password guessing detected", "Brute Force"],
    ["Large number of login failures", "Brute Force"],

    ["User entered credentials on fake website", "Phishing"],
    ["Suspicious email requesting password", "Phishing"],
    ["Credential harvesting attempt detected", "Phishing"],

    ["Malicious software installed on endpoint", "Malware"],
    ["Suspicious executable downloaded", "Malware"],
    ["Trojan detected on workstation", "Malware"],

    ["Files encrypted and ransom demanded", "Ransomware"],
    ["Mass file encryption activity detected", "Ransomware"],
    ["Ransom note found on system", "Ransomware"],

    ["Large volume of sensitive data transferred", "Data Exfiltration"],
    ["Unusual outbound traffic detected", "Data Exfiltration"],
    ["Confidential files copied externally", "Data Exfiltration"]
]

df = pd.DataFrame(data, columns=["alert_text", "threat_type"])

df.to_csv("data/security_alerts.csv", index=False)

print("NLP dataset created")