import discord
from discord.ext import commands
import requests

class quote(commands.Cog):
	def __init__(self, bot):
		bot.client = bot
	@commands.command()
	async def quote(self, ctx):
		try:
			## making the get request
			response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
			if response.status_code == 200:
				## extracting the core data
				json_data = response.json()
				data = json_data['data']

				embed=discord.Embed(title="Quote", description=f"{data[0]['quoteText']}", color = discord.Color.teal())
				await ctx.reply(embed=embed)
			else:
				await ctx.reply("Error while getting quote")
		except:
			await ctx.reply("Something went wrong! Try Again!")
def setup(bot):
	bot.add_cog(quote(bot))