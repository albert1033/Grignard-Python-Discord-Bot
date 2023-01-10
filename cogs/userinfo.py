import discord
from discord.ext import commands
import datetime
class userinfo(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command(aliases = ['whois'])
    async def userinfo(self, ctx, user:discord.Member = None):
        if user is None:
            user = ctx.author
        #_user = await self.client.fetch_user(user.id)
        create = str(int(user.created_at.astimezone(datetime.timezone.utc).timestamp()))
        join = str(int(user.joined_at.astimezone(datetime.timezone.utc).timestamp()))
        rolelist = [r.mention for r in user.roles if r != ctx.guild.default_role]
        if len(rolelist) == 0:
            roles = "None"
        else:
            roles = ", ".join(rolelist) 
        embed = discord.Embed(title=f"{user.display_name}'s userinfo", color=discord.Color.teal())

       # if _user.banner is not None:
            #embed.set_image(url=_user.banner.url)
        embed.set_thumbnail(url=f"{user.display_avatar}")
        embed.add_field(name="Name", value=f"**System name:** {user.name} \n **Display name:** {user.display_name} \n **ID:** {user.id}", inline=False)
        embed.add_field(name="Date", value=f"**Created At:** <t:{create}:F> <t:{create}:R> \n **Joined At:** {'<t:' + join + ':F> <t:' + join + ':R>' if join is not None else 'Not in the server.'}", inline=False)
        embed.add_field(name="Profile", value=f"System avatar: [Click this]({user.avatar.url}) \n Server avatar: [Click this]({user.display_avatar.url})", inline=False)
        embed.add_field(name="Roles", value=roles)
        await ctx.reply(embed=embed)
def setup(bot):
    bot.add_cog(userinfo(bot))



