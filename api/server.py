from fastapi import FastAPI
from pydantic import BaseModel
from env import AMREnv
from fastapi import Request

@app.post("/reset")
async def reset(request: Request):
    return {"state": env.reset()}

app = FastAPI()
env = AMREnv()

# ---- MODELS ----
class ActionRequest(BaseModel):
    action: str

# ---- ENDPOINTS ----

@app.post("/reset")
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
    return {"state": env.reset()}
