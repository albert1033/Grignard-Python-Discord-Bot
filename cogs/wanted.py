import discord
from discord.ext import commands
import canvacord

class wanted(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def wanted(self, ctx, *, user:discord.Member = None):
        if user is None:
            member = ctx.author
            image = await canvacord.wanted(member)
            file = discord.File(filename="wanted.png", fp=image)
            await ctx.reply(file=file)
        else:
            image = await canvacord.wanted(user)
            file = discord.File(filename="wanted.png", fp=image)
            await ctx.reply(file=file)
def setup(bot):
    bot.add_cog(wanted(bot))