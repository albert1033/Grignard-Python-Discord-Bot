import discord
from discord.ext import commands

class owner(commands.Cog):
    def __init__(self, bot):
        self.client = bot
    @commands.command()
    async def owner(self, ctx):
        embed = discord.Embed(title = f"{self.client.user.name} bot's owner", 
        description=f"Name: albert.#1033 \n Age: ||Under 18|| \n Description: I'm just a normal person who love making bot but don't want to make too many friends. Enjoy using {self.client.user.name}!",
        color = discord.Color.teal())
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        embed.set_image(url = "https://data.whicdn.com/images/350565090/original.jpg")
        await ctx.reply(embed = embed)
def setup(bot):
    bot.add_cog(owner(bot))