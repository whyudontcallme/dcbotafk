# bot.py
import discord
from discord.ext import commands
from datetime import datetime, timezone

# === НАСТРОЙКИ ===
TOKEN = "MTI0ODY2Njk5NTczODgwODQ2MQ.GAMf2s.jtvYfgO9D30wGGzvoJF7Fn0e7Oh4NZiuJQ8LJU"  # ← ЗАМЕНИ НА СВОЙ ТОКЕН!
VOICE_CHANNEL_ID = 1440353376822104184  # ← ЗАМЕНИ НА ID ТВОЕГО ГОЛОСОВОГО КАНАЛА

# === НАСТРОЙКА БОТА ===
intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    status=discord.Status.online,
    activity=discord.Game(name="Visual Studio Code")  # → «Играет в Visual Studio Code»
)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} запущен и в сети!')
    
    # Подключаемся к голосовому каналу
    channel = bot.get_channel(VOICE_CHANNEL_ID)
    if not channel:
        print("❌ Голосовой канал не найден! Проверь ID.")
        return

    if channel.guild.voice_client:
        print("🔊 Уже в голосовом канале.")
        return

    try:
        await channel.connect()
        print(f'🎧 Подключился к голосовому каналу: {channel.name}')
    except Exception as e:
        print(f"⚠️ Ошибка подключения: {e}")

# Команда для выхода из голоса
@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Вышел из голосового канала.")
    else:
        await ctx.send("Я не в голосе.")

# Запуск
bot.run(TOKEN)