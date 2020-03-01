import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='!')

@bot.event 
async def on_ready():
   print(">> Bot is online <<")

bot.run('NjgyNjA5MTEzNDY0NzAwOTI4.XltBQQ.uI5ihb3bOxH_pzfopss7q5YBnP0')