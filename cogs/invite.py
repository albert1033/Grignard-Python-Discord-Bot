import discord
from discord.ext import commands
from discord.ui import Button, View
class invite(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def invite(self, ctx):
        embed=discord.Embed(title = "Invite", description="Click the link below to invite me to your server", color = discord.Color.teal())
        btn = Button(label="Invite", url="https://discord.com/api/oauth2/authorize?client_id=926752322929983550&permissions=519087975671&scope=bot%20applications.commands", emoji="<:give_name:942048925756583987>")
        view = View()
        view.add_item(btn)
        await ctx.reply(embed = embed, view = view)

def setup(bot):
    bot.add_cog(invite(bot))