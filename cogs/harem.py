import discord
from discord.ext import commands
import random

class harem(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def harem(self, ctx, *, user:discord.Member = None):
        big = ['https://c.tenor.com/q1-HPf4e0XgAAAAC/pokemon-brock.gif',
        'https://c.tenor.com/dm6I5qc0YkQAAAAC/love-live-school-idol-project.gif',
        'https://c.tenor.com/8ArYEPt2JEgAAAAC/anime-harem.gif',
        'https://c.tenor.com/NvPab8QIaxIAAAAC/tsukihime-carnival-phantasm.gif',
        'https://c.tenor.com/TF_DxCjOLtIAAAAM/konosuba-anime.gif',
        'https://c.tenor.com/lFXm1cT_TxQAAAAC/gary-oak.gif']
        small = ['https://c.tenor.com/1d-uUlF5A2QAAAAM/maoyu-yuusha.gif',
        'https://c.tenor.com/uZaD_MRmlPQAAAAM/anime-harem.gif',
        'https://c.tenor.com/rCtKKJuiPaIAAAAC/anime.gif']
        gf = ['https://c.tenor.com/2xe_jm5Nvz4AAAAC/anime-hug.gif',
        'https://c.tenor.com/OY5wf5rjslYAAAAC/anime-cute.gif',
        'https://c.tenor.com/ph8pDcpFld0AAAAC/asuna-yuuki.gif',
        ]
        z = random.randint(0,3)
        if user is None:
            if z == 0:
                description = "You have no girlfriend"
                url = "https://c.tenor.com/PMolRwrILIIAAAAC/no-girlfriend-jutsu-jutsu.gif"
            if z == 1:
                description = "You have 1 girlfriend"
                url = random.choice(gf)
            if z == 2:
                description = "You have a small harem, but good luck!"
                url = random.choice(small)
            if z == 3:
                description = "You have a big harem, congratz. Remember not to make your girls disappointed"
                url = random.choice(big)
            embed = discord.Embed(title=f"{ctx.author.name}'s harem", description = description, color= discord.Color.teal())
            embed.set_image(url = url)
            await ctx.reply(embed = embed)
        else:
            if z == 0:
                description = "You have no girlfriend"
                url = "https://c.tenor.com/PMolRwrILIIAAAAC/no-girlfriend-jutsu-jutsu.gif"
            if z == 1:
                description = "You have 1 girlfriend"
                url = random.choice(gf)
            if z == 2:
                description = "You have a small harem, but good luck!"
                url = random.choice(small)
            if z == 3:
                description = "You have a big harem, congratz. Remember not to make your girls disappointed"
                url = random.choice(big)
            embed = discord.Embed(title=f"{user.display_name}'s harem", description = description, color=discord.Color.teal())
            embed.set_image(url = url)
            await ctx.reply(embed = embed)
def setup(bot):
    bot.add_cog(harem(bot))