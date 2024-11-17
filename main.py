from fastapi import HTTPException

import agents
import json
from fastapi import FastAPI
from pydantic import BaseModel

from game_driver import add_user_to_room, get_room_json, ready_user, get_user_json, is_valid_room, is_valid_user, \
    get_room_from_code, remove_user_from_room, get_last_joined_user, get_current_room_theme, advance_room_round
from pusher_controller import run_pusher


def validate_room(room_code):
    if not is_valid_room(room_code):
        raise HTTPException(status_code=404, detail="Room not found")

def validate_room_and_user(room_code, username):
    validate_room(room_code)
    if not is_valid_user(username, get_room_from_code(room_code)):
        raise HTTPException(status_code=404, detail="User not found")

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

class JoinGameParams(BaseModel):
    username: str
    room_code: str

@app.get("/room/{room_code}")
def get_room(room_code):
    validate_room(room_code)
    return get_room_json(room_code)

@app.get("/room/{room_code}/user/last")
def get_last_joined_user_to_room(room_code):
    validate_room(room_code)
    return get_last_joined_user(room_code)

@app.get("/room/{room_code}/user/{username}")
def get_user(room_code, username):
    validate_room_and_user(room_code, username)
    return get_user_json(username, room_code)

@app.post("/room/{room_code}/user/{username}")
def join_game(room_code, username):
    add_user_to_room(username, room_code)
    return get_user_json(username, room_code)

@app.delete("/room/{room_code}/user/{username}")
def leave(room_code, username):
    validate_room_and_user(room_code, username)
    remove_user_from_room(username, room_code)

@app.post("/room/{room_code}/user/{username}/ready")
def ready_up(room_code, username):
    validate_room_and_user(room_code, username)
    return ready_user(username, room_code)

@app.get("/room/{room_code}/theme")
def get_room_theme(room_code):
    validate_room(room_code)
    return get_current_room_theme(room_code)

@app.get("/room/{room_code}/advance-round")
def advance_round(room_code):
    validate_room(room_code)
    return advance_room_round(room_code)

class AnswerParams(BaseModel):
    answer: str

# @app.post("/room/{room_code}/user/{username}/answer")
# def answer(room_code, username, answer: AnswerParams):
#
