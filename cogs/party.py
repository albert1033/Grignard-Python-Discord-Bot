import discord 
from discord.ext import commands
import random
from discord.ui import Button, View
import asyncio

class party(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def party(self, ctx):
        abc = ['He/she brought pizza!',
        "Let's dance!!!",
        "He/she will be the DJ!",
        "I hope his/her mom won't call her to go home soon.",
        "Let's drink beer!",
        "The party's owner has opened the wine!",
        'What will he do?',
        "I hope you remember to bring your wallet."]
        button = Button(label= "Join the party!", style=discord.ButtonStyle.blurple, emoji="🍻")
        view = View()
        view.add_item(button)
        async def button_callback(interaction):
            await interaction.response.send_message(f"**{interaction.user}** has joined the party! {random.choice(abc)}")
        button.callback = button_callback
        button2 = Button(label= "Join the party!", style=discord.ButtonStyle.blurple, emoji="🍻", disabled=True)
        view2 = View()
        view2.add_item(button2)
        embed = discord.Embed(title=f"{ctx.author.name} has opened a party!", description="Click the button below to join", color=discord.Color.teal())
        msg = await ctx.send(embed = embed, view = view)
        await asyncio.sleep(20)
        await msg.edit(embed = embed, view = view2)
        await ctx.send("**The really fun party has ended**")
        
def setup(bot):
    bot.add_cog(party(bot))