import discord
from discord.ext import commands
import random

class kill(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def kill(self, ctx, user: discord.Member = None, *, Notes:str = None):
        kill = ['https://c.tenor.com/Ze50E1rW44UAAAAM/akudama-drive.gif',
        'https://c.tenor.com/Wq-Un4pZq50AAAAC/giant-scissor.gif',
        'https://c.tenor.com/bznBkYdhexcAAAAM/fire-arm-fire.gif',
        "https://c.tenor.com/f_Q2eibWWWcAAAAM/anime.gif",
        'https://c.tenor.com/HltbzNICQeAAAAAM/satsuki-kiryuin-kill-la-kill.gif',
        'https://c.tenor.com/6gghbFYRnqUAAAAM/rimuru-vs.gif',
        'https://c.tenor.com/Hp2BM9Q74zgAAAAd/smiley-anime-kill.gif',
        'https://c.tenor.com/SrJ8i0bWpOkAAAAC/arknights-w-anime.gif',
        'https://c.tenor.com/6525cG5E7oQAAAAd/anime-kill-kill.gif',
        'https://c.tenor.com/z5HVuzCiMWUAAAAd/angels-of-death-anime.gif',
        'https://c.tenor.com/Vk9HC22ya9MAAAAC/cyber-city-oedo808-anime.gif',
        'https://c.tenor.com/bBm44NlT4WwAAAAM/tokyo-ghoul.gif',
        'https://c.tenor.com/JBjznqwlUAYAAAAC/naruto-kakashi.gif',
        'https://c.tenor.com/5TtVl8vOeIEAAAAC/one-piece-luffy.gif',
        'https://c.tenor.com/9ieoIhppDisAAAAM/susanoo-akame-ga-kill.gif',
        'https://c.tenor.com/cc1EzfBVr4oAAAAC/yandere-tagged.gif',
        'https://c.tenor.com/V1htXlHhQoAAAAAC/akame-akame-of-demon-sword-murasame.gif',
        'https://c.tenor.com/XwlrL18IlDcAAAAC/tsumugu-kinagase-anime.gif',
        'https://c.tenor.com/Oi2zJc_rJ3MAAAAd/kill-la-kill-anime.gif',
        'https://c.tenor.com/-AQoYoFqY68AAAAM/ryuko-kill-la-kill.gif']
        author = ctx.message.author.mention
        kill2 = random.choice(kill)
        if user != None and Notes != None:
            member = user.mention
            embed = discord.Embed(title = "kill", description = author + " kills " + member + "! Note: " + Notes,
            color = discord.Color.teal())
            embed.set_image(url = kill2)
            await ctx.reply(embed = embed)
        elif user != None and Notes is None:
            member = user.mention
            embed = discord.Embed(title = "kill", description = author + " kills " + member + "!",
            color = discord.Color.teal())
            embed.set_image(url = kill2)
            await ctx.reply(embed = embed)
        elif user == None and Notes == None:
            embed = discord.Embed(title = "kill", description = author + " kills!",
            color = discord.Color.teal())
            embed.set_image(url = kill2)
            await ctx.reply(embed = embed)
        else:
            embed = discord.Embed(title = "Kill", description = author + " kills" + Notes + "!",
            color = discord.Color.teal())
            embed.set_image(url = kill2)
            await ctx.reply(embed = embed)
def setup(bot):
    bot.add_cog(kill(bot))