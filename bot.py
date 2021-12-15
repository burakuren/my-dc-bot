import os

from discord.ext import commands
from dotenv import load_dotenv

from scrape import dolar

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')


@bot.command(name="1")
async def dolar_v(value):

    await value.send(dolar)



bot.run(TOKEN)
