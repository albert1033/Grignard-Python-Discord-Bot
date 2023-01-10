import discord
from discord.ext import commands

class avatar(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command(aliases = ['av'])
    async def avatar(self, ctx, *, user:discord.Member = None):
        if user is None:
            user = ctx.author
        embed = discord.Embed(title= f"{user.display_name}'s avatar", color = discord.Color.teal())
        embed.set_image(url= user.display_avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)
def setup(bot):
    bot.add_cog(avatar(bot))
        