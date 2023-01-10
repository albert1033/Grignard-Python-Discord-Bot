import discord
import random
from discord.ext import commands
from discord.ui import Button, View



class rps(commands.Cog):
    def __init__(self, bot):
        bot.client = bot 

    @commands.command(aliases = ['rockpaperscissors'])
    async def rps(self, ctx):
        computer = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(computer)
        async def rock_callback(interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message(f"{interaction.user}, this is not your game", ephemeral=True)
            else:
                user = "rock" 
                if user == computer_choice: 
                    embed = discord.Embed(title = 'Tie!', description = 'You choosed rock and I choosed rock too.', color = discord.Color.red())
                    await interaction.response.edit_message(embed = embed, view=None)
                elif computer_choice=="scissors":
                    embed = discord.Embed(title = 'You won!', description = 'You choosed rock and I choosed scissors.', color = discord.Color.green())
                    await interaction.response.edit_message(embed = embed, view=None)
                elif computer_choice=="paper":
                    embed = discord.Embed(title = 'I won!', description = 'You choosed rock and I choosed papers.', color = discord.Color.blue())
                    await interaction.response.edit_message(embed = embed, view=None)

        async def paper_callback(interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message(f"{interaction.user}, this is not your game", ephemeral=True)
            else:
                user = "paper"
                if user == computer_choice: 
                    embed = discord.Embed(title = 'Tie!', description = 'You choosed paper and I choosed paper too.', color = discord.Color.red())
                    await interaction.response.edit_message(embed = embed, view=None)
                if computer_choice=="scissors":
                    embed = discord.Embed(title = 'I won!', description = 'You choosed paper and I choosed scissors.', color = discord.Color.green())
                    await interaction.response.edit_message(embed = embed, view=None)
                elif computer_choice=="rock":
                    embed = discord.Embed(title = 'You won!', description = 'You choosed paper and I choosed rock.', color = discord.Color.blue())
                    await interaction.response.edit_message(embed = embed, view=None)

        async def scissors_callback(interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message(f"{interaction.user}, this is not your game", ephemeral=True)

            else:
                user = "scissors" 
                if user == computer_choice: 
                    embed = discord.Embed(title = 'Tie!', description = 'You choosed scissors and I choosed Scissors too.', color = discord.Color.red())
                    await interaction.response.edit_message(embed = embed, view=None)
                if computer_choice=="paper":
                    embed = discord.Embed(title = 'You won!', description = 'You choosed scissors and I choosed paper.', color = discord.Color.green())
                    await interaction.response.edit_message(embed = embed, view=None)
                elif computer_choice=="rock":
                    embed = discord.Embed(title = 'I won!', description = 'You choosed scissors and I choosed rock.', color = discord.Color.blue())
                    await interaction.response.edit_message(embed = embed, view=None)

        rockb = Button(style = discord.ButtonStyle.red, emoji="🌑")
        paperb = Button(style = discord.ButtonStyle.green, emoji="📄")
        scissorb = Button(style = discord.ButtonStyle.blurple, emoji="✂️")

        view = View()

        view.add_item(rockb)
        view.add_item(paperb)
        view.add_item(scissorb)


        rockb.callback = rock_callback
        paperb.callback = paper_callback  
        scissorb.callback = scissors_callback

        question = discord.Embed(color = discord.Color.teal(), title = 'Play RPS with me!', description = "Rock, paper, or scissors? Choose fast or die")
        await ctx.reply(embed= question, view = view) 



def setup(bot):
    bot.add_cog(rps(bot))