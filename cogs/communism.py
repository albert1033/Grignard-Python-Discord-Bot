import discord
from discord.ext import commands
import canvacord

class communism(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def communism(self, ctx, *, user:discord.Member = None):
        if user is None:
            member = ctx.author
            image = await canvacord.communism(member)
            file = discord.File(filename="communism.gif", fp=image)
            await ctx.reply(file=file)
        else:
            image = await canvacord.communism(user)
            file = discord.File(filename="communism.gif", fp=image)
            await ctx.reply(file=file)
def setup(bot):
    bot.add_cog(communism(bot))