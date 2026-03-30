from fastapi import FastAPI
from pydantic import BaseModel
from env import AMREnv

app = FastAPI()
env = AMREnv()

# ---- MODELS ----
class ActionRequest(BaseModel):
    action: str

# ---- ENDPOINTS ----

@app.get("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action_req: ActionRequest):
    state, reward, done = env.step(action_req.action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

@app.get("/state")
def get_state():
    return {"state": env.state}
