import agents
from fastapi import FastAPI
from pydantic import BaseModel

class PlayerAnswer(BaseModel):
    theme: str
    plan: str
    judge: str

app = FastAPI()

@app.post("/response")
def response(data: PlayerAnswer):
    return {
        "test": agents.get_response(data.judge, data.theme, data.plan)
    }
