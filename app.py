from fastapi import FastAPI
from pydantic import BaseModel
from env import AMREnv

app = FastAPI()
env = AMREnv()


class ActionRequest(BaseModel):
    action: str


@app.get("/")
def root():
    return {"message": "API is running"}


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
