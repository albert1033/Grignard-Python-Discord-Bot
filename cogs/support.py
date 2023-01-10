import discord
from discord.ext import commands

class support(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def support(self, ctx):
        await ctx.reply("Please join our support server: https://discord.gg/gbgCyjhUqT")

def setup(bot):
    bot.add_cog(support(bot))