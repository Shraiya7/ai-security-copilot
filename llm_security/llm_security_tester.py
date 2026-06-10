import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
def classify_attack(prompt):
    prompt_lower = prompt.lower()

    if "ignore" in prompt_lower or "previous instructions" in prompt_lower:
        return "Prompt Injection"

    if "dan" in prompt_lower or "unrestricted" in prompt_lower:
        return "Jailbreak"

    if "system prompt" in prompt_lower or "private data" in prompt_lower:
        return "Data Leakage"

    if "base64" in prompt_lower or "credentials" in prompt_lower:
        return "Credential Extraction"

    return "General LLM Security Test"


def recommend_defense(attack_type):
    defenses = {
        "Prompt Injection": "Use instruction hierarchy, input validation, and output filtering.",
        "Jailbreak": "Use safety guardrails, refusal policies, and adversarial testing.",
        "Data Leakage": "Use data minimization, access control, and retrieval filtering.",
        "Credential Extraction": "Use secret scanning, output filtering, and credential isolation.",
        "General LLM Security Test": "Use monitoring, logging, and human review."
    }

    return defenses.get(attack_type, "Review manually.")


def run_security_test(prompt):
    attack_type = classify_attack(prompt)
    recommendation = recommend_defense(attack_type)

    return {
        "attack_type": attack_type,
        "result": "Needs Review",
        "risk_level": "Medium",
        "recommendation": recommendation
    }

def load_prompt_injection_tests():
    csv_path = BASE_DIR / "prompts" / "prompt_injection_tests.csv"
    tests = pd.read_csv(csv_path)
    return tests
def load_jailbreak_tests():
    csv_path = BASE_DIR / "prompts" / "jailbreak_tests.csv"
    tests = pd.read_csv(csv_path)
    return tests
def load_rag_document(file_name):
    file_path = BASE_DIR / "rag" / file_name

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return content

if __name__ == "__main__":

    prompt_injection_tests = load_prompt_injection_tests()
    jailbreak_tests = load_jailbreak_tests()

    all_tests = pd.concat([prompt_injection_tests, jailbreak_tests])

    print("Loaded LLM Security Tests")
    print("-------------------------")

    for index, row in all_tests.iterrows():
        prompt = row["prompt"]
        result = run_security_test(prompt)

        print()
        print(f"Test ID: {row['test_id']}")
        print(f"Expected Category: {row['attack_type']}")
        print(f"Prompt: {prompt}")
        print(f"Detected Attack Type: {result['attack_type']}")
        print(f"Risk Level: {result['risk_level']}")
        print(f"Recommendation: {result['recommendation']}")
        print()
    print("RAG Manipulation Test")
    print("---------------------")

    malicious_doc = load_rag_document("malicious_policy.txt")
    rag_result = run_security_test(malicious_doc)

    print(f"Document Tested: malicious_policy.txt")
    print(f"Detected Attack Type: {rag_result['attack_type']}")
    print(f"Risk Level: {rag_result['risk_level']}")
    print(f"Recommendation: {rag_result['recommendation']}")