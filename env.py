import random

class AMREnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = {
            "bacteria_type": random.choice(["E.coli", "MRSA"]),
            "resistance_level": round(random.uniform(0.4, 0.9), 2),
            "patient_condition": round(random.uniform(0.5, 0.8), 2),
            "treatment_days": 0
        }
        return self.state

    def step(self, action):
        reward = 0

        # --- ACTION LOGIC ---
        if action == "beta_lactam":
            if self.state["resistance_level"] > 0.6:
                reward -= 0.3
                self.state["resistance_level"] += 0.05
            else:
                reward += 0.4
                self.state["patient_condition"] += 0.1

        elif action == "glycopeptide":
            if self.state["resistance_level"] > 0.7:
                reward -= 0.2
            else:
                reward += 0.3
                self.state["patient_condition"] += 0.08

        elif action == "AMP_therapy":
            reward += 0.5
            self.state["resistance_level"] -= 0.1
            self.state["patient_condition"] += 0.12

        elif action == "increase_dose":
            reward += 0.1
            self.state["patient_condition"] += 0.05
            self.state["resistance_level"] += 0.02

        elif action == "wait":
            reward -= 0.2
            self.state["patient_condition"] -= 0.05

        # --- UPDATE STATE ---
        self.state["treatment_days"] += 1

        # Clamp values between 0 and 1
        self.state["resistance_level"] = max(0, min(1, self.state["resistance_level"]))
        self.state["patient_condition"] = max(0, min(1, self.state["patient_condition"]))

        # --- TERMINATION ---
        done = False

        if self.state["patient_condition"] >= 1:
            done = True
            reward += 1  # success bonus

        elif self.state["patient_condition"] <= 0:
            done = True
            reward -= 1  # failure penalty

        return self.state, reward, done


# --- SIMPLE TEST RUN ---
from tasks import easy_task, medium_task, hard_task
from grader import grade

if __name__ == "__main__":
    env = AMREnv()

    state = easy_task()
    env.state = state

    print("Initial State:", state)

    actions = ["beta_lactam", "glycopeptide", "AMP_therapy", "increase_dose", "wait"]

    for step in range(7):
        action = random.choice(actions)
        state, reward, done = env.step(action)

        print(f"\nStep {step+1}")
        print("Action:", action)
        print("State:", state)
        print("Reward:", reward)

        if done:
            break

    final_score = grade(state)
    print("\nFinal Score:", final_score)