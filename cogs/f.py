import discord
from discord.ext import commands
from discord.ui import Button, View
import asyncio


class MyView(View):
    @discord.ui.button(style=discord.ButtonStyle.gray, disabled=False, emoji="🇫")
    async def button_callback(self, button, interaction):
            await interaction.response.send_message(f"**{interaction.user}** has paid their respect!")

    
class f(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def f(self, ctx):
        embed = discord.Embed(title = "F in the chat", description="Press F to give respect", color = discord.Color.teal())
        view = MyView()
        button = Button(style = discord.ButtonStyle.gray, disabled= True, emoji="🇫")
        view2 = View()
        view2.add_item(button)
        message = await ctx.reply(embed = embed, view = view)
        await asyncio.sleep(10)
        await message.edit(embed = embed, view = view2)
        await ctx.send("**Respect paid, mission passed**")

def setup(bot):
    bot.add_cog(f(bot))

