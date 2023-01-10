import discord
from discord.ext import commands
import canvacord

class aborted(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def aborted(self, ctx, *, user:discord.Member = None):
        if user is None:
            member = ctx.author
            image = await canvacord.aborted(member)
            file = discord.File(filename="aborted.png", fp=image)
            await ctx.reply(file=file)
        else:
            image = await canvacord.aborted(user)
            file = discord.File(filename="aborted.png", fp=image)
            await ctx.reply(file=file)
def setup(bot):
    bot.add_cog(aborted(bot))