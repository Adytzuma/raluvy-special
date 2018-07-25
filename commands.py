import discord
from discord.ext import commands
import asyncio
import logging
import math
import random



class Commands():
    def __init__(self, bot):
        self.bot = bot




        @commands.command()
        async def sal(ctx):
               await ctx.send('sal')
             





















def setup(bot):
        bot.add_cog(Commands(bot))
