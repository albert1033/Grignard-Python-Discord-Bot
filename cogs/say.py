import discord
from discord.ext import commands

class say(commands.Cog):
	def __init__(self, bot):
		bot.client=bot
	@commands.command()
	async def say(self, ctx, *, content):
		allowed_mentions = discord.AllowedMentions(everyone=False, roles=False) 
		try:
		    await ctx.message.delete()
		except Exception:
			pass
		await ctx.send(content, allowed_mentions=allowed_mentions)
def setup(bot):
	bot.add_cog(say(bot))