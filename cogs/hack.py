import discord
from discord.ext import commands
from discord.ext.commands import bot
import random
import asyncio
class hack(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command()
    async def hack(self, ctx, *, user:discord.Member = None):
        email = ['ilovemum@gmail.com',
        'lucyishot@gmail.com',
        'yourgfismine@yahoo.com',
        'youarehot@hotmail.com',
        'iloveyourbutt@hotmail.com',
        'mayidateyoursister@yahoo.com',
        'sendmenukes@gmail.com',
        'donaldtrumpishandsome@yahoo.com',]
        password = ['123456',
        'iloveyou',
        'ilovemum123',
        'narutosasuke',
        '12345678',
        '1234567890',
        'yourbuttisbig',
        'fbiopenup',
        'bigbuttboi',]
        DM = ['I love you bro',
        'Your mum is hot',
        'Kiss me when?',
        'Send me nukes',
        'May I date your sister?',
        'Can you marry me?',
        'Remember our secret bro',
        'FBI OPEN UP',
        'LMFAO',
        'Let me lick your face',
        'Dattebayo']
        emoji = ['🙏','🇫','🖕', '💋', '💀','😏']
        if user is None:
            msg = await ctx.reply(f"Hacking has begun. We are hacking **{ctx.author.name}** <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"**{ctx.author.name}**'s email: {random.choice(email)} <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"**{ctx.author.name}**'s password: {random.choice(password)} <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"Bypassing 2FA (if **{ctx.author.name}** has) <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"**{ctx.author.name}**'s latest DM: {random.choice(DM)} <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"**{ctx.author.name}**'s most used emoji: {random.choice(emoji)} <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"Sending **{ctx.author.name}**'s data to FBI <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"The **totally** dangerous hacking has been ended")
        else:
            msg = await ctx.reply(f"Hacking has begun. We are hacking **{user.display_name}** <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"**{user.display_name}**'s email: {random.choice(email)} <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"**{user.display_name}**'s password: {random.choice(password)} <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"Bypassing 2FA (if **{user.display_name}** has) <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"**{user.display_name}**'s latest DM: {random.choice(DM)} <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"**{user.display_name}**'s most used emoji: {random.choice(emoji)} <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"Selling **{user.display_name}**'s data to FBI and receive 100 millions dollars <a:loadingloading:928828204632899644>")
            await asyncio.sleep(10)
            await msg.edit(f"The **totally** dangerous hacking has been ended")


def setup(bot):
    bot.add_cog(hack(bot))