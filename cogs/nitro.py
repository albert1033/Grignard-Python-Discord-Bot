import discord
from discord.ext import commands
from discord.ui import Button, View

class nitro(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    
    @commands.command()
    async def nitro(self, ctx):
        embed = discord.Embed(title = "You've been gifted a subscription!", description="You've been gifted Nitro for **1 Month!**\nExpires in **24 hours**", color = 0x36393f)
        button = Button(style=discord.ButtonStyle.green, label = "Claim") 
        view = View() 
        view.add_item(button)
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/L5DOV7R8cjH5P8niHjsXeMCQM6xuIbGgtZeTujtJYjM/https/media.discordapp.net/attachments/895163964361674752/895982514093555763/images_1_-_2021-10-08T160355.540.jpeg")
        async def button_callback(interaction):
            await interaction.response.edit_message(content = "https://images-ext-1.discordapp.net/external/AoV9l5YhsWBj92gcKGkzyJAAXoYpGiN6BdtfzM-00SU/https/i.imgur.com/NQinKJB.mp4", view = None, embed = None)
        button.callback = button_callback
        await ctx.send(embed = embed, view = view)
def setup(bot):
    bot.add_cog(nitro(bot))