import discord
from discord.ext import commands
import loremipsum
import random
class textwall(commands.Cog):
	def __init__(self, bot):
		bot.client=bot
	@commands.command()
	async def textwall(self, ctx):
		ee = random.randint(1, 4)
		nvm = loremipsum.generate(ee)
		embed = discord.Embed(title="Textwall", description=nvm, color=discord.Color.teal())
		embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar.url)
		await ctx.reply(embed=embed)

def setup(bot):
	bot.add_cog(textwall(bot))