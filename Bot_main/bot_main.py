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
# client = discord.Client()

@client.event # Toimii
async def on_ready():
    print(f'{client.user.name} is online!')

@client.command() # Toimii
async def bot_info(ctx):
    embed = discord.Embed(title="DnD-Bot", description="Making DnD easier :)")
    embed.add_field(name="Commands I react to:", value="!phb, !roll d4....")
    await ctx.send(embed=embed)

@client.command()
async def phb(ctx):
    await ctx.send("A link to the player's handbook: http://orc-news.ru/dnd5eng.pdf")

@client.command() # TOIMII
async def d4(ctx):
    d4 = list(range(1,5))
    await ctx.send(random.choice(d4))

@client.command() # TOIMII
async def d6(ctx):
    d6 = list(range(1,7))
    await ctx.send(random.choice(d6))

@client.command() # TOIMII
async def d8(ctx):
    d8 = list(range(1,9))
    await ctx.send(random.choice(d8))

@client.command() # TOIMII
async def d10(ctx):
    d10 = list(range(1,11))
    await ctx.send(random.choice(d10))

@client.command() # TOIMII
async def d12(ctx):
    d12 = list(range(1,13))
    await ctx.send(random.choice(d12))

@client.command() # TOIMII
async def d20(ctx):
    d20 = list(range(1,21))
    await ctx.send(random.choice(d20))

@client.command() # TOIMII
async def d100(ctx):
    d100 = list(range(1,101))
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

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print(f"{name} has finished playing"))
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
