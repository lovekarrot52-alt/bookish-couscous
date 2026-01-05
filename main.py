import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Discord Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)


Thread(target=run_flask).start()


TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} запущен!')


bot.run(TOKEN)
