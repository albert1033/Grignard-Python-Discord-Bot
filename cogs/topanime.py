import kitsu
import asyncio
import discord
from discord.ext import commands
from discord.ui import Button, View

class MyView(View):
    @discord.ui.button(label= "Page 1", style=discord.ButtonStyle.green, emoji="👈")
    async def button_callback(self, button, interaction):
        client = kitsu.Client()
        data = await client.trending_anime()
        main_data = data[0:5]
        embed = discord.Embed(title="Trending Anime", color = discord.Color.teal())
        for anime in main_data:
            embed.add_field(name = "📈 Name: ", value = f"{anime.canonical_title}", inline = False)
            embed.add_field(name ="🌠 Average Rating: ", value =  f"{str(anime.average_rating)} \n ――――――――――――――――――――――――――――", inline = True)
            embed.set_image(url="https://i.redd.it/q5khrnrwimu71.jpg")
            embed.set_footer(text=f"Page 1")
        await interaction.response.edit_message(embed=embed)
        await client.close()

    @discord.ui.button(label= "Page 2", style=discord.ButtonStyle.green, emoji="👉")
    async def page2_button_callback(self, button, interaction):
        client = kitsu.Client()
        data = await client.trending_anime()
        main_data = data[5:10]
        embed = discord.Embed(title="Trending Anime", color = discord.Color.teal())
        for anime in main_data:
            embed.add_field(name = "📈 Name: ", value = f"{anime.canonical_title}", inline = False)
            embed.add_field(name ="🌠 Average Rating: ", value =  f"{str(anime.average_rating)} \n ――――――――――――――――――――――――――――", inline = True)
            embed.set_image(url="https://i.redd.it/q5khrnrwimu71.jpg")
            embed.set_footer(text=f"Page 2")
        await interaction.response.edit_message(embed=embed)
        await client.close()
class topanime(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    @commands.command(aliases = ['trendinganime'])
    async def topanime(self, ctx):
        client = kitsu.Client()
        data = await client.trending_anime()
        main_data = data[0:5]
        embed = discord.Embed(title="Trending Anime", color = discord.Color.teal())
        embed.set_footer(text="Page 1")
        view = MyView()
        for anime in main_data:
            embed.add_field(name = "📈 Name: ", value = f"{anime.canonical_title}", inline = False)
            embed.add_field(name ="🌠 Average Rating: ", value =  f"{str(anime.average_rating)} \n ――――――――――――――――――――――――――――", inline = True)
            embed.set_image(url="https://i.redd.it/q5khrnrwimu71.jpg")
        
        # Close the internal aiohttp ClientSession  
        await client.close()
        await ctx.reply(embed = embed, view = view)

def setup(bot):
    bot.add_cog(topanime(bot))