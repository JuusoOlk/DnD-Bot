import discord
import os
from events import *

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = read_token()

on_message()

#on_ready()

client.run(token)
