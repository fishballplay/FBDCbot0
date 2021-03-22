import discord
from discord.ext import commands
bot =commands.Bot(command_prefix= '!')

@bot.event
async def on_ready():
    print('>>Bot is online')

bot.run('MzY4Mzk2MzM4MzA1Njk1NzQ1.WeDF0w.sKriItzVOZz81OZGsDGGHDVb8xM')