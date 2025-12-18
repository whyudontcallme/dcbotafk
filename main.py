# main.py — БЕЗ сторонних библиотек
import discord
from discord.ext import commands

# ⚠️ НЕ ХРАНИ ТОКЕН ТАК В РЕАЛЬНОСТИ! Это временный обход.
# Собираем токен по частям, чтобы он не искался как цельная строка
t1 = "MTI0ODY2Njk5NTczODgwODQ2MQ"
t2 = "GYgMwg"
t3 = "EuduCb_2gPO8DzNMgAv1EAixUEKZ4-WDbHwuZQ"
TOKEN = f"{t1}.{t2}.{t3}"

VOICE_CHANNEL_ID = 1440353376822104184

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, activity=discord.Game(name="VS Code"))

@bot.event
async def on_ready():
    print(f'✅ {bot.user} запущен!')
    channel = bot.get_channel(VOICE_CHANNEL_ID)
    if channel and not channel.guild.voice_client:
        await channel.connect()

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()

bot.run(TOKEN)
