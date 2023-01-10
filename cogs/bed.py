import discord
from discord.ext import commands
import canvacord

class bed(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def bed(self, ctx, user1: discord.Member, *,user2: discord.Member = None):
        if user2 is None:
            author = ctx.author
            image = await canvacord.bed(author, user1)
            file = discord.File(filename="bed.png", fp=image)
            await ctx.reply(file=file)
        else:
            image = await canvacord.bed(user1, user2)
            file = discord.File(filename="bed.png", fp=image)
            await ctx.reply(file=file)
def setup(bot):
    bot.add_cog(bed(bot))