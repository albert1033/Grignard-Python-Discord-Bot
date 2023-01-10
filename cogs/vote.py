import discord 
from discord.ext import commands
from discord.ui import Button, View
class vote(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def vote(self, ctx):
        top = Button(label="Top.gg", url="https://top.gg/bot/926752322929983550/vote", emoji="<:topgg:941275682024067112>")
        vcodes = Button(label = "vCodes.xyz", url = "https://vcodes.xyz/bot/926752322929983550/vote", emoji="<:vcodes:941276326604718120>")
        embed = discord.Embed(title = "Vote", description="Please vote for us! Thank you very much for voting! ❤️", color=discord.Color.purple())
        view = View()
        view.add_item(top)
        view.add_item(vcodes)
        await ctx.reply(embed = embed, view = view)
def setup(bot):
    bot.add_cog(vote(bot))