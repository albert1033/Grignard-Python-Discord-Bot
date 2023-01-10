from discord.ext import commands
import discord
import json
import aiohttp
import random

class laugh(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command(aliases = ['smile'])
    async def laugh(self, ctx, user: discord.Member = None, *, Notes:str = None):
        embed = discord.Embed(title= f"Smile", color=discord.Colour.random())
        session = aiohttp.ClientSession()
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + "anime+laugh" + '&api_key=bEzT2KtucyvhQxuEtQVk3y7LCenZnz1G&limit=10')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        url=data['data'][gif_choice]['images']['original']['url']
        author = ctx.message.author.mention
        if user != None and Notes != None:
            member = user.mention
            embed = discord.Embed(title = "Laugh", description = author + " laughes at " + member + "! Note: " + Notes,
            color = discord.Color.teal())
            embed.set_image(url = url)
            await ctx.reply(embed = embed)
        elif user != None and Notes is None:
            member = user.mention
            embed = discord.Embed(title = "Laugh", description = author + " laughes at " + member + "!",
            color = discord.Color.teal())
            embed.set_image(url = url)
            await ctx.reply(embed = embed)
        elif user == None and Notes == None:
            embed = discord.Embed(title = "Laugh", description = author + " laughes!",
            color = discord.Color.teal())
            embed.set_image(url = url)
            await ctx.reply(embed = embed)
        else:
            embed = discord.Embed(title = "Laugh", description = author + " laughes" + Notes + "!",
            color = discord.Color.teal())
            embed.set_image(url = url)
            await ctx.reply(embed = embed)
        await session.close()

def setup(bot):
    bot.add_cog(laugh(bot))