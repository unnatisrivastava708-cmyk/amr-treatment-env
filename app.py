from fastapi import FastAPI
from pydantic import BaseModel
from env import AMREnv

app = FastAPI(root_path="")

env = AMREnv()

class ActionRequest(BaseModel):
    action: str


@app.post("/reset")
def reset():
    return {"state": env.reset()}


@app.post("/step")
def step(action_req: ActionRequest):
    state, reward, done = env.step(action_req.action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }


@app.get("/")
def home():
    return {"message": "API running"}


@app.get("/health")
def health():
    return {"status": "ok"}
