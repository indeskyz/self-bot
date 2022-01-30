import asyncio
import config
import discord
import logging
from discord.ext import commands, tasks
from random import randint

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# class MyClient(discord.Client):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # an attribute we can access from our task
#         self.bump_command = config.bump_msg

#         # start the task to run in the background
#         self.my_background_task.start()

#     async def on_ready(self):
#         print('Logged in as')
#         print(self.user.name)
#         print(self.user.id)
#         print('------')

#     @tasks.loop(seconds=config.wait_time)
#     async def my_background_task(self):
#         channel = self.get_channel(config.server_id) 
#         await channel.send(self.bump_command)

#     @my_background_task.before_loop
#     async def before_my_task(self):
#         await self.wait_until_ready()

# client = MyClient()
# client.run(config.bot_token)


# bot = commands.Bot(config.preifx, self_bot=True)

@bot.event
async def on_ready():
    if config.stream:
        await bot.change_presence(activity=discord.Streaming(name="Marc Jacobs Spring 1998", url="https://www.youtube.com/watch?v=Nv33ni_acFs&list=PLVo48CvBKNtjZiFwKNX0bRhn4wrISpP7c&index=2&t=6s"))
    print('logged in')
    

@bot.command()
async def bump(ctx):
    
    async def sendMsg(msg):
        async with ctx.typing():
            await asyncio.sleep(randint(2, 9))
        await ctx.send(msg)
    
    while True:
        await sendMsg(config.bump_msg)
        await asyncio.sleep(config.wait_time)



bot.run(config.bot_token, bot=False)

