import discord
from discord.ext import commands
import canvacord

class trigger(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def trigger(self, ctx, *, user:discord.Member = None):
        if user is None:
            member = ctx.author
            image = await canvacord.trigger(member)
            file = discord.File(filename="trigger.gif", fp=image)
            await ctx.reply(file=file)
        else:
            image = await canvacord.trigger(user)
            file = discord.File(filename="trigger.gif", fp=image)
            await ctx.reply(file=file)
def setup(bot):
    bot.add_cog(trigger(bot))