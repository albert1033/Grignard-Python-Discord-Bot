import discord
from discord.ext import commands
import random
from discord.ext.commands import MemberConverter

class simprate(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command(aliases=['simp', 'simprate'])
    async def howsimp(self,ctx, *, user:str = None):
        owner = ctx.author.id
        z = random.randint(0,100)
        y = ctx.message.author.name
        a = random.randint(0,3)
        albert = 767342472400994355
        kino = 798481497546817547
        apple = 844591475458965524
        if user is None:
            if owner == albert or owner == kino or owner == apple:
                embed = discord.Embed(title = y + "'s simprate:", description = str(a) + "%", color = discord.Color.teal())
                embed.set_footer(text = "100% real")
                await ctx.reply(embed = embed)
            else:
                embed = discord.Embed(title = y + "'s simprate", description = str(z) + "%", color = discord.Color.teal())
                embed.set_footer(text = "100% real")
                await ctx.reply(embed = embed)
        else:
            converter = MemberConverter()
            member2 = user.replace(">","")
            member3 = member2.replace("<@!", "")
            member = await converter.convert(ctx, member3)
            if user == '<@!767342472400994355>' or user == "<@!798481497546817547>" or user == "<@!844591475458965524>":
                embed = discord.Embed(title = str(member) + "'s simprate:", description = str(a) + "%", color = discord.Color.teal())
                embed.set_footer(text = "100% real")
                await ctx.reply(embed = embed)
            else:
                embed = discord.Embed(title = str(member) + "'s simprate:", description = str(z) + "%", color = discord.Color.teal())
                embed.set_footer(text = "100% real")
                await ctx.reply(embed = embed)
def setup(bot):
    bot.add_cog(simprate(bot))