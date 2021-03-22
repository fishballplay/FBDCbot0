import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Makeline(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        keywords = ['felt','tabasa']
        for keyword in keywords:
            if msg.content.find(keyword) != -1 and msg.author != self.bot:
               await msg.channel.send('OuOb')
               break



def setup(bot):
    bot.add_cog(Makeline(bot))