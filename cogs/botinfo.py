import discord
from discord.ext import commands
import datetime, time
class botinfo(commands.Cog):
    def __init__(self, bot):
        self.client=bot
    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()
    @commands.command()
    async def botinfo(self, ctx):
        embed = discord.Embed(title = f"{self.client.user.name}'s info", description=f"**Servers:** ```{len(self.client.guilds)}``` \n**Users:** ```{len(self.client.users)}``` \n**Commands:** ```{len(self.client.commands)}``` \n**Uptime:** ```{str(datetime.timedelta(seconds=int(round(time.time()-startTime))))}```", color = discord.Color.teal())
        embed.set_thumbnail(url=self.client.user.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        await ctx.reply(embed=embed)
def setup(bot):
    bot.add_cog(botinfo(bot))