import os
from dotenv import load_dotenv
load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
channel_id = os.getenv('CHANNEL_ID')
preifx = ""
disboard_prefix = "!d"
bump_msg = disboard_prefix + " bump"
stream = True
wait_time = 7460
