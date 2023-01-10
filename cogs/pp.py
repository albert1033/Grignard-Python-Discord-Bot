import discord
from discord.ext import commands
import random
from discord.ext.commands import MemberConverter

class pp(commands.Cog):
    def __init__(self,bot):
        bot.client = bot
    @commands.command()
    async def pp(self,ctx, *, member:discord.Member = None):
        dauser = ctx.author.id
        W = random.randint(1, 9)
        z = random.randint(8, 14)
        albert = 767342472400994355
        kino = 798481497546817547
        silent = 718417101844512859
        if member is None:
          y = ctx.author.name
          if dauser == kino or dauser == albert:
            pp = f"8{'='*z}D"
            color =discord.Color.teal()
            footer = "big boi pp"

          elif dauser == silent or random.randint(0, 5) == 1:
            pp = "8=D"
            color = 0xff0000
            footer = "LMFAOA"

          else:
            pp = f"8{'='*W}D"
            color = discord.Color.teal()
            footer = "ah yes"
          embed = discord.Embed(title= y + "'s pp", description=pp, color=color)
          embed.set_footer(text=footer)
          await ctx.reply(embed=embed)

        else:
          if member.id == kino or member.id == albert:
            pp = f"8{'='*z}D"
            color =discord.Color.teal()
            footer = "big boi pp"

          elif random.randint(0, 5) == 1:
            pp = "8==D"
            color = 0xff0000
            footer = "rip"

          else:
            pp = f"8{'='*W}D"
            color = discord.Color.teal()
            footer = "cool"

          mbed = discord.Embed(title = member.display_name + "'s pp", description = pp, color=0xa381a7)
          mbed.set_footer(text=footer)
          await ctx.reply(embed=mbed)
def setup(bot):
    bot.add_cog(pp(bot))
