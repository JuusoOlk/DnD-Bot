import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
from os import system
import shutil
import youtube_dl
import os
import random
import asyncio
import sqlite3
from ctypes.util import find_library

# Libraries used: asyncio, youtubedl
# discord.py framework
#SQLite database

# Prefix defines the key for commanding the bot e.g. !play
client = commands.Bot(command_prefix='!')

# Reads the unique discord client token from the text-file
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

dclient = Bot('!')

# Connects to the SQLite-database
conn = sqlite3.connect('diceroll.db')
c = conn.cursor()

# Tries to create a database if it is the first time the application runs
try:
    c.execute('''CREATE TABLE dice
                 (fname text,
                 d4 int,
                 d6 int,
                 d8 int,
                 d10 int,
                 d12 int,
                 d20 int,
                 d100 int)''')
except:
    print("table already exists")

c.execute('SELECT * FROM dice')

# Inserts database values into the diceresult variable
diceresult = c.execute('SELECT * FROM dice').fetchall()
print(diceresult)

# Informs the admin about the bot being online in command prompt
@client.event
async def on_ready():
    print(f'{client.user.name} is online!')

# Shows the bot information
@client.command()
async def bot_info(ctx):
    embed = discord.Embed(title="DnD-Bot", description="Making DnD easier :)")
    embed.add_field(name="Commands I react to:", value="!play, !d4...")
    await ctx.send(embed=embed)

# Gives the user a link to DnD player's handbook
@client.command()
async def phb(ctx):
    await ctx.send("A link to the player's handbook: http://orc-news.ru/dnd5eng.pdf")

# Picks a random song from a list depending genre (mobile phone user friendly)
@client.command()
async def heroic(ctx):
    heroic = ["https://open.spotify.com/track/29gW6N4TtGhpkYmYwhRvDL?si=iGc9ASDUQu2VVa7QozaGRg", "https://open.spotify.com/track/4JtvyWkWQTPVcroZf8JJkp?si=N30P6Q_JT0CNnc8N0VBF9g", "https://open.spotify.com/track/2jn89xTHIVsy167uOmAewt?si=iVbs2iivT5eyu35MCqPKrA", "https://open.spotify.com/track/1YtHpYEbbfQQIyxXkdxEoW?si=zWzC7hnLSpSNc5nfj8nwvQ", "https://open.spotify.com/track/3pTNVDJpzaLxiZnbC18SMX?si=WWBjGMXqTDG19-FhbEp3SA", "https://open.spotify.com/track/2ZssT3XEX1cObqahy9YrQM?si=hplZhcrHRgCNyGT7-W6SjQ", "https://open.spotify.com/track/0G8iyOJFQ8Wvm4Fe6xjQdr?si=CjjUIecdRxyQ_Zy07muxAw", "https://open.spotify.com/track/2F9xBxKbx2M0pbgtSu8fLf?si=d6tLHZMyQSCoRlfoVsDr3w", "https://open.spotify.com/track/3GJZLvGXaVszYdSBLMtJFX?si=4uVSIjm5Tey0Ykvc3bYH4g", "https://open.spotify.com/track/2k2Pwkt3Fqowcve91PiH4g?si=wSJjbyoiTv6o_JISrRIMdQ", "https://open.spotify.com/track/1l2g97tNnO52U1IS0y9GRL?si=zaa7CBA3RlS2WUY4Bxadzw", "https://open.spotify.com/track/1No2I2TNhCXDNovL5O7ang?si=0dY850i8TVuC34l88yk4DA", "https://open.spotify.com/track/3jKkPcETVg1I9RR7ECgE4b?si=qSfGtzwHR4mtVESXNa66Gw"]
    await ctx.send(random.choice(heroic))
# Another little list for a different genre

@client.command()
async def tavern(ctx):
    tavern = ["https://open.spotify.com/track/396qEVyZ1I7W6fNE12APdO?si=dI3xM_v9QcmT0lWeQ_WpSA", "https://open.spotify.com/track/4pW1ftcpCJt1VxbPwVknz0?si=mhyy92-RS7uijJpRYSJfQQ", "https://open.spotify.com/track/7z7WfdoT4qI16aXfWoNRlj?si=E_eVuNZIRrW-PlYMQBvRYw", "https://open.spotify.com/track/7Lp3BqKR2VE1NNd2LDuvzb?si=0ASpEeP3Tzi6K2UAVmZAzQ", "https://open.spotify.com/track/2TLO035tumZKpxxeDlKYQb?si=o72w9mXPQTSK7rGjMmXUhw", "https://open.spotify.com/track/1FdX2jpsp9Gt1rHxUROE6n?si=_-B6igUBRo6eFRa41TbAnQ", "https://open.spotify.com/track/1FV2g6zFu0ThzLMK4apEEy?si=hX6K-029S4STvdFPMap4Gg", "https://open.spotify.com/track/6ZBvQOuEp4ggTYAsqq0YFa?si=eB9uvq20QSSXxGZ4lmUJ4A", "https://open.spotify.com/track/3q79jp15s3gBLddLosTPP5?si=LrKwxK2ESZ2SqxHnwNPj8A", "https://open.spotify.com/track/08m0MIad094kPXhjwWi6Gu?si=LMzCgTbCS2SF7SdJ3V3Pxg"]
    await ctx.send(random.choice(tavern))

# Prints all the results from the dice roll SQLite-database
@client.command()
async def alldice(ctx):
    diceresult = c.execute( 'SELECT * FROM dice').fetchall()
    await ctx.send(diceresult)

# Commands to print 4-, 6-, 8-, 10-, 12-, 20- and 100 sided dice (the rest of the code below)
# Chooses a random number between the given range
# Inserts the rolled dice under the rollers discord username into the database
@client.command()
async def d4(ctx):
    d4 = list(range(1, 5))
    d4result = random.choice(d4)
    fname = str(ctx.message.author)
    c.execute("INSERT INTO dice(fname, d4) VALUES ('%s', '%d')"%(fname, d4result))
    diceresult = c.execute( 'SELECT * FROM dice').fetchall()
    conn.commit()
    await ctx.send(d4result)


@client.command()
async def d6(ctx):
    d6 = list(range(1, 7))
    d6result = random.choice(d6)
    fname = str(ctx.message.author)
    c.execute("INSERT INTO dice(fname, d6) VALUES ('%s', '%d')"%(fname, d6result))
    diceresult = c.execute( 'SELECT * FROM dice').fetchall()
    conn.commit()
    await ctx.send(d6result)


@client.command()
async def d8(ctx):
    d8 = list(range(1, 9))
    d8result = random.choice(d8)
    fname = str(ctx.message.author)
    c.execute("INSERT INTO dice(fname, d8) VALUES ('%s', '%d')"%(fname, d8result))
    diceresult = c.execute( 'SELECT * FROM dice').fetchall()
    conn.commit()
    await ctx.send(d8result)

@client.command()
async def d10(ctx):
    d10 = list(range(1, 11))
    d10result = random.choice(d10)
    fname = str(ctx.message.author)
    c.execute("INSERT INTO dice(fname, d10) VALUES ('%s', '%d')"%(fname, d10result))
    diceresult = c.execute( 'SELECT * FROM dice').fetchall()
    conn.commit()
    await ctx.send(d10result)


@client.command()
async def d12(ctx):
    d12 = list(range(1, 13))
    d12result = random.choice(d12)
    fname = str(ctx.message.author)
    c.execute("INSERT INTO dice(fname, d12) VALUES ('%s', '%d')"%(fname, d12result))
    diceresult = c.execute( 'SELECT * FROM dice').fetchall()
    conn.commit()
    await ctx.send(d12result)

@client.command()
async def d20(ctx):
    d20 = list(range(1, 21))
    d20result = random.choice(d20)
    fname = str(ctx.message.author)
    c.execute("INSERT INTO dice(fname, d20) VALUES ('%s', '%d')"%(fname, d20result))
    diceresult = c.execute( 'SELECT * FROM dice').fetchall()
    conn.commit()
    await ctx.send(d20result)


@client.command()
async def d100(ctx):
    d100 = list(range(1, 101))
    d100result = random.choice(d100)
    fname = str(ctx.message.author)
    c.execute("INSERT INTO dice(fname, d100) VALUES ('%s', '%d')"%(fname, d100result))
    diceresult = c.execute( 'SELECT * FROM dice').fetchall()
    conn.commit()
    await ctx.send(d100result)

# Command to invite the bot to the voice channel
@client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

# If the bot is connected to another voice channel, moves it to the wanted channel
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

# Informs the users that the bot joined a channel
    await ctx.send(f"Joined {channel}")

# Commands the bot to leave the voice channel
@client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

# Informs the users that the bot has left the channel and mentions the disconnected channel's name
# If the bot is not in a voice channel and is commanded to leave, it sends a message to the channel about not being able to leave
    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Don't think I am in a voice channel")

# Commands the bot to play the wanted Youtube-link with !play "--link--"
@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

# Bot checks if an earlier queue exists and informs if no queue exists
    def check_queue():

        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_que = length - 1
            try:
                first_file = os.listdir(DIR)[0]
            except:
# Bot clears the queue before starting to play a new link
                print("No songs in queue!\n")
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
            if length != 0:
                print("Playing next song in queue!\n")
                print(f"Queued songs: {still_que}")
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                    shutil.move(song_path, main_location)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, 'song.mp3')
# Uses the ffmpeg-codec library to convert the link into MP3-file
                voice.play(discord.FFmpegPCMAudio("song.mp3"),
                           after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.05

            else:
                queues.clear()
                return

        else:
            queues.clear()
            print("Queue empty!\n")

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed old song file")
    except PermissionError:
        print("Trying to remove song file, but it is being played")
        await ctx.send("ERROR: Music Playing")
        return

# Defines a Queue-folder where the song.mp3 will later be added to
    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:
            print("Cleared queue folder!")
            shutil.rmtree(Queue_folder)
    except:
        print("No queue folder to clear!")

    await ctx.send("Getting everything ready to rock!")

    voice = get(client.voice_clients, guild=ctx.guild)

# youtubedl-settings to set the quality and the extraction for the played link
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

# Informs the admin in the command prompt about starting to download the given link
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

# Takes the downloaded link and renames it to song.mp3
# The rename is mandatory for the client to be able to play the link without knowing the name
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"),
               after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.05

# Splits the link name to make it more readable and then informs the channel about the actual name of the played link
    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("Playing\n")

# Commands the bot to pause the audio
@client.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

# The bot checks if the audio is played or not and if it is being played, pauses it
# If an audio is not playing, the bot tells the channel about failed pause
    if voice and voice.is_playing():
        print("Song paused")
        voice.pause()
        await ctx.send("Song paused")
    else:
        print("Song is not playing, failed pause")
        await ctx.send("Song is not playing, failed pause")

# Pause function to pause the currently played audio
@client.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

# If the audio is paused, resumes playing it
    if voice and voice.is_paused():
        print("Song resumed")
        voice.resume()
        await ctx.send("Song resumed")
    else:
        print("Song is not paused")
        await ctx.send("Song is not paused")

# Stop function to stop or skip the current played audio (skips the audio in case a queue exists)
@client.command(pass_context=True, aliases=['s', 'sto'])
async def stop(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    queues.clear()

    if voice and voice.is_playing():
        print("Song stopped/skipped")
        voice.stop()
        await ctx.send("Song stopped/skipped")
    else:
        print("Song is not playing, failed stop")
        await ctx.send("Song is not playing, failed stop")

queues = {}

# Commands the bot to queue next audio, adding it to the queue
@client.command(pass_context=True, aliases=['q', 'que'])
async def queue(ctx, url:str):
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is False:
            os.mkdir("Queue")
        DIR = os.path.abspath(os.path.realpath("Queue"))
        q_num = len(os.listdir(DIR))
# q_num shows the audio's position in queue
        q_num += 1
        add_queue = True
        while add_queue:
            if q_num in queues:
                q_num += 1
            else:
                add_queue = False
                queues[q_num] = q_num

        queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'outtmpl': queue_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
        await ctx.send("Adding song" + str(q_num) + " to the que!")

        print("Successfully added a song to que :)\n")

client.run(token)
# Closes the database connection
conn.close()
