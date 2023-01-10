import discord
from animec import *
from discord.ext import commands

class anime(commands.Cog):
    def __init__(self, bot):
        bot.client = bot 

    @commands.command(aliases = ['animeinfo', 'searchanime'])
    async def anime(self, ctx,*,query):
        try:
            anime = Anime(query)
        except:
            mbed = discord.Embed(Title = 'No corresponding anime can be found!', description="Please check the name of the anime you're searching for and try again.", color = discord.Color.red())
            await ctx.reply(embed = mbed)
            return
        if anime.is_nsfw() is True:
            embed=discord.Embed(title="Nooooo", description="I won't let you search NSFW anime!", color = discord.Color.red())
            embed.set_footer(text=f"Guys wtf {ctx.author.name} just searched for a nsfw anime")
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title=f'{anime.name}',url=anime.url, color = discord.Color.teal())
            embed.add_field(name='- Basic Info -:',value = f"**English Name :** *{str(anime.title_english)}* \n**Japanese Name: ** *{str(anime.title_jp)}*", inline=False)
            embed.add_field(name='- Summary -', value=f"{anime.description[:1000]}...")
            embed.add_field(name='- Other Info -:', value = f'**Status: **{str(anime.status)}\n**Episodes: **{str(anime.episodes)}\n**Rating: **{str(anime.rating)}\n**Type: **{str(anime.type)}\n**Ranked:** {str(anime.ranked)}\n **NSFW Status: **{str(anime.is_nsfw())}\n**Genres: **{str(anime.genres)}\n**Ranked: **{str(anime.ranked)}\n**Aired: **{str(anime.aired)}\n**Favourite: **{str(anime.favorites)}', inline=False)

            embed.set_thumbnail(url = anime.poster)
            embed.set_footer(icon_url=ctx.author.avatar.url, text = f'Requested by {ctx.author.name}')
            await ctx.reply(embed = embed)


def setup(bot):
    bot.add_cog(anime(bot))
