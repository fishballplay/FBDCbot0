import discord
from discord.ext import commands
import os
bot =commands.Bot(command_prefix= '!')

@bot.event
async def on_ready():
    print('>>Bot is online')
for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(F'cmds.{Filename[:-3]}')
if __name__ == "__main__":
    bot.run('MzY4Mzk2MzM4MzA1Njk1NzQ1.WeDF0w.sKriItzVOZz81OZGsDGGHDVb8xM')