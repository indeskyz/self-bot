import os
import discord
import asyncio
import config
import wait_times
import helpers
import logging
import sys
from discord.ext import commands
from random import randint
from time import sleep
from random import randint


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

bot = commands.Bot(config.preifx, self_bot=True)

@bot.event
async def on_ready():
    if config.stream:
        await bot.change_presence(activity=discord.Streaming(name="Marc Jacobs Spring 1998", url="https://www.youtube.com/watch?v=Nv33ni_acFs&list=PLVo48CvBKNtjZiFwKNX0bRhn4wrISpP7c&index=2&t=6s"))
    print('logged in')
    

@bot.command()
async def bump(ctx):
    
    print('running command')
    async def sendMsg(msg):
        async with ctx.typing():
            await asyncio.sleep(randint(2, 9))
        await ctx.send(msg)

    while True:
        await sendMsg(config.bump_msg)
        sleep(helpers.set_wait_time(wait_times.bump_times))

bot.run(config.bot_token, bot=False)

