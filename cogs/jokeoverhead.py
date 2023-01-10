import discord
from discord.ext import commands
import canvacord

class jokeoverhead(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def jokeoverhead(self, ctx, *, user:discord.Member = None):
        if user is None:
            member = ctx.author
            image = await canvacord.jokeoverhead(member)
            file = discord.File(filename="jokeoverhead.png", fp=image)
            await ctx.reply(file=file)
        else:
            image = await canvacord.jokeoverhead(user)
            file = discord.File(filename="jokeoverhead.png", fp=image)
            await ctx.reply(file=file)
def setup(bot):
    bot.add_cog(jokeoverhead(bot))