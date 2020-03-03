# bot.py
import os
import random
import sys

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# sys.stdout.write("Token = " + token + "\n")

bot = commands.Bot(command_prefix='!')


@bot.command(name='roll_dice', help='!roll_dice <number of dice> <number of sides>')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.command(name='verse', help='Responds with a random Bible quote')
async def bible_verse(ctx):
    bible_quotes = [
        (
            '```Be devoted to one another in love. Honor one another above yourselves.\n'
            ' - Romans 12:10```'
        ),

    ]

    response = random.choice(bible_quotes)
    await ctx.send(response)


bot.run(token)
