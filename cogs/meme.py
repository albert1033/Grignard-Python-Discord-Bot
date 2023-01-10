import discord
from discord.ext import commands
import aiohttp
class Meme(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command(aliases = ['meme'])
    async def memes(self,ctx):
        async with aiohttp.ClientSession() as session:
          url = "https://meme-api.herokuapp.com/gimme"
          async with session.get(url) as response:
            response = await response.json()
            embed = discord.Embed(
              title= response['title'],
              url = response['postLink'],
              color = discord.Color.teal(),
            )
            embed.set_image(url=response['url'])
            embed.set_footer(text=f"r/{response['subreddit']} | Requested by {ctx.author.name} | Enjoy your memes!")
            await ctx.reply(embed=embed)
def setup(bot):
  bot.add_cog(Meme(bot))
