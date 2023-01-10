import discord
from discord.ext import commands
import canvacord

class america(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def america(self, ctx, *, user:discord.Member = None):
        if user is None:
            member = ctx.author
            image = await canvacord.america(member)
            file = discord.File(filename="america.gif", fp=image)
            await ctx.reply(file=file)
        else:
            image = await canvacord.america(user)
            file = discord.File(filename="america.gif", fp=image)
            await ctx.reply(file=file)
def setup(bot):
    bot.add_cog(america(bot))