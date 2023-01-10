import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class artist(commands.Cog):
	def __init__(self, bot):
		bot.client = bot 
	@commands.command()
	async def artist(self, ctx, *, singer):
		spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="61693009a0e443c381ebd4027c70d5d2",
                                                   client_secret="aed6a2c01d654aada5e039f3b8afbdc8"))
		try:
			results = spotify.search(q=singer, type='artist')
			artist = results['artists']['items'][0]
			id = artist['id']
			top = spotify.artist_top_tracks(id)
			embed = discord.Embed(title=f"{singer.upper()}'s top track", color = discord.Color.teal())
			for idx, track in enumerate(top['tracks']):
				description= idx+1, track['name']
				e = idx+1
				embed.add_field(name=e, value=f"{track['name']}")
				# = "\n".join(description_list)
			await ctx.reply(embed=embed)
			
		except:
			embed= discord.Embed(title="Error!", description="Sorry, we can not find this artist. Try checking the typo", color=discord.Color.red())
			await ctx.reply(embed=embed)
def setup(bot):
	bot.add_cog(artist(bot))