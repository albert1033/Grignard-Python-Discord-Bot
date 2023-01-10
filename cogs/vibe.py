import discord
from discord.ext import commands
import random
class vibe(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command(aliases = ['dance'])
    async def vibe(self, ctx, user: discord.Member = None, *, Notes:str = None):
        vibe = ['https://c.tenor.com/LCpcrdtI0GYAAAAM/vibing-st6.gif',
        'https://c.tenor.com/TMFZeFRR-eQAAAAd/vibing-cat.gif',
        'https://c.tenor.com/iSVDwxuQUKsAAAAd/vibing-cat-vibing.gif',
        "https://c.tenor.com/6R6Xok1bVKQAAAAd/cat-vibeing.gif",
        'https://c.tenor.com/OxvEqKx7_ScAAAAM/jig-dance.gif',
        'https://c.tenor.com/qNyX3aivxDIAAAAd/rick-ross.gif',
        'https://c.tenor.com/2JXLM-ab0McAAAAd/rick-and-morty-fortnite.gif',
        'https://c.tenor.com/n1oq1EFNSwEAAAAM/dance-weekend-vibe.gif',
        'https://c.tenor.com/y_NLohYyZ6EAAAAC/playit-chuckberrystyle.gif',
        'https://c.tenor.com/s8PpYKZ0OPwAAAAC/snoop-dogg-dance.gif',
        'https://c.tenor.com/DkJRx7VXXSkAAAAM/girl-dancing-woman-dancing.gif',
        'https://c.tenor.com/DCgGhzPjCqgAAAAM/chika-dance.gif',
        'https://c.tenor.com/76sUEuWYpscAAAAC/vibe-dont.gif',
        'https://c.tenor.com/y9wCPf0zWTgAAAAM/tobi-naruto.gif',
        'https://c.tenor.com/TCxulrEkOjwAAAAM/soulection-family.gif',]
        author = ctx.message.author.mention
        vibe2 = random.choice(vibe)
        if user != None and Notes != None:
            member = user.mention
            embed = discord.Embed(title = "Vibe", description = author + " vibes with" + member + "! Note: " + Notes,
            color = discord.Color.teal())
            embed.set_image(url = vibe2)
            await ctx.reply(embed = embed)
        elif user != None and Notes is None:
            member = user.mention
            embed = discord.Embed(title = "Vibe", description = author + " vibes with" + member + "!",
            color = discord.Color.teal())
            embed.set_image(url = vibe2)
            await ctx.reply(embed = embed)
        elif user == None and Notes == None:
            embed = discord.Embed(title = "Vibe", description = author + " vibes!",
            color = discord.Color.teal())
            embed.set_image(url = vibe2)
            await ctx.reply(embed = embed)
        else:
            embed = discord.Embed(title = "Vibe", description = author + " vibes with" + Notes + "!",
            color = discord.Color.teal())
            embed.set_image(url = vibe2)
            await ctx.reply(embed = embed)
def setup(bot):
    bot.add_cog(vibe(bot))