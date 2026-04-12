from fastapi import FastAPI
import uvicorn

from server.env import AMREnv

# Initialize FastAPI app
app = FastAPI(
    title="AMR Treatment Environment API",
    description="AI environment for optimizing antibiotic treatment strategies under antimicrobial resistance.",
    version="1.0.0"
)

# Initialize environment
env = AMREnv()


@app.get("/")
def root():
    return {"message": "AMR Treatment Environment is running successfully."}


@app.post("/reset")
def reset():
    """Reset the environment to its initial state."""
    state = env.reset()
    return {"state": state}


@app.post("/step")
def step(action: str):
    """Execute a step in the environment."""
    result = env.step(action)
    return result


@app.get("/state")
def get_state():
    """Retrieve the current state of the environment."""
    return {"state": env.get_state()}


def main():
    """Entry point for multi-mode deployment."""
    uvicorn.run(
        "server.app:app",
        host="0.0.0.0",
        port=7860,
        reload=False
    )


if __name__ == "__main__":
    main()
