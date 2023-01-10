import discord
from discord.ext import commands
import random
from discord.ext.commands import MemberConverter

class gayrate(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command(aliases=['gayrate'])
    async def howgay(self,ctx, *, user:discord.Member = None):
        owner = ctx.author.id
        z = random.randint(0,100)
        a = random.randint(0,3)
        y = ctx.message.author.name
        albert = 767342472400994355
        kino = 798481497546817547
        apple = 844591475458965524
        if user is None:
            if owner == albert or owner == kino or owner == apple:
                embed = discord.Embed(title = y + "'s gayrate:", description = str(a) + "%", color = discord.Color.teal())
                embed.set_footer(text = "100% real")
                await ctx.reply(embed = embed)
            else:
                embed = discord.Embed(title = y + "'s gayrate", description = str(z) + "%", color = discord.Color.teal())
                embed.set_footer(text = "100% real")
                await ctx.reply(embed = embed)
        else:
            if user.id == albert or user.id == kino or user.id == apple:
                embed = discord.Embed(title = user.display_name + "'s gayrate:", description = str(a) + "%", color = discord.Color.teal())
                embed.set_footer(text = "100% real")
                await ctx.reply(embed = embed)
            else:
                embed = discord.Embed(title = user.display_name + "'s gayrate:", description = str(z) + "%", color = discord.Color.teal())
                embed.set_footer(text = "100% real")
                await ctx.reply(embed = embed)
def setup(bot):
    bot.add_cog(gayrate(bot))