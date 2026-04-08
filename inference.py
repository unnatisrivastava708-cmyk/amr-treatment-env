import requests

BASE_URL = "https://unnatisrivastava708-cmyk-amr-treatment-env-v2.hf.space"


def reset_env():
    r = requests.post(f"{BASE_URL}/reset")
    return r.json()["state"]


def step_env(action):
    r = requests.post(f"{BASE_URL}/step", json={"action": action})
    return r.json()


def main():
    print("[START] task=amr-treatment env=amr-env model=rule-based")

    rewards = []
    success = False
    steps = 0

    try:
        state = reset_env()

        for _ in range(10):
            steps += 1

            action = "increase_dose"

            result = step_env(action)

            reward = float(result["reward"])
            done = result["done"]

            rewards.append(f"{reward:.2f}")

            print(
                f"[STEP] step={steps} action={action} "
                f"reward={reward:.2f} done={str(done).lower()} error=null"
            )

            if done:
                success = True
                break

    except Exception as e:
        success = False

    finally:
        print(
            f"[END] success={str(success).lower()} "
            f"steps={steps} rewards={','.join(rewards)}"
        )


if __name__ == "__main__":
    main()
