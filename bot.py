import os

from discord.ext import commands
from dotenv import load_dotenv

from scrape import dolar
from send_wp import msg

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')


@bot.command(name="1")
async def dolar_v(value):

    await value.send(dolar)


@bot.command(name="hi")
async def msg_dc(value):
    
    msg_class = msg()

    msg_class.msg_hi()

    await value.send("Your Message is Sent !")


bot.run(TOKEN)
