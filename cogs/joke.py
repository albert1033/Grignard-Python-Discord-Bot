import discord
from discord.ext import commands
import pyjokes

class joke(commands.Cog):
	def __init__(self, bot):
		bot.client = bot
	@commands.command()
	async def joke(self, ctx):
		joke= pyjokes.get_joke(language="en", category='neutral')
		embed=discord.Embed(title=f"{ctx.author.name}'s joke request", description=f"**Joke:** {joke}",
			color=discord.Color.teal())
		await ctx.reply(embed=embed)
def setup(bot):
	bot.add_cog(joke(bot))