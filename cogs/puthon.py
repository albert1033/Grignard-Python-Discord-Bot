import discord
from discord.ext import commands

class puthon(commands.Cog):
    def __init__(self, bot):
        bot.client = bot

    @commands.command()
    async def puthon(self, ctx):
            embed = discord.Embed(title='Puthon Anthem', description = "puthon..\nits ourdivine\nits power\nits life\nits our home\nits our pride\nits our glory\nits our mom\nits ur mumtoo\nits our parents\nits our pleasure\nits our nation\nits our energy\nits our pressure\nits our anxiety\nits our depression\nits our headache\nits our daddy\nits our king\nits our queen\nits our prince\nits our princess\nits our worker\nits our master\nits our homie\nits our elder\nits our force\nits our acceleration\nits our heart\nits our soul\nits our hobby\nits our eren yaegar\nits our amogus\nits our anime\nits our firend\nits our belief\nits our history\nits our future\nits our present\nits our inception\nits our dream\nits our dream cafeits our ocean\nits our sea\nits our beach\nits our island\nits our ship\nits our captain\nits our gf\nits our work\nits our network\nits our sussy baka\nits our nuts\nits our sperm\nits our motherland\nits our gaming chair\nits our entertainment\nits our arts\nits our waifu\nits our husbandoo\nits our segs\nits our meme material\nits our condom\nits ur mum's worm too btw\nit's our dictionary", color = 0x5865F2)
            await ctx.reply(embed = embed)
def setup(bot):
	bot.add_cog(puthon(bot))