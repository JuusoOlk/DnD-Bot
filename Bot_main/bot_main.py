import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import youtube_dl
import os
import random
import asyncio

from ctypes.util import find_library

client = commands.Bot(command_prefix='!')


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

dclient = Bot('!')
# MUISTETAAN KOMMENTOIDA KOODI
# MUISTETAAN KOMMENTOIDA KOODI
# MUISTETAAN KOMMENTOIDA KOODI
# MUISTETAAN KOMMENTOIDA KOODI
# MUISTETAAN KOMMENTOIDA KOODI

@client.event
async def on_ready():
    print(f'{client.user.name} is online!')


@client.command()
async def bot_info(ctx):
    embed = discord.Embed(title="DnD-Bot", description="Making DnD easier :)")
    embed.add_field(name="Commands I react to:", value="!phb, !roll d4....")
    await ctx.send(embed=embed)


@client.command()
async def phb(ctx):
    await ctx.send("A link to the player's handbook: http://orc-news.ru/dnd5eng.pdf")

@client.command()
async def heroic(ctx):
    heroic = ["https://open.spotify.com/track/29gW6N4TtGhpkYmYwhRvDL?si=iGc9ASDUQu2VVa7QozaGRg", "https://open.spotify.com/track/4JtvyWkWQTPVcroZf8JJkp?si=N30P6Q_JT0CNnc8N0VBF9g", "https://open.spotify.com/track/2jn89xTHIVsy167uOmAewt?si=iVbs2iivT5eyu35MCqPKrA", "https://open.spotify.com/track/1YtHpYEbbfQQIyxXkdxEoW?si=zWzC7hnLSpSNc5nfj8nwvQ", "https://open.spotify.com/track/3pTNVDJpzaLxiZnbC18SMX?si=WWBjGMXqTDG19-FhbEp3SA", "https://open.spotify.com/track/2ZssT3XEX1cObqahy9YrQM?si=hplZhcrHRgCNyGT7-W6SjQ", "https://open.spotify.com/track/0G8iyOJFQ8Wvm4Fe6xjQdr?si=CjjUIecdRxyQ_Zy07muxAw", "https://open.spotify.com/track/2F9xBxKbx2M0pbgtSu8fLf?si=d6tLHZMyQSCoRlfoVsDr3w", "https://open.spotify.com/track/3GJZLvGXaVszYdSBLMtJFX?si=4uVSIjm5Tey0Ykvc3bYH4g", "https://open.spotify.com/track/2k2Pwkt3Fqowcve91PiH4g?si=wSJjbyoiTv6o_JISrRIMdQ", "https://open.spotify.com/track/1l2g97tNnO52U1IS0y9GRL?si=zaa7CBA3RlS2WUY4Bxadzw", "https://open.spotify.com/track/1No2I2TNhCXDNovL5O7ang?si=0dY850i8TVuC34l88yk4DA", "https://open.spotify.com/track/3jKkPcETVg1I9RR7ECgE4b?si=qSfGtzwHR4mtVESXNa66Gw"]
    await ctx.send(random.choice(heroic))

@client.command()
async def tavern(ctx):
    tavern = ["https://open.spotify.com/track/396qEVyZ1I7W6fNE12APdO?si=dI3xM_v9QcmT0lWeQ_WpSA", "https://open.spotify.com/track/4pW1ftcpCJt1VxbPwVknz0?si=mhyy92-RS7uijJpRYSJfQQ", "https://open.spotify.com/track/7z7WfdoT4qI16aXfWoNRlj?si=E_eVuNZIRrW-PlYMQBvRYw", "https://open.spotify.com/track/7Lp3BqKR2VE1NNd2LDuvzb?si=0ASpEeP3Tzi6K2UAVmZAzQ", "https://open.spotify.com/track/2TLO035tumZKpxxeDlKYQb?si=o72w9mXPQTSK7rGjMmXUhw", "https://open.spotify.com/track/1FdX2jpsp9Gt1rHxUROE6n?si=_-B6igUBRo6eFRa41TbAnQ", "https://open.spotify.com/track/1FV2g6zFu0ThzLMK4apEEy?si=hX6K-029S4STvdFPMap4Gg", "https://open.spotify.com/track/6ZBvQOuEp4ggTYAsqq0YFa?si=eB9uvq20QSSXxGZ4lmUJ4A", "https://open.spotify.com/track/3q79jp15s3gBLddLosTPP5?si=LrKwxK2ESZ2SqxHnwNPj8A", "https://open.spotify.com/track/08m0MIad094kPXhjwWi6Gu?si=LMzCgTbCS2SF7SdJ3V3Pxg"]
    await ctx.send(random.choice(tavern))


@client.command()
async def d4(ctx):
    d4 = list(range(1, 5))
    await ctx.send(random.choice(d4))


@client.command()
async def d6(ctx):
    d6 = list(range(1, 7))
    await ctx.send(random.choice(d6))


@client.command()
async def d8(ctx):
    d8 = list(range(1, 9))
    await ctx.send(random.choice(d8))


@client.command()
async def d10(ctx):
    d10 = list(range(1, 11))
    await ctx.send(random.choice(d10))


@client.command()
async def d12(ctx):
    d12 = list(range(1, 13))
    await ctx.send(random.choice(d12))


@client.command()
async def d20(ctx):
    d20 = list(range(1, 21))
    await ctx.send(random.choice(d20))


@client.command()
async def d100(ctx):
    d100 = list(range(1, 101))
    await ctx.send(random.choice(d100))


@client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel}")


@client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Don't think I am in a voice channel")


@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to remove song file, but it is being played")
        await ctx.send("ERROR: Music Playing")
        return

    await ctx.send("Getting everything ready to rock!")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"),
               after=lambda e: print(f"{name} has finished playing"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.05

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("Playing\n")


@client.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Song paused")
        voice.pause()
        await ctx.send("Song paused")
    else:
        print("Song is not playing, failed pause")
        await ctx.send("Song is not playing, failed pause")


@client.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Song resumed")
        voice.resume()
        await ctx.send("Song resumed")
    else:
        print("Song is not paused")
        await ctx.send("Song is not paused")


@client.command(pass_context=True, aliases=['s', 'sto'])
async def stop(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Song stopped")
        voice.stop()
        await ctx.send("Song stopped")
    else:
        print("Song is not playing, failed stop")
        await ctx.send("Song is not playing, failed stop")


client.run(token)
