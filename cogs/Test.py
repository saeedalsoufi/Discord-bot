import discord
from discord.ext import commands
from .utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help, settings
from datetime import datetime
from collections import deque, defaultdict, OrderedDict
from cogs.utils.chat_formatting import escape_mass_mentions, box, pagify
import os
import re
import logging
import asyncio



class Test:

    def __init__(self, bot):
        self.bot = bot
            
    @commands.command(pass_context=True)
    async def invitelink(self):
            await self.bot.say("https://discord.gg/GCGuD4q")


def setup(bot):
    bot.add_cog(Test(bot))