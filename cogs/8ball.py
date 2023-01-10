import discord
from discord.ext import commands
import random

class eightball(commands.Cog):
    def __init__(self, bot):
        self.client = bot
    @commands.command(aliases=['8ball', '8b'])
    async def _8ball(self,ctx, *, question):
        responses = [
            'Hell no.',
            'Prolly not.',
            'Idk bro.',
            'Prolly.',
            'Hell yeah my dude.',
            'It is certain.',
            'It is decidedly so.',
            'Without a Doubt.',
            'Yes - Definitaly.',
            'You may rely on it.',
            'As i see it, Yes.',
            'Most Likely.',
            'Outlook Good.',
            'Yes!',
            'No!',
            'Signs a point to Yes!',
            'Reply Hazy, Try again.',
            'Better not tell you know.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            "Don't Count on it.",
            'My reply is No.',
            'My sources say No.',
            'Outlook not so good.',
            'Very Doubtful']
        embed = discord.Embed(title = f"{self.client.user.name} bot's 8ball system", description = '🎱 **Question:** ' + question + "\n 🎱 **Answer:** " + (random.choice(responses)),
        color = discord.Color.teal())
        await ctx.reply(embed = embed)
def setup(bot):
    bot.add_cog(eightball(bot))