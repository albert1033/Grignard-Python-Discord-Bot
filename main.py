import discord
from discord.ext import commands
import os
from nd_data import *
import jishaku
import json
import asyncio
def get_prefix(bot, message):
    with open(r'prefixes.json','r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]
bot = commands.Bot(command_prefix = get_prefix, help_command = None, case_insensitive=True, intents = discord.Intents.all())
#_________________________________________________________
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("$help"))
    print("I am alive")

@bot.event
async def on_guild_join(guild):
    with open(r'prefixes.json','r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '$'

    with open(r'prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
@bot.event
async def on_guild_remove(guild):
    with open(r'prefixes.json','r') as f:
        prefixes = json.load(f)
    
    prefixes.pop(str(guild.id))

    with open(r'prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)
@bot.event
async def on_message(message):
  pfx = get_prefix(bot, message)[0]
  if message.content.lower().startswith(pfx):
    message.content=message.content[:len(pfx)].lower() + message.content[len(pfx):]
  await bot.process_commands(message)
@bot.command()
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefix):
    with open(r'prefixes.json','r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix.lower()
    with open(r'prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.reply(f"Prefixed changed to {prefix.lower()}")
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("You can't do this command. Beg the owner for administrator first lmao.")
    if isinstance(error, commands.MissingRequiredArgument):
      member = ctx.author.mention
      await ctx.reply("Oi " + member +", check again if you forgot something in the command. You can do $help <command name> to see the full structure <a:dance:927768973443993650>")
    if isinstance(error, commands.NotOwner):
      embed = discord.Embed(title = "Error!", description = "You must own this bot to use this command", color = discord.Color.red())
      await ctx.reply(embed = embed)
#_________________________________________________________________
bot.load_extension("jishaku")
#________________________________________________
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

#________________________________________________

@bot.command()
async def ping(ctx):
  await ctx.reply(f'Pong! {round(bot.latency * 1000)}ms')
@bot.command()
@commands.is_owner()
async def servercount(ctx):
  await ctx.reply(f"I'm in {len(bot.guilds)} servers!")
@bot.command()
async def suggestion(ctx, *, suggestion):
  suggestion_channel = bot.get_channel(932202778464510032)
  await ctx.reply(f"Thank you {ctx.author.name}! We will read your suggestion and develop our bot")
  embed = discord.Embed(title="New Suggestion!", description=suggestion, color = discord.Color.teal())
  embed.set_footer(text=f"Author: {ctx.author.name} | Guild: {ctx.guild.id}")
  await suggestion_channel.send(embed = embed)

@bot.command()
async def report(ctx, *, report):
  report_channel = bot.get_channel(932204428700815420)
  await ctx.reply(f"Thank you {ctx.author.name}! We will read your report and develop our bot")
  embed = discord.Embed(title="New Report!", description=report, color = discord.Color.teal())
  embed.set_footer(text=f"Author: {ctx.author.name} | Guild: {ctx.guild.id}")
  await report_channel.send(embed = embed)

@bot.command()
@commands.is_owner()
async def reload(ctx,*, module:str):
  bot.unload_extension(f'cogs.{module}')
  bot.load_extension(f'cogs.{module}')
  await ctx.reply("done")
@bot.command()
@commands.is_owner()
async def load(ctx,*, module:str):
  bot.load_extension(f'cogs.{module}')
  await ctx.reply("done")
bot.run(TOKEN)
