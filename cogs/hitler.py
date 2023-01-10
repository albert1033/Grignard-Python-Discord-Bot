import discord
from discord.ext import commands
import canvacord

class hitler(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def hitler(self, ctx, *, user:discord.Member = None):
        if user is None:
            member = ctx.author
            image = await canvacord.hitler(member)
            file = discord.File(filename="hitler.png", fp=image)
            await ctx.reply(file=file)
        else:
            image = await canvacord.hitler(user)
            file = discord.File(filename="hitler.png", fp=image)
            await ctx.reply(file=file)
def setup(bot):
    bot.add_cog(hitler(bot))