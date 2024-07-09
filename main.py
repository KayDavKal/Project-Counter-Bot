import discord
from discord.ext import commands
from discord import app_commands
from count import *
import os

token = os.environ['token']
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@tree.command(name="count", description="Get current project count")
async def count(ctx):
  number = await getCount()
  embed = discord.Embed(
    title = "Current Project Count",
    description = f"The current count is at ``{number}``",
    color = discord.Color.random()
  )
  await ctx.response.send_message(embed=embed)

@client.event
async def on_message(message):
  if ("suggest" in message.content or "recommend" in message.content) and "project" in message.content:
    await addCount()
    print("added")

@client.event
async def on_ready():
  await table()
  await tree.sync()
  print("Ready!")

client.run(token)
