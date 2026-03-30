from fastapi import FastAPI, Request
from pydantic import BaseModel
from env import AMREnv

app = FastAPI()
env = AMREnv()

class ActionRequest(BaseModel):
    action: str

@app.post("/reset")
async def reset(request: Request):
    return {"state": env.reset()}

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
