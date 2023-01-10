import discord
from discord.ext import commands
import random
from discord.ext.commands import MemberConverter

class Brain(commands.Cog):
    def __init__(self,bot):
        bot.client = bot
    @commands.command(aliases=['brainsize'])
    async def brain(self,ctx, user:discord.Member = None):
        owner = ctx.author.id
        z = random.randint(0,12)
        y = ctx.message.author.name
        albert = 767342472400994355
        kino = 798481497546817547
        apple = 844591475458965524
        color = discord.Color.teal()
        if user is None:
            if owner == albert or owner == kino or owner == apple:
              embed = discord.Embed(title = y + "'s brain:", description = "100% real 🧠", color = color)
              embed.set_image(url = "https://cdn.discordapp.com/attachments/893888180439367833/927214605460209744/brain2__1_-removebg-preview.png")
              embed.set_footer(text = "Big brain")
              await ctx.reply(embed = embed)
            else:
              if z <= 3:
                embed = discord.Embed(title = y + "'s brain:'", description = "100% real 🧠 \n" + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", color = color)
                embed.set_footer(text = "No brain")
                await ctx.reply(embed = embed)
              elif z <= 6:
                embed = discord.Embed(title = y+"'s brain:", description = "100% real 🧠", color = color)
                embed.set_image(url = "https://cdn.discordapp.com/attachments/893888180439367833/927214605896384532/brain-removebg-preview.png")
                embed.set_footer(text = "Small brain")
                await ctx.reply(embed = embed)
              elif z <= 9:
                embed = discord.Embed(title = y + "'s brain", description = "100% real 🧠", color = color)
                embed.set_image(url = "https://cdn.discordapp.com/attachments/893888180439367833/927214605690892288/brain2-removebg-preview.png")
                embed.set_footer(text = "Medium brain")
                await ctx.reply(embed = embed)
              else:
                embed = discord.Embed(title = y + "'s brain", description = "100% real 🧠", color = color)
                embed.set_image(url = "https://cdn.discordapp.com/attachments/893888180439367833/927214605460209744/brain2__1_-removebg-preview.png")
                embed.set_footer(text = "Big brain")
                await ctx.reply(embed = embed)
        else:
          if user.id == albert or user.id == kino or user.id == apple:
            embed = discord.Embed(title = user.display_name + "'s brain:", description = "100% real 🧠", color = color)
            embed.set_image(url = "https://cdn.discordapp.com/attachments/893888180439367833/927214605460209744/brain2__1_-removebg-preview.png")
            embed.set_footer(text = "Big brain")
            await ctx.reply(embed = embed)
          else:
              if z <= 3:
                embed = discord.Embed(title = user.display_name  + "'s brain:'", description = "100% real 🧠 \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", color = color)
                embed.set_footer(text = "No brain")
                await ctx.reply(embed = embed)
              elif z <= 6:
                embed = discord.Embed(title = user.display_name  +"'s brain:", description = "100% real 🧠", color = color)
                embed.set_image(url = "https://cdn.discordapp.com/attachments/893888180439367833/927214605896384532/brain-removebg-preview.png")
                embed.set_footer(text = "Small brain")
                await ctx.reply(embed = embed)
              elif z <= 9:
                embed = discord.Embed(title = user.display_name  + "'s brain", description = "100% real 🧠", color = color)
                embed.set_image(url = "https://cdn.discordapp.com/attachments/893888180439367833/927214605690892288/brain2-removebg-preview.png")
                embed.set_footer(text = "Medium brain")
                await ctx.reply(embed = embed)
              else:
                embed = discord.Embed(title = user.display_name  + "'s brain", description = "100% real 🧠", color = color)
                embed.set_image(url = "https://cdn.discordapp.com/attachments/893888180439367833/927214605460209744/brain2__1_-removebg-preview.png")
                embed.set_footer(text = "Big brain")
                await ctx.reply(embed = embed)
def setup(bot):
    bot.add_cog(Brain(bot))
