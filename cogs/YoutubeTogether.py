from discord.ext import commands
from discord_together import DiscordTogether

class YoutubeTogetherCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.togetherControl = await DiscordTogether("OTI2NzUyMzIyOTI5OTgzNTUw.YdAPXA.6-R5xDJlTB6Sn884LKlRLsXmTJ0") 
        # Remember to only use this if you haven't already made a bot variable for `togetherControl` in your bot.py file.
        # If you have already declared a bot variable for it, you can use `self.client.togetherControl` to access it's functions

    @commands.command(aliases = ['youtubetogether'])
    async def yttogether(self, ctx):
        # Here we consider that the user is already in a VC accessible to the bot.
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        await ctx.reply(f"Click the blue link below!\n{link}")

def setup(client):
    client.add_cog(YoutubeTogetherCog(client))