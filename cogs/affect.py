import discord
from discord.ext import commands
import canvacord

class affect(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def affect(self, ctx, *, user:discord.Member = None):
        if user is None:
            member = ctx.author
            image = await canvacord.affect(member)
            file = discord.File(filename="affect.png", fp=image)
            await ctx.reply(file=file)
        else:
            image = await canvacord.affect(user)
            file = discord.File(filename="affect.png", fp=image)
            await ctx.reply(file=file)
def setup(bot):
    bot.add_cog(affect(bot))