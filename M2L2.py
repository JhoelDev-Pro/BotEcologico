import discord
from discord.ext import commands
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def Hola(ctx):
    await ctx.send("Hola soy tu bot ecologico")

@bot.command()
async def reciclar(ctx, objeto: str):
    clasificacion = {
        "botella": "♻️ Va al contenedor de PLÁSTICO.",
        "papel": "📄 Va al contenedor de PAPEL.",
        "cáscara": "🍌 Va al contenedor ORGÁNICO.",
        "pilas": "⚠️ Las PILAS deben ir a un punto especial de reciclaje."
    }
    
    respuesta = clasificacion.get(objeto.lower, "Noce donde va este papel")

    await ctx.send(respuesta)

@bot.command()
async def tiempo(ctx, objeto: str):
  
    degradacion = {
        "botella": "🍼 Una botella de plástico tarda ¡450 años! en degradarse 😱",
        "papel": "📄 El papel tarda unos 2 a 6 meses.",
        "cáscara": "🍌 Una cáscara tarda solo unas semanas.",
        "pilas": "⚠️ Las pilas pueden tardar ¡1000 años! y además contaminan el suelo."
    }

    respuesta = degradacion.get(objeto.lower, "Noce")
    await ctx.send(respuesta)
bot.run(TOKEN)