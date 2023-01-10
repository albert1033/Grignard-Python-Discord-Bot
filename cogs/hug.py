import discord
from discord.ext import commands
import random

class hug(commands.Cog):
    def __init__(self,bot):
        bot.client = bot
    @commands.command()
    async def hug(self, ctx, user: discord.Member = None, *, Notes:str = None):
        hug = ['https://c.tenor.com/xgVPw2QK5n8AAAAC/sakura-quest-anime.gif',
        'https://c.tenor.com/rQ2QQQ9Wu_MAAAAC/anime-cute.gif',
        'https://c.tenor.com/9e1aE_xBLCsAAAAC/anime-hug.gif',
        'https://c.tenor.com/UhcyGsGpLNIAAAAC/hug-anime.gif',
        'https://c.tenor.com/pcULC09CfkgAAAAC/hug-anime.gif',
        'https://c.tenor.com/kPgR6UH6AXcAAAAC/anime-hug.gif',
        'https://c.tenor.com/0PIj7XctFr4AAAAC/a-whisker-away-hug.gif',
        'https://c.tenor.com/jQ0FcfbsXqIAAAAC/hug-anime.gif',
        'https://c.tenor.com/xIuXbMtA38sAAAAd/toilet-bound-hanakokun.gif',
        'https://c.tenor.com/83QLplerW8sAAAAC/anime-hug.gif',
        'https://c.tenor.com/qF7mO4nnL0sAAAAC/abra%C3%A7o-hug.gif',
        'https://c.tenor.com/ixaDEFhZJSsAAAAC/anime-choke.gif',
        'https://c.tenor.com/GJ6oX6r0mZsAAAAC/chuunibyou-anime.gif',
        'https://c.tenor.com/RRmtObXpOegAAAAC/anime-hug.gif',
        'https://c.tenor.com/jDJlRRFUge4AAAAC/anime-cute.gif',
        'https://c.tenor.com/_OamUWxaZd0AAAAC/love-i-love-you.gif',
        'https://c.tenor.com/Ge4DoX5aDD0AAAAC/love-kiss.gif',
        'https://c.tenor.com/1aQeiWOHmuMAAAAC/hug-anime.gif',
        'https://c.tenor.com/PeYQKzkX2WwAAAAC/anime-hug.gif',
        'https://c.tenor.com/JjQJUIu6K0QAAAAC/cute-hug.gif']
        author = ctx.message.author.mention
        hug2 = random.choice(hug)
        if user != None and Notes != None:
            member = user.mention
            embed = discord.Embed(title = "Hug", description = author + " hugs " + member + "! Note: " + Notes,
            color = discord.Color.teal())
            embed.set_image(url = hug2)
            await ctx.reply(embed = embed)
        elif user != None and Notes is None:
            member = user.mention
            embed = discord.Embed(title = "Hug", description = author + " hugs " + member + "!",
            color = discord.Color.teal())
            embed.set_image(url = hug2)
            await ctx.reply(embed = embed)
        elif user == None and Notes == None:
            embed = discord.Embed(title = "Hug", description = author + " hugs!",
            color = discord.Color.teal())
            embed.set_image(url = hug2)
            await ctx.reply(embed = embed)
        else:
            embed = discord.Embed(title = "Hug", description = author + " hugs" + Notes + "!",
            color = discord.Color.teal())
            embed.set_image(url = hug2)
            await ctx.reply(embed = embed)

def setup(bot):
    bot.add_cog(hug(bot))
