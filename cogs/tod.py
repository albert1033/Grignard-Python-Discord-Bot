import discord 
from discord.ext import commands 
from discord.ui import Button, View, view
import random

class tod(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command(aliases =['truthordare'])
    async def tod(self, ctx):
        truth = ['When was the last time you lied?',
        'When was the last time you cried?',
        "What's your biggest fear?"
        "Have you ever had a crush on an online girl/boy?",
        "How long do you often use Discord in a day?",
        "Have you ever begged your parents for more than $100?",
        "Have you ever cried because of an online girl/boy?",
        "What is your IP address? ||You can do nd!ip , ez||",
        "Hong long have you been using your current device?",
        "What's something you're glad that your mum doesn't know about you?",
        "Do you have a hidden talent?",
        "Have you ever cheated in an exam?",
        "Who is the cutest person in this game?",
        "Have you ever cheated on somebody?"]
        dare =["Kiss someone in the game ||do nd!kiss||",
        "Show your pp ||do nd!pp||",
        "Show the most embarrassing photo on your device.",
        "Say something dirty to a person",
        "Show your voice in VC.",
        "Talk like a pet in 1 minute.",
        "Take a screenshot of your device",
        "Give your Spotify playlist",
        "Do reveal ||nd!aniver is allowed||",
        "Spam someone else's DM",
        "Get muted in a server and take screenshot for prooving",]
        truth_btn = Button(label="Truth", style=discord.ButtonStyle.green, emoji= "<:abchehe:930388815984623646>")
        dare_btn = Button(label="Dare",style=discord.ButtonStyle.red,emoji="<a:abclmao:930389904884658197>")
        truth_view = View()
        truth_view.add_item(truth_btn)
        truth_view.add_item(dare_btn)
        embed = discord.Embed(title="TOD command",description="Choose one button",color=discord.Color.teal())
        async def truth_callback(interaction):
            embed = discord.Embed(title = "Truth", description=random.choice(truth),color=discord.Color.teal())
            await interaction.response.edit_message(embed=embed, view = None)
        async def dare_callback(interaction):
            embed = discord.Embed(title = "Dare", description=random.choice(dare),color=discord.Color.teal())
            await interaction.response.edit_message(embed=embed, view = None)
        truth_btn.callback = truth_callback
        dare_btn.callback = dare_callback
        await ctx.reply(embed = embed, view=truth_view)

def setup(bot):
    bot.add_cog(tod(bot))