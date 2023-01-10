import discord
from discord.ext import commands
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO

class ship(commands.Cog):
    def __init__(self, bot):
        self.client=bot
    @commands.command()
    async def ship(self, ctx, member1: discord.Member, *, member2: discord.Member = None):
        img = Image.open("cogs/lovepic.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("cogs/Lover.otf", 90)
        rate = random.randint(0, 100)
        if member2 is None:
            author = ctx.author
            asset1 = author.avatar.with_size(256)
            asset2 = member1.avatar.with_size(256)
            if author.id == 767342472400994355 and member1.id == 892088884937228290:
                rate = 100
        else:
            asset1 = member1.avatar.with_size(256)
            asset2 = member2.avatar.with_size(256)
            if member1.id == 767342472400994355 and member2.id == 892088884937228290:
                rate = 100
            
        data1=BytesIO(await asset1.read())
        data2 = BytesIO(await asset2.read())
        pfp1 = Image.open(data1)
        pfp2 = Image.open(data2)
        img.paste(pfp1, (10, 10))
        img.paste(pfp2, (565, 10))
        draw.text((350, 110), f"{str(rate)}%", font=font)
        img.save("cogs/loveimg2.png")
        await ctx.reply(file=discord.File("cogs/loveimg2.png"))
        

def setup(bot):
    bot.add_cog(ship(bot))
            