import discord
from discord.ext import commands
import random
import asyncio

class aniver(commands.Cog):
    def __init__(self, bot):
        bot.client = bot
    
    @commands.command(aliases = ['animever','animeversion','aniversion'])
    async def aniver(self, ctx, *, user:discord.Member = None):
        character = ['Kirito', 'Son Goku', 'Naruto Uzumaki','Ichigo','Gojo Satoru','Asuna','Hinata Shoyo', 
        'Hinata Hyuga','Kageyama Tobio','Kiyoko Shimizu','Sakura Haruno','Natsu Dragneel','Lucy Heartfilia', 
        'Gray Fullbuster', 'Vegeta','Sasuke Uchiha','Madara Uchiha','Boruto Uzumaki','Tanjiro Kamado', 
        'Zenitsu Agatsuma', 'Giyuu Tomioka', 'Shinobu Kocho', 'Kanao Tsuyuri', 'Aqua', 'Chichi','Nezuko Kamado',
        'Kaguya Shinomiya','Rikka Tanakashi','Mitsuri Kanroji','Kyouko Hori','Izumi Miyamura','Sukuna','Nobara Kusanagi',
        'Ram','Rem','Levi Ackerman','Eren Yeager','Mikasa Ackerman']
        z = random.choice(character)
        if z == 'Kirito':
                url = ['https://c.tenor.com/zbZ3fR5i5hcAAAAC/sao-kirito.gif',
                'https://c.tenor.com/JJXP77656U4AAAAC/sword-art-online-unamused.gif']
        elif z == 'Son Goku':
                url = ['https://c.tenor.com/XfrqyR_-jzIAAAAC/anime-goku.gif',
                'https://c.tenor.com/Qj3K1p9s2HkAAAAd/son-goku-super-saiyan.gif']
        elif z == 'Naruto Uzumaki':
                url = ['https://c.tenor.com/mCiM7CmGGI4AAAAC/naruto.gif',
                'https://c.tenor.com/ofn7NRb0E14AAAAC/naruto-fox-mode-naruto-shippuden.gif']
        elif z == 'Ichigo':
                url = ['https://c.tenor.com/uty2QXNscmQAAAAC/ichigo-bleach.gif',
                'https://c.tenor.com/uZkLh_-nK3kAAAAC/ichigo-bleach.gif']
        elif z == 'Gojo Satoru':
                url = ['https://c.tenor.com/6QqupmFFausAAAAd/satoru-gojo.gif',
                'https://c.tenor.com/N9tfR3_w9uYAAAAC/gojo-satoru-hollow-purple.gif']
        elif z == 'Asuna':
                url = ['https://c.tenor.com/Fz3fwf0ETCoAAAAC/asuna-sao.gif',
                'https://c.tenor.com/8AX-nvqjUHQAAAAC/sao-hits.gif']
        elif z == 'Hinata Shoyo':
                url = ['https://c.tenor.com/C125fnskXNYAAAAC/grrrrrr.gif',
                'https://c.tenor.com/CYlBRIQNK0UAAAAC/hinata-smile.gif']
        elif z == 'Hinata Hyuga':
                url = ['https://c.tenor.com/U_nsDqH7klkAAAAC/ano-blushing.gif',
                'https://c.tenor.com/AsZNVBdcauMAAAAC/hinata-hyuga.gif']
        elif z == 'Kageyama Tobio':
                url = ['https://c.tenor.com/AZaius9fhyIAAAAC/kageyama-tobio.gif',
                'https://c.tenor.com/1ase4-e7yi8AAAAd/kageyama-eating.gif']
        elif z == 'Kiyoko Shimizu':
                url = ['https://c.tenor.com/GhiNS-Tjqz0AAAAC/kiyoko-kiyoko-shimizu.gif',
                'https://c.tenor.com/alyynTmYpgsAAAAC/kiyoko-haikyuu.gif']
        elif z == 'Sakura Haruno':
                url = ['https://c.tenor.com/rSS0Q35MGNQAAAAC/punch-sakura.gif',
                'https://c.tenor.com/k7WWwfU5nAYAAAAC/sakura-naruto.gif']
        elif z == 'Natsu Dragneel':
                url = ['https://c.tenor.com/0OCyLe8flawAAAAC/natsu.gif',
                'https://c.tenor.com/JHkrzIAFxaQAAAAC/natsu-dragneel-natsu-tartaros.gif']
        elif z == 'Lucy Heartfilia':
                url = ['https://c.tenor.com/76FoWEZsouIAAAAM/fairy-tail-lucy-heartfilia.gif',
                'https://c.tenor.com/ge5s70AZ5fQAAAAC/fairy-tail-winking.gif']
        elif z == 'Gray Fullbuster':
                url = ['https://c.tenor.com/XsZki-voy1MAAAAd/grayfullbuster.gif',
                'https://c.tenor.com/bGJULkN2DzoAAAAC/bola-de-hielo-dou.gif']
        elif z == 'Vegeta':
                url = ['https://c.tenor.com/u9PUI2VfXKkAAAAC/vegeta-gifs.gif',
                'https://c.tenor.com/WeMuLPPq2cwAAAAC/vegeta-rage.gif']
        elif z == 'Sasuke Uchiha':
                url = ['https://c.tenor.com/9Pnj62UINAcAAAAM/sasuke-sasuke-susanoo.gif',
                'https://c.tenor.com/iR3Wf_HLMYAAAAAC/laugh-lol.gif']
        elif z == 'Madara Uchiha':
                url = ['https://c.tenor.com/paSN7hpqlIIAAAAM/madara-naruto-shippuden-madara.gif',
                'https://c.tenor.com/mBbDsPL0icQAAAAC/hh.gif']
        elif z == 'Boruto Uzumaki':
                url = ['https://c.tenor.com/dN8QK_pU700AAAAC/boruto-jogan.gif',
                'https://c.tenor.com/-GuBdOP4nYAAAAAC/lets-fight.gif']
        elif z == 'Tanjiro Kamado':
                url = ['https://c.tenor.com/57kKrag-yvoAAAAM/demon-slayer-tanjiro.gif',
                'https://c.tenor.com/4NITUw4C1awAAAAd/anime-demon-slayer.gif']
        elif z == 'Zenitsu Agatsuma':
                url = ['https://c.tenor.com/aIvuHZ0RISMAAAAd/kimetsu-no-yaiba-demon-slayer.gif',
                'https://c.tenor.com/MNtqvOEE5Z0AAAAC/zenitsu-zenitsu-agatsuma.gif']
        elif z == 'Giyuu Tomioka':
                url = ['https://c.tenor.com/VF6ZiN9PrTAAAAAC/giyuu-tomioka-kimetsu-no-yaiba.gif',
                'https://c.tenor.com/hal0bUXw_mYAAAAC/giyuu-tomioka-demon-slayer.gif']
        elif z == 'Shinobu Kocho':
                url = ['https://c.tenor.com/LWfAAmi64nwAAAAd/shinobu-kocho.gif',
                'https://c.tenor.com/IsoR_vUmoDQAAAAC/shinobu-kocho-demon-slayer.gif']
        elif z == 'Kanao Tsuyuri':
                url = ['https://c.tenor.com/h8kvXLmjXFAAAAAC/kanao-smile.gif',
                'https://c.tenor.com/9unBzWU9qPwAAAAC/kanao-vs-tanjiro-tanjiro.gif']
        elif z == 'Aqua':
                url = ['https://c.tenor.com/TtSO-_weHb0AAAAC/aqua-anime.gif',
                'https://c.tenor.com/_LGLman7M6wAAAAC/aqua-konosuba.gif']
        elif z == 'Chichi':
                url = ['https://c.tenor.com/SkNVAk8852kAAAAC/goku-chichi.gif']
        elif z == 'Nezuko Kamado':
                url = ['https://c.tenor.com/Y0He2t8G0DMAAAAC/nezuko-kamado-tanjirou-kamado.gif',
                'https://c.tenor.com/rA526R3LxxUAAAAd/nezuko-kamado-running.gif']
        elif z == 'Kaguya Shinomiya':
                url = ['https://c.tenor.com/6oF4HsBgyTQAAAAC/kaguya-kaguya-sama.gif',
                'https://c.tenor.com/WzaIC9WHmogAAAAC/triggered-triggered-kaguya.gif']
        elif z == 'Rikka Tanakashi':
                url = ['https://c.tenor.com/Vf3v7W2oGpIAAAAC/rikka-rikka-takanashi.gif',
                'https://c.tenor.com/Oeh1BhX4wAAAAAAC/love-chunibyo-rikka-takanashi.gif']
        elif z == 'Mitsuri Kanroji':
                url = ['https://c.tenor.com/IZeujtId1j8AAAAd/shhhh.gif',
                'https://c.tenor.com/eGBU5BiY2vIAAAAC/mitsuri-demon-slayer.gif']
        elif z == 'Kyouko Hori':
                url = ['https://c.tenor.com/mU_WOLlVI-IAAAAC/horimiya-hori.gif',
                'https://c.tenor.com/ovD0fGxkDPEAAAAC/kyouko-hori.gif']
        elif z == 'Izumi Miyamura':
                url = ['https://c.tenor.com/V-TCY1xFJzIAAAAd/miyamura.gif',
                'https://c.tenor.com/gePaZLuiEagAAAAC/miyamura-izumi.gif']
        elif z == 'Sukuna':
                url = ['https://c.tenor.com/rRm8II31YF0AAAAC/ryomen-sukuna-sukuna.gif',
                'https://c.tenor.com/cf6fnw5P1QcAAAAC/merci.gif']
        elif z == 'Nobara Kusanagi':
                url = ['https://c.tenor.com/ob4qP-jLrNUAAAAC/jujutsu-kaisen-kugisaki-nobara.gif',
                'https://c.tenor.com/7YHmEqEEiTQAAAAd/jujutsu-kaisen-kugisaki-nobara.gif']
        elif z == 'Ram':
                url = ['https://c.tenor.com/wklB6YsMfXEAAAAd/ram-re.gif',
                'https://c.tenor.com/j6bc7KPSG-EAAAAM/ram-rem.gif']
        elif z == 'Rem':
                url = ['https://c.tenor.com/9pZXqC2wc3UAAAAC/rem-waifu.gif',
                'https://c.tenor.com/tVuvcf4SFwoAAAAC/anime-cute.gif']
        elif z == 'Levi Ackerman':
                url = ['https://c.tenor.com/AXTSXVbBdOIAAAAC/leviackerman-attackontitan.gif',
                'https://c.tenor.com/9Bu-lTKMyxsAAAAC/levi-ackerman-snk.gif']
        elif z == 'Eren Yeager':
                url = ['https://c.tenor.com/b87IgxOfeKUAAAAd/eren-yeager-eren.gif',
                'https://c.tenor.com/5SUdQj8_Fw4AAAAC/asd.gif']
        elif z == 'Mikasa Ackerman':
                url = ['https://c.tenor.com/DW3SnSCakS8AAAAC/getting-fit-workout.gif',
                'https://c.tenor.com/UHuYFGm16_QAAAAd/mikasa-ackerman-mikasa.gif']
        if user is None:
            embed = discord.Embed(title= f"{ctx.author.name}'s anime version", description=f"Your anime version is **{z}**", color = discord.Color.teal())
            embed.set_image(url = random.choice(url))
            embed.set_footer(text= "100% real")
            await ctx.reply(embed = embed)
        else:
            embed = discord.Embed(title = f"{user.display_name}'s anime version", description=f"{user.display_name}'s anime version is **{z}**", color=discord.Color.teal()) 
            embed.set_image(url = random.choice(url))
            embed.set_footer(text= "100% real")
            await ctx.reply(embed = embed)
def setup(bot):
    bot.add_cog(aniver(bot))