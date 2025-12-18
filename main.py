# main.py
import discord
from discord.ext import commands
from cryptography.fernet import Fernet
import base64

VOICE_CHANNEL_ID = 1440353376822104184

# Вставь СЮДА свой ENCRYPTED_TOKEN из encrypt.py
ENCRYPTED_TOKEN = b'gAAAAABpQ-QdIwxnPX3SvVdc7bhpJacmTaabifK7eO7oCjFNzZUIXszgJXCn2Lw8oYowpfsm0MerCauN-GEZ00KIMkU7M1BIOuJLjo7_oJqn-bpSXCgh4OgxxO_LW02JSmRVCSB6qZR3z0RwRnm37cQmoVLBTcWL_nnIgmAzcYJC3PbxWKrYaBU='

# Вставь СЮДА свои части из encrypt.py
p1 = "my_super"
p2 = "_secret_"
p3 = "key_for_"
p4 = "bot_2025"

raw_key = (p1 + p2 + p3 + p4)[:32].encode()
key = base64.urlsafe_b64encode(raw_key.ljust(32, b'0'))

try:
    cipher = Fernet(key)
    TOKEN = cipher.decrypt(ENCRYPTED_TOKEN).decode()
except Exception as e:
    print("❌ Ошибка расшифровки:", e)
    exit(1)

# ... остальной код бота (как у тебя был)
intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, activity=discord.Game(name="Visual Studio Code"))

@bot.event
async def on_ready():
    print(f'✅ {bot.user} запущен!')
    channel = bot.get_channel(VOICE_CHANNEL_ID)
    if channel and not channel.guild.voice_client:
        await channel.connect()
        print(f'🎧 Подключён к: {channel.name}')

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Вышел из голосового канала.")

bot.run(TOKEN)
