import os
import requests
import random

# --- REQUIRED ENV VARIABLES ---
API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

# --- ACTION SPACE ---
actions = [
    "beta_lactam",
    "glycopeptide",
    "AMP_therapy",
    "increase_dose",
    "wait"
]

# --- RESET ---
state = requests.post(f"{API_BASE_URL}/reset").json()

print(f"START state={state}")

# --- STEPS ---
for step in range(7):
    action = random.choice(actions)

    response = requests.post(
        f"{API_BASE_URL}/step",
        json={"action": action}
    ).json()

    state = response["state"]
    reward = response["reward"]
    done = response["done"]

    print(f"STEP action={action} state={state} reward={reward}")

    if done:
        break

# --- END ---
print(f"END state={state}")
