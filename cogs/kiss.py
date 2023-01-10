import discord
from discord.ext import commands
import random
class kiss(commands.Cog):
    def __init__(self,bot):
        bot.client = bot
    @commands.command()
    async def kiss(self, ctx, user: discord.Member = None, *, Notes:str = None):
        kiss = ["https://c.tenor.com/wDYWzpOTKgQAAAAC/anime-kiss.gif",
        "https://c.tenor.com/TWbZjCy8iN4AAAAC/girl-anime.gif",
        "https://c.tenor.com/V0nBQduEYb8AAAAC/anime-kiss-making-out.gif",
        "https://c.tenor.com/03wlqWILqpEAAAAM/highschool-dxd-asia.gif",
        "https://c.tenor.com/4ofp_xCUBxcAAAAM/eden-of-the-east-akira-takizawa.gif",
        "https://c.tenor.com/9vycr5sUYBMAAAAC/eden-of-the-east-anime.gif",
        "https://c.tenor.com/IvfI1mCRtRoAAAAC/anime-kiss-love.gif",
        "https://c.tenor.com/etSTc3aWspcAAAAC/yuri-kiss.gif",
        "https://c.tenor.com/WxITy4XYFVUAAAAC/kiss-yuri.gif",
        "https://c.tenor.com/3NCLnc_FaQAAAAAC/kirito-asuna.gif",
        "https://c.tenor.com/YTsHLAJdOT4AAAAC/anime-kiss.gif",
        "https://c.tenor.com/VxNAxTOeT3YAAAAM/anime-kiss.gif",
        "https://c.tenor.com/Hcvab1NgNdkAAAAM/kiss-anime.gif",
        "https://c.tenor.com/hc2ZCXLcH5AAAAAC/hakuoki-hakuouki.gif",
        "https://c.tenor.com/JhgpAnpzd8UAAAAd/kiss-anime.gif",
        "https://c.tenor.com/-wQWOYZbtqQAAAAM/anime-kissing.gif",
        "https://c.tenor.com/_QYEmI3cT2wAAAAC/kiss-kissing.gif",
        "https://c.tenor.com/DH5tnIbT9qgAAAAC/love-tyrant-kiss.gif",
        "https://c.tenor.com/PJdw6qCLD1MAAAAM/issei-akeno.gif",
        "https://c.tenor.com/zu78lSJzp6sAAAAM/anime-kiss.gif",]
        author = ctx.message.author.mention
        kiss2 = random.choice(kiss)
        if user != None and Notes != None:
            member = user.mention
            embed = discord.Embed(title = "Kiss", description = author + " kisses " + member + "! Note: " + Notes,
            color = discord.Color.teal())
            embed.set_image(url = kiss2)
            await ctx.reply(embed = embed)
        elif user != None and Notes is None:
            member = user.mention
            embed = discord.Embed(title = "Kiss", description = author + " kisses " + member + "!",
            color = discord.Color.teal())
            embed.set_image(url = kiss2)
            await ctx.reply(embed = embed)
        elif user == None and Notes == None:
            embed = discord.Embed(title = "Kiss", description = author + " kisses!",
            color = discord.Color.teal())
            embed.set_image(url = kiss2)
            await ctx.reply(embed = embed)
        else:
            embed = discord.Embed(title = "Kiss", description = author + " kissess" + Notes + "!",
            color = discord.Color.teal())
            embed.set_image(url = kiss2)
            await ctx.reply(embed = embed)

def setup(bot):
    bot.add_cog(kiss(bot))