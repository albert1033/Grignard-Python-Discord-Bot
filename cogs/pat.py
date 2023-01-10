import discord
from discord.ext import commands
import random

class Pat(commands.Cog):
    def __init__(self,bot):
        bot.client = bot
    @commands.command()
    async def Pat(self, ctx, user: discord.Member = None, *, Notes:str = None):
        Pat = ['https://c.tenor.com/E6fMkQRZBdIAAAAC/kanna-kamui-pat.gif',
        'https://c.tenor.com/wLqFGYigJuIAAAAC/mai-sakurajima.gif',
        'https://c.tenor.com/dmYhPDHbbI4AAAAM/misha-misha-necron-anos-voldigoad-the-misfit-of-demon-king-academy-headpat-pat.gif',
        'https://c.tenor.com/jEfC8cztigIAAAAM/anime-pat.gif',
        'https://c.tenor.com/OGnRVWCps7IAAAAC/anime-head-pat.gif',
        'https://c.tenor.com/N41zKEDABuUAAAAC/anime-head-pat-anime-pat.gif',
        'https://c.tenor.com/3PjRNS8paykAAAAC/pat-pat-head.gif',
        'https://c.tenor.com/DCMl9bvSDSwAAAAd/pat-head-gakuen-babysitters.gif',
        'https://c.tenor.com/f5asRSsfl-wAAAAC/good-boy-pat-on-head.gif',
        'https://c.tenor.com/dLdNYQrLsp4AAAAM/umaru-frown.gif',
        'https://c.tenor.com/w0dss_nCbsQAAAAC/nogamenolife.gif',
        'https://c.tenor.com/QAIyvivjoB4AAAAM/anime-anime-head-rub.gif',
        'https://c.tenor.com/lnoDyTqMk24AAAAC/anime-anime-headrub.gif',
        'https://c.tenor.com/RDfGm9ftwx0AAAAC/anime-pat.gif',
        'https://c.tenor.com/S3pfBHXIDYQAAAAC/ijiranaide-nagatoro-anime-pat.gif',
        'https://c.tenor.com/Y7B6npa9mXcAAAAC/rikka-head-pat-pat-on-head.gif',
        'https://c.tenor.com/Ls2uiad4RRUAAAAC/anime-anime-headpat.gif',
        'https://c.tenor.com/6dyxfdQx--AAAAAd/anime-senko-san.gif',
        'https://c.tenor.com/frXOu8zwFOoAAAAM/tsukiuta-anime.gif',
        'https://c.tenor.com/jKd455LtcpsAAAAC/anime-head-pat.gif']
        author = ctx.message.author.mention
        Pat2 = random.choice(Pat)
        if user != None and Notes != None:
            member = user.mention
            embed = discord.Embed(title = "Pat", description = author + " pats " + member + "! Note: " + Notes,
            color = discord.Color.teal())
            embed.set_image(url = Pat2)
            await ctx.reply(embed = embed)
        elif user != None and Notes is None:
            member = user.mention
            embed = discord.Embed(title = "Pat", description = author + " pats " + member + "!",
            color = discord.Color.teal())
            embed.set_image(url = Pat2)
            await ctx.reply(embed = embed)
        elif user == None and Notes == None:
            embed = discord.Embed(title = "Pat", description = author + " pats!",
            color = discord.Color.teal())
            embed.set_image(url = Pat2)
            await ctx.reply(embed = embed)
        else:
            embed = discord.Embed(title = "Pat", description = author + " pats" + Notes + "!",
            color = discord.Color.teal())
            embed.set_image(url = Pat2)
            await ctx.reply(embed = embed)

def setup(bot):
    bot.add_cog(Pat(bot))
