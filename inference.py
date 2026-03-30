import requests
import random

BASE_URL = "http://127.0.0.1:8000"

actions = ["beta_lactam", "glycopeptide", "AMP_therapy", "increase_dose", "wait"]

# Reset environment
state = requests.get(f"{BASE_URL}/reset").json()["state"]
print("Initial:", state)

for step in range(7):
    action = random.choice(actions)

    response = requests.post(
        f"{BASE_URL}/step",
        json={"action": action}
    ).json()

    state = response["state"]
    reward = response["reward"]

    print(f"\nStep {step+1}")
    print("Action:", action)
    print("State:", state)
    print("Reward:", reward)

    if response["done"]:
        break

print("\nFinal State:", state)