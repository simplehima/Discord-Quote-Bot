import os
import discord
from discord.ext import commands
import requests
import schedule
import time
import json

# Add your bot token here
TOKEN = ''
# Replace with your desired role ID (integer)
ROLE_ID = 123456789
# Add the text channel ID where the bot should send messages
TEXT_CHANNEL_ID = 123456789 # Replace with your text channel ID (integer)

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)
# Fetch a random quote and return it as a string
def get_quote():
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    quote_data = response.json()
    quote = f'"{quote_data["content"]}" - {quote_data["author"]}'
    return quote

# Fetch a random image related to the quote and return its URL
def get_related_image(quote):
    # Replace this with your Unsplash API key
    unsplash_access_key = ''
    search_query = quote.split()[0] # Use the first word of the quote as the search query
    url = f'https://api.unsplash.com/photos/random?query={search_query}&client_id={unsplash_access_key}'
    response = requests.get(url)
    image_data = response.json()
    image_url = image_data['urls']['small']
    return image_url

# Send the quote and image to the specified text channel
async def send_quote_and_image():
    channel = bot.get_channel(TEXT_CHANNEL_ID)
    role = discord.utils.get(channel.guild.roles, id=ROLE_ID)
    quote = get_quote()
    image_url = get_related_image(quote)
    embed = discord.Embed(title=quote, color=discord.Color.blue())
    embed.set_image(url=image_url)
    await channel.send(f'{role.mention}', embed=embed)

# Schedule the bot to send the quote and image every 12 hours
schedule.every(12).hours.do(lambda: bot.loop.create_task(send_quote_and_image()))

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await send_quote_and_image()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)
