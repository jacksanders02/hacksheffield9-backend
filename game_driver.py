from pusher_controller import run_pusher


class Room:
    def __init__(self, name: str):
        self.name = name
        self.users = {}
        self.round = 0
        self.current_theme = ""
        self.last_joined_user = ""

    def is_ready(self):
        return all(user.ready for user in self.users.values())

class User:
    def __init__(self, name: str, room: Room):
        self.name = name
        self.score = 0
        self.ready = False
        self.current_room = room
        self.submitted_answer = ""

        self.current_room.users[name] = self

    def ready_up(self):
        self.ready = not self.ready

NUM_ROUNDS = 5
GAME_ROOMS = {}
THEMES = [
    "A bank for polar bears",
    "Suits for babies",
    "Worm smoothies",
    "Boats made out of cheese",
    "Cars made entirely out of glass"
]
pusher_client = run_pusher()

def get_room_from_code(room_code):
    return GAME_ROOMS[room_code]

def is_valid_room(room_code: str):
    return room_code in GAME_ROOMS

def is_valid_user(username: str, room: Room):
    return username in room.users

def get_user_json(username, room_code):
    user = get_room_from_code(room_code).users[username]
    return {
        "name": user.name,
        "score": user.score,
        "ready": user.ready,
        "current_room": user.current_room.name,
        "submitted_answer": user.submitted_answer
    }

def get_room_json(room_code):
    room = get_room_from_code(room_code)
    return {
        "name": room.name,
        "round": room.round,
        "current_theme": room.current_theme,
        "ready": room.is_ready(),
        "users": [get_user_json(username, room_code) for username in room.users.keys()]
    }

def add_user_to_room(username, room_code):
    if not is_valid_room(room_code):
        GAME_ROOMS[room_code] = Room(room_code)

    get_room_from_code(room_code).users[username] = User(username, get_room_from_code(room_code))
    get_room_from_code(room_code).last_joined_user = username

def get_last_joined_user(room_code):
    return get_room_from_code(room_code).last_joined_user

def remove_user_from_room(username, room_code):
    del get_room_from_code(room_code).users[username]
    if len(get_room_from_code(room_code).users) == 0:
        del GAME_ROOMS[room_code]

def ready_user(username, room_code):
    get_room_from_code(room_code).users[username].ready_up()
    if get_room_from_code(room_code).is_ready():
        pusher_client.trigger(room_code, 'game_start', {})
    return get_room_from_code(room_code).users[username].ready

def get_current_room_theme(room_code):
    current_round = get_room_from_code(room_code).round
    return THEMES[current_round - 1]

def advance_room_round(room_code):
    get_room_from_code(room_code).round += 1
    if get_room_from_code(room_code).round > NUM_ROUNDS:
        return -1
    return get_room_from_code(room_code).round

def add_user_answer(username, room_code, answer):
    get_room_from_code(room_code)