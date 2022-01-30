import os
from dotenv import load_dotenv
load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
server_id = os.getenv('SERVER_ID')
preifx = ""
disboard_prefix = "!d"
bump_msg = disboard_prefix + " bump"
stream = True
wait_time = 7460
