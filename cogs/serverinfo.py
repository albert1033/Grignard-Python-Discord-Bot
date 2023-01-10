import discord
from discord.ext import commands
import datetime
class serverinfo(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def serverinfo(self,ctx):
        embed = discord.Embed(title=f"{ctx.guild.name}'s information", color=discord.Color.teal())
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        categories = len(ctx.guild.categories)
        channels = text_channels + voice_channels
        id = ctx.guild.id
        owner = ctx.guild.owner
        create = str(int(ctx.guild.created_at.astimezone(datetime.timezone.utc).timestamp()))
        member = ctx.guild.member_count
        embed.set_thumbnail(url = str(ctx.guild.icon.url))
        embed.add_field(name="General", value=f"**Name:** {ctx.guild.name} \n **ID:** {id}", inline=True)
        embed.add_field(name="Channels", value=f"**Channels:** {channels} \n **Categories:** {categories} \n **Text channels:** {text_channels} \n **Voice channels:** {voice_channels}", inline=True)
        embed.add_field(name="Details", value=f"**Owner:** {owner} \n **Created at:** <t:{create}:F> <t:{create}:R> \n **Member count:** {member}", inline=True)
        await ctx.reply(embed=embed)
def setup(bot):
    bot.add_cog(serverinfo(bot))