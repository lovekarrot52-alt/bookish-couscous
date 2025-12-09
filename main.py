import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

# Flask сервер для поддержания работы
app = Flask('')

@app.route('/')
def home():
    return "Discord Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Запуск Flask в отдельном потоке
Thread(target=run_flask).start()

# Discord бот
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} запущен!')

# Ваш основной код защиты...

bot.run(TOKEN)
