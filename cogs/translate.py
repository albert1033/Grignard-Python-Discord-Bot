import discord
from discord.ext import commands
from googletrans import Translator

class translate(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def translate(self, ctx,*,content):
        translator = Translator()
        translation = translator.translate(content)
        embed = discord.Embed(title = "Translate", description=f"**Request:** {translation.origin} ({translation.src}) \n **Translate:** {translation.text} ({translation.dest})", color = discord.Color.teal())
        await ctx.reply(embed = embed)

def setup(bot):
    bot.add_cog(translate(bot))