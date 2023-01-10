import discord
from discord.ext import commands
import random

class future(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def future(self, ctx, *, user:discord.Member = None):
        poor = ['You went to a casino and you lost all of your money. Now you are poor as hell.',
        'You got deceived by an old lady and she took all of your money. Lmao imagine getting deceived by an old lady.',
        'You gave all of your money to the bank but you forgot your password. RIP.',
        "You got a job but the boss deceived you and didn't pay you. Poor you.",
        "You were poor from the start so I have nothing to say."]
        rich = ["You married a person who is a billionaire's child. You are rich now.",
        "You got an idea about how to save the environment so you gained a lot of money, good job.",
        "You had a good certification by chance so that you have a nice job and gain lots of money.",
        "You were born in a rich family so I have nothing to say.",
        "You were born in a normal family but when you were 15 years old your father said 'My kid, I am billionaire' so you became rich."]
        z = random.randint(0,1)
        if user == None:
            if z == 0:
                description = f"{random.choice(poor)}"
                url = "https://cdn.discordapp.com/attachments/893888180439367833/929206077675950160/pixlr-bg-result_1.png"
            elif z == 1:
                description = f"{random.choice(rich)}"
                url = "https://cdn.discordapp.com/attachments/893888180439367833/929041904748884040/main-qimg-a43265d4b83cecb31659b98724b3c4a2.png"
            embed = discord.Embed(title=f"{ctx.author.name}'s future", description = description, color = discord.Color.teal())
            embed.set_image(url = url)
            await ctx.reply(embed = embed)
        else:
            if z == 0:
                description = f"{random.choice(poor)}"
                url = "https://cdn.discordapp.com/attachments/893888180439367833/929206077675950160/pixlr-bg-result_1.png"
            elif z == 1:
                description = f"{random.choice(rich)}"
                url = "https://cdn.discordapp.com/attachments/893888180439367833/929041904748884040/main-qimg-a43265d4b83cecb31659b98724b3c4a2.png"
            embed = discord.Embed(title=f"{user.display_name}'s future", description = description, color= discord.Color.teal())
            embed.set_image(url = url)
            await ctx.reply(embed = embed)
def setup(bot):
    bot.add_cog(future(bot))