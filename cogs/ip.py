import discord
from discord.ext import commands
import random
import asyncio
class ip(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command(aliases = ['ipadress'])
    async def ip(self, ctx, *, user: discord.Member = None):
        if user is None:
            msg = await ctx.reply(f"We are finding your IP address, {ctx.author.mention} <a:loadingloading:928828204632899644>")
            await asyncio.sleep(7)
            await msg.edit(f"{ctx.author.mention}, your IP address is {random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}")
        else:
            msg = await ctx.reply(f"{ctx.author.mention}, we are finding **{user.display_name}**'s IP address <a:loadingloading:928828204632899644>")
            await asyncio.sleep(7)
            await msg.edit(f"{ctx.author.mention}, **{user.display_name}**'s IP address is {random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}")
def setup(bot):
    bot.add_cog(ip(bot))