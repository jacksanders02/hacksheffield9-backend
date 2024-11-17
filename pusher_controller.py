import os
import pusher
from dotenv import  load_dotenv

def run_pusher():
    load_dotenv()

    return pusher.Pusher(
        app_id=os.getenv('NEXT_PUBLIC_PUSHER_APP_ID'),
        key=os.getenv('NEXT_PUBLIC_PUSHER_PUBLISHABLE_KEY'),
        secret=os.getenv('PUSHER_SECRET_KEY'),
        cluster=os.getenv('NEXT_PUBLIC_PUSHER_CLUSTER'),
    )