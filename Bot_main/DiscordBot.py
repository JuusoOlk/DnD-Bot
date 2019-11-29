import discord

client = discord.Client()
@client.event
async def on_message(message):
    if message.content.find(":smile:") != -1:
        await message.channel.send("Hi :) Keep the positive mindset!") # If the user says !hello we will send back hi
    print(message.content) # Now every message sent will be printed to the console
client.run("NjQ5NjEyOTI0NDY5NTEwMTY1.XeEZ3A.tThmbyFuSJr1AgEm8Y-5NuR5s8M")
