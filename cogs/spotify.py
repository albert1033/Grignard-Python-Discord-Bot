import discord
from discord import Spotify
from discord.ext import commands

class spotify(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def spotify(self, ctx, *, user:discord.Member=None):
        if user is None:
            user = ctx.author
        if user.activities:
            for activity in user.activities:
                if isinstance(activity, Spotify):
                    embed = discord.Embed(title=f"{activity.title}", color = activity.color, url=activity.track_url)
                    embed.set_author(name = "Spotify Track Information", icon_url="https://cdn.discordapp.com/emojis/585766969144508416.webp?size=96&quality=lossless")
                    embed.add_field(name="Name", value=f"```{activity.title}```", inline=True)
                    embed.add_field(name="Artists", value=f"```{str(activity.artists) if len(activity.artists) > 1 else activity.artist}```", inline=True)
                    embed.add_field(name="Album", value=f"```{activity.album}```", inline=True)
                    embed.add_field(name="URL", value=f"```{activity.track_url}```", inline=False)
                    embed.set_thumbnail(url=f"{activity.album_cover_url}")
                    embed.set_footer(text=f"{user.display_name}'s Current Track", icon_url=user.display_avatar.url)
                    await ctx.reply(embed=embed)
                else:
                    embed = discord.Embed(title="Error!", description="<:abccross:940404011104874518> This user is not listening to Spotify. If they are setting a status message, turn it off because that will stop me reaching your Spotify data ??", color = discord.Color.red())
                    await ctx.reply(embed=embed)
                return
        else:
            embed = discord.Embed(title="Error!", description="<:abccross:940404011104874518> This user is not doing anything", color = discord.Color.red())
            await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(spotify(bot))