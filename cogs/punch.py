import discord
from discord.ext import commands
import random

class punch(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def punch(self, ctx, user: discord.Member = None, *, Notes:str = None):
        punch = ['https://c.tenor.com/UH8Jnl1W3CYAAAAC/anime-punch-anime.gif',
        'https://c.tenor.com/SwMgGqBirvcAAAAC/saki-saki-kanojo-mo-kanojo.gif',
        'https://c.tenor.com/BoYBoopIkBcAAAAC/anime-smash.gif',
        "https://c.tenor.com/hs6GB44v8aQAAAAM/one-punch-man-%E3%83%AF%E3%83%B3%E3%83%91%E3%83%B3%E3%83%9E%E3%83%B3.gif",
        'https://c.tenor.com/YGKPpkNN6g0AAAAM/anime-jujutsu-kaisen-anime-punch.gif',
        'https://c.tenor.com/6a42QlkVsCEAAAAd/anime-punch.gif',
        'https://c.tenor.com/aEX1wE-WrEMAAAAC/anime-right-in-the-stomach.gif',
        'https://c.tenor.com/xWqmJMePsqEAAAAM/weaboo-otaku.gif',
        'https://c.tenor.com/EdV_frZ4e_QAAAAC/anime-naruto.gif',
        'https://c.tenor.com/3CUBZHrDUvUAAAAC/punch-combo.gif',
        'https://c.tenor.com/ObgxhbfdVCAAAAAd/luffy-anime.gif',
        'https://c.tenor.com/o8RbiF5-9dYAAAAM/killua-hxh.gif',
        'https://c.tenor.com/l_zcD2qX5M4AAAAM/double-punch-anime-double-punch.gif',
        'https://c.tenor.com/TrIZGVo5GV0AAAAC/meliodas-seven-deadly-sins-anime.gif',
        'https://c.tenor.com/5Ry4AVOgod4AAAAC/bear-fight.gif',
        'https://c.tenor.com/Ka8eQ8D7yVwAAAAC/anime-super-punch.gif',
        'https://c.tenor.com/3TvlgppifSMAAAAC/anime-girls.gif',
        'https://c.tenor.com/BESYHOr_4uIAAAAM/v9-fight.gif',
        'https://c.tenor.com/bWv7Av9UOMkAAAAC/relationship-anime.gif',
        'https://c.tenor.com/OYv6aDua76wAAAAM/hanagaki-takemichi-takemichi.gif']
        author = ctx.message.author.mention
        punch2 = random.choice(punch)
        if user != None and Notes != None:
            member = user.mention
            embed = discord.Embed(title = "punch", description = author + " punches " + member + "! Note: " + Notes,
            color = discord.Color.teal())
            embed.set_image(url = punch2)
            await ctx.reply(embed = embed)
        elif user != None and Notes is None:
            member = user.mention
            embed = discord.Embed(title = "punch", description = author + " punches " + member + "!",
            color = discord.Color.teal())
            embed.set_image(url = punch2)
            await ctx.reply(embed = embed)
        elif user == None and Notes == None:
            embed = discord.Embed(title = "punch", description = author + " punches!",
            color = discord.Color.teal())
            embed.set_image(url = punch2)
            await ctx.reply(embed = embed)
        else:
            embed = discord.Embed(title = "Punch", description = author + " punches" + Notes + "!",
            color = discord.Color.teal())
            embed.set_image(url = punch2)
            await ctx.reply(embed = embed)
def setup(bot):
    bot.add_cog(punch(bot))