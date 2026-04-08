from fastapi import FastAPI, Request
from env import AMREnv
from pydantic import BaseModel


app = FastAPI()
env = AMREnv()

class ActionRequest(BaseModel):
    action: str

@app.api_route("/reset", methods=["GET", "POST"])
def reset():
    return env.reset()

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
