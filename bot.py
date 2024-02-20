import discord
import os
from cogs import *
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.add_cog(Urban(bot))
    await bot.add_cog(Text(bot))
    await bot.add_cog(Eight(bot))
    await bot.add_cog(General(bot))
    print(f'Logged on as {bot.user}')

def main():
    bot.run(os.getenv('TOKEN'))

if __name__ == '__main__':
    main()

