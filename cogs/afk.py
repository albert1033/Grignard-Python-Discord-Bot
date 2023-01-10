import discord
from discord.ext import commands
from discord.utils import get
import asyncio
def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
class afk(commands.Cog):
    def __init__(self, bot):
        self.client = bot
        global afks
        afks = {}
    
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def afk(self, ctx, *, reason=None):
        member = ctx.author
        if member.id in afks.keys():
            afks.pop(member.id)
        else: 
            try:
                await member.edit(nick=f"[AFK] {member.display_name}")
            except:
                pass
        if reason is None:
            reason = "No reason provided."  
        embed=discord.Embed(title="<a:afk:946311198645837864> AFK", description=f"{member.mention} is now AFK for reason: {reason}", color=discord.Color.teal())
        embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.set_footer(text=f"{member.name}#{member.discriminator}", icon_url=member.avatar.url)
        await ctx.send(embed=embed)
        await asyncio.sleep(10)
        afks[member.id] = reason  #adds the user to the afk list
    @afk.error
    async def afk_error(self, ctx:commands.Context, error:commands.CommandError):
        if isinstance(error, commands.CommandOnCooldown):
            message = f"Calm down... You can only use this command once every 10 seconds. Chill out."
            await ctx.send(message)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in afks.keys():
            afks.pop(message.author.id)
            try:
                await message.author.edit(nick=remove(message.author.display_name))
            except:
                pass
            embed = discord.Embed(title = "<:welcome:921664546677071894> Welcome back", description=f"Welcome back {message.author.name}, I removed your AFK status.", color=discord.Color.teal())
            await message.reply(embed=embed, delete_after=5)
        for id, reason in afks.items():
            member = get(message.guild.members, id=id)
            if (message.reference and member==(await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
                embed = discord.Embed(title = f"<a:afk:946311198645837864> {member.display_name} is AFK", description = f"Reason: {reason}", color = discord.Color.teal())
                embed.set_thumbnail(url = member.avatar.url)
                await message.reply(embed=embed, delete_after=5)
def setup(bot):
    bot.add_cog(afk(bot))