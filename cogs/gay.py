import discord
from discord.ext import commands
import canvacord

class gay(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def gay(self, ctx, *, user:discord.Member = None):
        if user is None:
            member = ctx.author
            image = await canvacord.gay(member)
            file = discord.File(filename="gay.png", fp=image)
            await ctx.reply(file=file)
        else:
            image = await canvacord.gay(user)
            file = discord.File(filename="gay.png", fp=image)
            await ctx.reply(file=file)
def setup(bot):
    bot.add_cog(gay(bot))