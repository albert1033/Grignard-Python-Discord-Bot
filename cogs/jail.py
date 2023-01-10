import discord
from discord.ext import commands
import canvacord

class jail(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def jail(self, ctx, *, user:discord.Member = None):
        if user is None:
            member = ctx.author
            image = await canvacord.jail(member)
            file = discord.File(filename="jail.png", fp=image)
            await ctx.reply(file=file)
        else:
            image = await canvacord.jail(user)
            file = discord.File(filename="jail.png", fp=image)
            await ctx.reply(file=file)
def setup(bot):
    bot.add_cog(jail(bot))