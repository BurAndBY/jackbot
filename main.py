import os
import discord
from discord.ext import commands
from discord import Option
print("Everything imported")

bot = discord.Bot()
client = discord.Client()
print("Token added")

# Startup Information
@bot.event
async def on_ready():
    activity = discord.Game(name="The Jackbox Party Pack 10", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")
# Enter your guild ID here if needed to make bot server-only
@bot.slash_command()
async def code(
    ctx: discord.ApplicationContext,
    game: Option(str, "Game Name"),
    code: Option(str, "Game's Code"),
    pack: Option(int, "Jackbox pack"),
):
    steamid = 0 
    #Preset, could be removed since else added

    #I should implement switch cases, though it's too late. Let this cringe code rest.
    if pack==1:
      steamid = 331670
    elif pack == 2:
      steamid = 397460
    elif pack == 3:
      steamid = 434170
    elif pack == 4:
      steamid = 610180
    elif pack == 5:
      steamid = 774461
    elif pack == 6:
      steamid = 1005300
    elif pack == 7:
      steamid = 1211630
    elif pack == 8:
      steamid = 1552350
    elif pack == 9:
        steamid = 1850960
    elif pack == 0:
        steamid = 442070
    else:
        steamid = 1082710
        # 👀 Bug Fables easter egg. Remove this or replace steam id

    embed=discord.Embed(title="Game sent", color=0x00ff3c)
    embed.set_author(name="Jackbox Games")
    embed.set_thumbnail(url='https://yt3.ggpht.com/ytc/AKedOLQSi-NFAc6lL3E0mUvSl_78o9iC5jsbL6WQKopmcQ=s900-c-k-c0x00ffffff-no-rj')
    embed.add_field(name="Game:", value=game, inline=False)
    embed.add_field(name="Room code:", value=code, inline=False)
    if game != "MemeWax" or game != "MP3-Бред":
      gamelink = f"https://jackbox.tv/#{code}"
    else:
      gamelink = f"https://jack.trgu.ru/#{code}"
    embed.add_field(name="Link:", value=gamelink, inline=False)
    embed.add_field(name=f"Jackbox Party Pack {pack}", value="Bot made by @burandby (BurAndBY#6688)", inline=False)
    embed.set_image(url="https://cdn.cloudflare.steamstatic.com/steam/apps/" + str(steamid) + "/header.jpg?t=1644892505")
    await ctx.respond(embed=embed)

bot.run("put the token here")
client.run("put the token here")
print("Bot deployed")
