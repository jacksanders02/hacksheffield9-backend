import agents
import json
from fastapi import FastAPI
from pydantic import BaseModel

class PlayerAnswer(BaseModel):
    theme: str
    plan: str
    judge: str

app = FastAPI()

@app.post("/response")
def response(data: PlayerAnswer):
    res = agents.get_response(data.judge, data.theme, data.plan).text
    first_i = res.index("{")
    last_i = res.rindex("}")
    return json.loads(res[first_i:last_i+1])
