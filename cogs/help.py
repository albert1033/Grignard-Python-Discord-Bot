import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.client=bot
    @commands.group(invoke_without_command = True, case_insensitive=True)  #, aliases = ['Help']
    async def help(self, ctx):
      embed=discord.Embed(title="All commands", color = discord.Color.teal())
      embed.set_author(name=f"{self.client.user.name} bot", icon_url=self.client.user.avatar.url)
      embed.add_field(name="For Admin Only", value="`setprefix`", inline=False)
      embed.add_field(name="Information", value="`about`, `owner`, `vote`, `ping`, `suggestion`, `report`, `invite`, `support`, `botinfo`", inline=False)
      embed.add_field(name="Fun", value="`8ball`, `aniver`, `brain`, `cute`, `f`, `future`, `gayrate`, `hack`, `harem`, `ip`, `meme`, `nitro`, `party`, `pp`, `simp`, `sus`, `hornyrate`, `joke`, `textwall`, `say`, `ship`", inline=False)
      embed.add_field(name="Roleplay", value="`hug`, `kiss`, `kill`, `punch`, `vibe`, `laugh`, `pat`", inline=False)
      embed.add_field(name = "Utility", value ="`translate`, `quote`, `artist`, `anime`, `topanime`, `yttogether`, `spotify`, `snipe`, `afk`", inline = False)
      embed.add_field(name="Image", value="`gay`, `trigger`, `jail`, `hitler`, `airpods`, `america`, `communism`, `wanted`, `bed`, `aborted`, `affect`, `spank`, `jokeoverhead`", inline=False)
      embed.add_field(name="Games", value="`tod`, `rps`",inline=False)
      embed.add_field(name="User And Server", value="`avatar`, `userinfo`, `serverinfo`", inline=False)
      embed.set_footer(text="Do g.help <command> to see full help of each commag.")
      await ctx.reply(embed=embed)

    @help.command(aliases = ['8ball', '8b'])
    async def _8ball(self, ctx):
      embed = discord.Embed(title="8ball command", description="**Structure**: g.8ball [Question (required)]\n **Description**: Ask the bot a question!", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: 8b")
      await ctx.reply(embed=embed)

    @help.command()
    async def about(self, ctx):
      embed = discord.Embed(title="About command", description="**Structure**: g.about\n **Description**:About this bot.", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: About")
      await ctx.reply(embed=embed)

    @help.command(aliases = ['brainsize'])
    async def brain(self, ctx):
      embed = discord.Embed(title="Brain command", description="**Structure**: g.brain <Mention (not required)> \n **Description**: Check your brain's size or your friends' brains' sizes", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: brainsize")
      await ctx.reply(embed=embed)

    @help.command()
    async def f(self, ctx):
      embed = discord.Embed(title="F command", description="**Structure**: g.f\n **Description**: Pray respect in the chat.", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: F")
      await ctx.reply(embed=embed)

    @help.command()
    async def future(self, ctx):
      embed = discord.Embed(title="Future command", description="**Structure**: g.future <Mention (not required)>\n **Description**: See your future or your friends' future", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: Future")
      await ctx.reply(embed=embed)

    @help.command(aliases = ['howgay'])
    async def gayrate(self, ctx):
      embed = discord.Embed(title="Gayrate command", description="**Structure**: g.gayrate <Mention (not required)>\n **Description**: See your gayrate or your friends' gayrate", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: howgay")
      await ctx.reply(embed=embed)

    @help.command(aliases = ['howhorny'])
    async def hornyrate(self, ctx):
      embed = discord.Embed(title="Hornyrate command", description="**Structure**: g.hornyrate <Mention (not required)>\n **Description**: See your hornyrate or your friends' gayrate", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: howhorny, hornyrate")
      await ctx.reply(embed=embed)

    @help.command(aliases = ['rockpaperscissors'])
    async def rps(self, ctx):
      embed = discord.Embed(title="RPS command", description="**Structure**: g.rps\n **Description**: Play rps with me!", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: rockpaperscissors")
      await ctx.reply(embed=embed)

    @help.command()
    async def hack(self, ctx):
      embed = discord.Embed(title="Hack command", description="**Structure**: g.hack <Mention (not required)>\n **Description**: Hack your account or your friends' accounts", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: Hack")
      await ctx.reply(embed=embed)

    @help.command()
    async def harem(self, ctx):
      embed = discord.Embed(title="Harem command", description="**Structure**: g.harem <Mention (not required)>\n **Description**: See your harem or your friend's harems", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: Harem")
      await ctx.reply(embed=embed)

    @help.command()
    async def hug(self, ctx):
      embed = discord.Embed(title="Hug command", description="**Structure**: g.hug <Mention (not required)> <Notes (not required)>\n **Description**: Hug someone!", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: Hug")
      await ctx.reply(embed=embed)

    @help.command()
    async def kill(self, ctx):
      embed = discord.Embed(title="Kill command", description="**Structure**: g.kill <Mention (not required)> <Notes (not required)>\n **Description**: Kill someone!", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: Kill")
      await ctx.reply(embed=embed)

    @help.command()
    async def kiss(self, ctx):
      embed = discord.Embed(title="Kiss command", description="**Structure**: g.kiss <Mention (not required)> <Notes (not required)>\n **Description**: Kiss someone!", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: Kiss")
      await ctx.reply(embed=embed)

    @help.command(aliases = ['meme'])
    async def memes(self, ctx):
      embed = discord.Embed(title="Meme command", description="**Structure**: g.meme\n **Description**: See a meme from Reddit.", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: Meme")
      await ctx.reply(embed=embed)

    @help.command()
    async def nitro(self, ctx):
      embed = discord.Embed(title="Nitro command", description="**Structure**: g.nitro \n **Description**: Claim fake nitro.", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: Nitro")
      await ctx.reply(embed=embed)

    @help.command()
    async def owner(self, ctx):
      embed = discord.Embed(title="Owner command", description="**Structure**: g.owner \n **Description**: Information about owner of the bot", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: Owner")
      await ctx.reply(embed=embed)

    @help.command()
    async def party(self, ctx):
      embed = discord.Embed(title="Party command", description="**Structure**: g.party \n **Description**: Open a party!", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: Party")
      await ctx.reply(embed=embed)

    @help.command()
    async def pp(self, ctx):
      embed = discord.Embed(title="PP command", description="**Structure**: g.pp <Mention (not required)>\n **Description**: See your pp or your friends' pps", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: Pp")
      await ctx.reply(embed=embed)

    @help.command()
    async def punch(self, ctx):
      embed = discord.Embed(title="Punch command", description="**Structure**: g.punch <Mention (not required)> <Notes (not required)>\n **Description**: Punch someone!", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: Punch")
      await ctx.reply(embed=embed)

    @help.command()
    async def pat(self, ctx):
      embed = discord.Embed(title="Pat command", description="**Structure**: g.pat <Mention (not required)> <Notes (not required)>\n **Description**: Pat someone!", color = discord.Color.teal())
      await ctx.reply(embed=embed)

    @help.command()
    async def simp(self, ctx):
      embed = discord.Embed(title="Simp command", description="**Structure**: g.simp <Mention (not required)>\n **Description**: See your simprate or your friends' simprates", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: simprate")
      await ctx.reply(embed=embed)

    @help.command(aliases = ['dance'])
    async def vibe(self, ctx):
      embed = discord.Embed(title="Vibe command", description="**Structure**: g.vibe <Mention (not required)> <Notes (not required)>\n **Description**: Vibing time!", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: dance")
      await ctx.reply(embed=embed)

    @help.command(aliases = ['animever','animeversion'])
    async def aniver(self, ctx):
      embed = discord.Embed(title="Anime Version command", description="**Structure**: g.aniver <Mention (not required)>\n **Description**: See your or your friends' anime versions", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: animeversion, animever")
      await ctx.reply(embed=embed)

    @help.command(aliases = ['howcute', 'cuterate'])
    async def cute(self, ctx):
      embed = discord.Embed(title="Cute command", description="**Structure**: g.cute <Mention (not required)>\n **Description**: See how cute are you or how cute are your friends", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: howcute, cuterate")
      await ctx.reply(embed=embed)

    @help.command()
    async def ip(self, ctx):
      embed = discord.Embed(title="IP command", description="**Structure**: g.ip <Mention (not required)>\n **Description**: See your IP or your friends' IPs", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: None")
      await ctx.reply(embed=embed)

    @help.command(aliases = ['howsus', 'susrate'])
    async def sus(self, ctx):
      embed = discord.Embed(title="Sus command", description="**Structure**: g.sus <Mention (not required)>\n **Description**: See how sus are you or how sus are your friends", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: howsus, susrate")
      await ctx.reply(embed=embed)

    @help.command(aliases = ['truthordare'])
    async def tod(self, ctx):
      embed = discord.Embed(title="TOD command", description="**Structure**: g.tod\n **Description**: Play TOD", color = discord.Color.teal())
      embed.set_footer(text= "Aliases: truthordare")
      await ctx.reply(embed=embed)

    @help.command()
    async def ping(self, ctx):
      embed = discord.Embed(title ="Ping command", description="**Structure**: g.ping \n **Description**: See the bot's ping", color = discord.Color.teal())
      await ctx.reply(embed = embed)

    @help.command(aliases = ['aliases'])
    async def suggestion(self, ctx):
      embed = discord.Embed(title="Suggestion Command", description="**Structure**: g.suggestion [Suggestion (required)] \n **Description**: Suggest new idea for the bot's owner",
      color=discord.Color.teal())
      embed.set_footer(text="Aliases: sug")
      await ctx.reply(embed = embed)

    @help.command(aliases = ["smile"])
    async def laugh(self, ctx):
      embed = discord.Embed(title="Laugh command", description="**Structure**: g.laugh <Mention (not required)> <Notes (not required)> \n **Description** Laughing!!!",
      color = discord.Color.teal())
      embed.set_footer(text="Aliases: smile")
      await ctx.reply(embed = embed)

    @help.command()
    async def gay(self, ctx):
      embed = discord.Embed(title = "Gay command", description="**Structure**: g.gay <Mention (not required)> \n **Description**: Gay image of yourself or your friends'",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)

    @help.command()
    async def trigger(self, ctx):
      embed = discord.Embed(title = "Trigger command", description="**Structure**: g.trigger <Mention (not required)> \n **Description**: Triggered gif of yourself or your friends'",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)

    @help.command()
    async def jail(self, ctx):
      embed = discord.Embed(title = "Jail command", description="**Structure**: g.jail <Mention (not required)> \n **Description**: Jail image of yourself or your friends'",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)
    
    @help.command()
    async def aborted(self, ctx):
      embed = discord.Embed(title = "Aborted command", description="**Structure**: g.aborted <Mention (not required)> \n **Description**: Aborted image of yourself or your friends'",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)
    
    @help.command()
    async def affect(self, ctx):
      embed = discord.Embed(title = "Affect command", description="**Structure**: g.affect <Mention (not required)> \n **Description**: Affect image of yourself or your friends'",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)

    @help.command()
    async def hitler(self, ctx):
      embed = discord.Embed(title = "Hitler command", description="**Structure**: g.hitler <Mention (not required)> \n **Description**: Hitler image of yourself or your friends'",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)

    @help.command()
    async def airpods(self, ctx):
      embed = discord.Embed(title = "Airpods command", description="**Structure**: g.airpods <Mention (not required)> \n **Description**: Airpods gif of yourself or your friends'",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)

    @help.command()
    async def america(self, ctx):
      embed = discord.Embed(title = "America command", description="**Structure**: g.america <Mention (not required)> \n **Description**: America gif of yourself or your friends'",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)

    @help.command()
    async def communism(self, ctx):
      embed = discord.Embed(title = "Communism command", description="**Structure**: g.communism <Mention (not required)> \n **Description**: Communism gif of yourself or your friends'",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)

    @help.command()
    async def wanted(self, ctx):
      embed = discord.Embed(title = "Wanted command", description="**Structure**: g.wanted <Mention (not required)> \n **Description**: Wanted of yourself or your friends (Imagine being an One Piece character)'",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)

    @help.command()
    async def bed(self, ctx):
      embed = discord.Embed(title = "Bed command", description="**Structure**: g.bed [Mention 1 (required)] <Mention2 (not required)> \n **Description**: Bed gif of a couple",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)
    @help.command()
    async def ship(self, ctx):
      embed = discord.Embed(title = "Ship command", description="**Structure**: g.ship [Mention 1 (required)] <Mention2 (not required)> \n **Description**: Shipping time hehe",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)

    @help.command()
    async def jokeoverhead(self, ctx):
      embed = discord.Embed(title = "JokeOverHead command", description="**Structure**: g.jokeoverhead <Mention (not required)> \n **Description**: JokeOverHead image of yourself or your friends (Imagine being an One Piece character)'",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)
      
    @help.command()
    async def spank(self, ctx):
      embed = discord.Embed(title = "Spank command", description="**Structure**: g.spank [Mention 1 (required)] <Mention2 (not required)> \n **Description**: Spank image of a couple",
      color= discord.Color.teal())
      await ctx.reply(embed = embed)

    @help.command()
    async def report(self, ctx):
      embed = discord.Embed(title = "Report command", description="**Structure**: g.report [Content (required)] \n **Description**: Report a bug",
      color = discord.Color.teal())
      await ctx.reply(embed = embed)

    @help.command()
    async def support(self, ctx):
      embed = discord.Embed(title = "Support command", description="**Structure**: g.support \n **Description**: Join our official server",
      color = discord.Color.teal())
      await ctx.reply(embed = embed)
    @help.command()
    async def invite(self, ctx):
      embed = discord.Embed(title = "Invite command", description="**Structure**: g.invite \n **Description**: Add me to your bot",
      color = discord.Color.teal())
      await ctx.reply(embed = embed)
    @help.command(aliases = ['av'])
    async def avatar(self, ctx):
      embed=discord.Embed(title="Avatar command", description="**Structure:** g.avatar <Mention (not required)> \n **Description:** View your avatar",
      color=discord.Color.teal())
      embed.set_footer(text="Aliases: av")
      await ctx.reply(embed=embed)

    @help.command(aliases = ['whois'])
    async def userinfo(self, ctx):
      embed=discord.Embed(title="Userinfo command", description="**Structure:** g.userinfo <Mention (not required)> \n **Description:** See user's information",
      color=discord.Color.teal())
      embed.set_footer(text="Aliases: whois")
      await ctx.reply(embed=embed)

    @help.command()
    async def serverinfo(self, ctx):
      embed=discord.Embed(title="Serverinfo command", description="**Structure:** g.serverinfo <Mention (not required)> \n **Description:** See server's information",
      color=discord.Color.teal())
      await ctx.reply(embed=embed)

    @help.command()
    async def translate(self, ctx):
      embed=discord.Embed(title="Translate command", description="**Structure:** g.translate [Content (required)] \n **Description:** Translate a sentence from another language to English",
      color=discord.Color.teal())
      await ctx.reply(embed=embed)

    @help.command()
    async def joke(self, ctx):
      embed=discord.Embed(title="Joke command", description="**Structure:** g.joke \n **Description:** See a random joke",
      color=discord.Color.teal())
      await ctx.reply(embed=embed)

    @help.command()
    async def quote(self, ctx):
      embed=discord.Embed(title="Quote command", description = '**Structure:** g.quote \n **Description:** Get a random quote', color=discord.Color.teal())
      await ctx.reply(embed=embed)

    @help.command()
    async def artist(self, ctx):
      embed=discord.Embed(title="Artist command", description = "**Structure:** g.artist [Artist's name] \n **Description:** Get an artist's top 10 famous track", color=discord.Color.teal())
      await ctx.reply(embed=embed)

    @help.command(aliases=['animeinfo', 'searchanime'])
    async def anime(self, ctx):
      embed=discord.Embed(title="Anime command", description = "**Structure:** g.anime [Anime's name] \n **Description:** Search for an anime by its name", color=discord.Color.teal())
      embed.set_footer(text="Aliases: animeinfo, searchanime")
      await ctx.reply(embed=embed)

    @help.command(aliases=['trendinganime'])
    async def topanime(self, ctx):
      embed=discord.Embed(title="Topanime command", description = "**Structure:** g.topanime \n **Description:** Get top 10 most famous anime", color=discord.Color.teal())
      embed.set_footer(text="Aliases: trendinganime")
      await ctx.reply(embed=embed)

    @help.command()
    async def textwall(self, ctx):
      embed=discord.Embed(title="Textwall command", description="**Structure:** g.textwall \n **Description:** Get a textwall", color=discord.Color.teal())
      await ctx.reply(embed=embed)

    @help.command()
    async def say(self, ctx):
      embed=discord.Embed(title="Say command", description="**Structure:** g.say [Content (required)] \n **Description:** Make the bot say something", color=discord.Color.teal())
      await ctx.reply(embed=embed)

    @help.command(aliases = ['youtubetogether'])
    async def yttogether(self, ctx):
        embed = discord.Embed(title = "Youtube-Together command", description = "**Structure:** g.yttogether \n **Requirement:** User will have to join a VC before doing this command \n **Description:** Open a Youtube-Together Activity in VC", color = discord.Color.teal())
        embed.set_footer(text = "Aliases: yttogether, youtubetogether")
        await ctx.reply(embed=embed)
    @help.command()
    async def spotify(self, ctx):
      embed = discord.Embed(title = "Spotify command", description="**Structure:** g.spotify <User (Not required)> \n **Description:** Get information of the current Spotify track that an user is listening to.", color = discord.Color.teal())
      await ctx.reply(embed = embed)

    @help.command()
    async def snipe(self, ctx):
      embed = discord.Embed(title = "Snipe command", description="**Structure:** g.snipe \n **Description:** Get the latest message that got deleted in the server", color = discord.Color.teal())
      await ctx.reply(embed = embed)
    @help.command()
    async def setprefix(self, ctx):
      embed = discord.Embed(title = "Set prefix command", description="**Structure:** g.setprefix [Prefix (required)] \n **Description:** Set custom prefix (For admin only)", color = discord.Color.teal())
      await ctx.reply(embed = embed)
    @help.command()
    @commands.is_owner()
    async def jsk(self, ctx):
      await ctx.reply("read this shit https://cdn.discordapp.com/attachments/940897949347610654/941340350960791562/unknown.png")
    @help.command()
    async def botinfo(self, ctx):
        embed = discord.Embed(title = "Bot info command", description="**Structure:** g.botinfo \n **Description:** See bot's info", color= discord.Color.teal())
        await ctx.reply(embed=embed)
    @help.command()
    async def afk(self, ctx):
        embed=discord.Embed(title = "AFK command", description = "**Structure:** g.afk <Reason (not required)> \n **Description:** Set an afk message, work globally on every servers that have the me", color= discord.Color.teal())
        await ctx.reply(embed=embed)
      
def setup(bot):
    bot.add_cog(help(bot))