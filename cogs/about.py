import discord
from discord.ext import commands

class about(commands.Cog):
    def __init__(self, bot):
        self.client = bot
    @commands.command()
    async def about(self, ctx):
        embed = discord.Embed(title = f"{self.client.user.name} bot's information", 
        description="Creator: ||albert.#1033|| \n Category: **fun**, **random**, **utility**", color= discord.Color.teal())
        embed.set_footer(text=f"Have fun! | Requested by {ctx.author.name}")
        embed.set_image(url = "https://images-ext-2.discordapp.net/external/Rtv6uueCyruVbWbm-EUQy0EOLYB0gsru_-oSswDqxsE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/767342472400994355/5d443c17cb35152dea125ac1bae7e092.png")
        await ctx.reply(embed = embed)
def setup(bot):
    bot.add_cog(about(bot))