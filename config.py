import os
from dotenv import load_dotenv
load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
preifx = ""
disboard_prefix = "!d"
bump_msg = disboard_prefix + " bump"
stream = True
