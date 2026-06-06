def calculate_risk_score(failed_logins, login_hour, country_risk, device_risk, bytes_sent):
    score = 0

    score += failed_logins * 2
    score += country_risk * 10
    score += device_risk * 8

    if login_hour < 6 or login_hour > 22:
        score += 20

    if bytes_sent > 15000:
        score += 30
    elif bytes_sent > 8000:
        score += 20
    elif bytes_sent > 4000:
        score += 10

    return min(score, 100)


def explain_event(failed_logins, login_hour, country_risk, device_risk, bytes_sent):
    reasons = []

    if failed_logins >= 10:
        reasons.append("High number of failed login attempts suggests possible brute-force activity.")

    if login_hour < 6 or login_hour > 22:
        reasons.append("The event occurred during unusual login hours.")

    if country_risk >= 4:
        reasons.append("The login originated from a high-risk location.")

    if device_risk >= 4:
        reasons.append("The device risk score indicates an unfamiliar or suspicious device.")

    if bytes_sent > 15000:
        reasons.append("Large outbound data transfer may indicate data exfiltration.")

    if not reasons:
        reasons.append("No major suspicious indicators were found.")

    return reasons