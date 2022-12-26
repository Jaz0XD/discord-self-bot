import discord
from discord.ext import commands
import dotenv

bot = commands.Bot(command_prefix = '>', self_bot = True)

@bot.event 
async def on_ready():
    print('_' * 20)
    print('Logged in as ')
    print(f'User: {bot.user.name}')
    print(f'ID: {bot.user.id}' )
    print('_' * 20)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

TOKEN = 'NzU5OTg1NzU1NTg1NzczNjEw.Gp7qDX.MkyiTWCrFKJHYrL1GjOHbIg9RkXOhmvlW-GNgk'
bot.run(TOKEN)

# NzU5OTg1NzU1NTg1NzczNjEw.Gp7qDX.MkyiTWCrFKJHYrL1GjOHbIg9RkXOhmvlW-GNgk