from discord.ext import commands
import aiohttp
import discord
import re

class AddEmoji(commands.Cog):
    def __init__(self, bot):
        bot.client = bot

    @commands.command()
    @commands.has_permissions(manage_emojis=True)
    async def addemoji(self, ctx, emoji: discord.Emoji,*, name=None):
        #asset = emoji.url()
        if not name:
            name = emoji.name
        emoji = await ctx.guild.create_custom_emoji(image=await emoji.read(), name=name)
        await ctx.send(f"Emoji <:{emoji.name}:{emoji.id}> was added!")

    @addemoji.error
    async def addemoji_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(title="Error", description="Please give us a valid emoji", color=discord.Color.red())
            await ctx.send(embed = embed)
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description="Please give us an emoji", color=discord.Color.red())
            await ctx.send(embed = embed)
            return
        raise error
        
def setup(bot):
    bot.add_cog(AddEmoji(bot))