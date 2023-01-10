import discord
from discord.ext import commands
import canvacord

class airpods(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def airpods(self, ctx, *, user:discord.Member = None):
        if user is None:
            member = ctx.author
            image = await canvacord.airpods(member)
            file = discord.File(filename="airpods.gif", fp=image)
            await ctx.reply(file=file)
        else:
            image = await canvacord.airpods(user)
            file = discord.File(filename="airpods.gif", fp=image)
            await ctx.reply(file=file)
def setup(bot):
    bot.add_cog(airpods(bot))