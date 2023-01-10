import discord
from discord.ext import commands

class snipe(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
        self.sniped_messages = {}
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.attachments:
            bob = message.attachments[0]
            self.sniped_messages[message.guild.id] = (bob.proxy_url, message.content, message.author, message.channel.id, message.created_at)
        else:
            self.sniped_messages[message.guild.id] = (message.content,message.author, message.channel.id, message.created_at)

    @commands.command()
    async def snipe(self, ctx):
        try:
            bob_proxy_url, contents,author, channel_name, time = self.sniped_messages[ctx.guild.id]
        except:
            contents,author, channel_name, time = self.sniped_messages[ctx.guild.id]
        
        embed = discord.Embed(color=discord.Color.teal(), timestamp=time)
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar.url)
        try:
            embed = discord.Embed(description=f"{contents} \n [This message has an attachment]" , color=discord.Color.teal(), timestamp=time)
            embed.set_image(url=bob_proxy_url)
            embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar.url)
            embed.add_field(name="Deleted in", value=f"<#{channel_name}>", inline=False)
            embed.set_footer(text=f"Server: {ctx.guild.name} | Requested by: {ctx.author.display_name}", icon_url=ctx.author.display_avatar.url)
            await ctx.channel.send(embed=embed)
        except:
            embed = discord.Embed(description=contents , color=discord.Color.teal(), timestamp=time)
            embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar.url)
            embed.add_field(name="Deleted in", value=f"<#{channel_name}>", inline=False)
            embed.set_footer(text=f"Server: {ctx.guild.name} | Requested by: {ctx.author.display_name}", icon_url=ctx.author.display_avatar.url)
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(snipe(bot))