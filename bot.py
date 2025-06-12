import discord
from discord.ext import commands
import config
import os

intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content for leveling

bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.event
async def on_message(message):
    if message.author.bot or message.guild is None:
        return

    leveling_cog = bot.get_cog("Leveling")
    if leveling_cog:
        await leveling_cog.give_xp(message.author, 10)

    await bot.process_commands(message)

async def load_cogs():
    for extension in ["cogs.leveling", "cogs.custom_commands"]:
        try:
            await bot.load_extension(extension)
            print(f"Loaded extension: {extension}")
        except Exception as e:
            print(f"Failed to load extension {extension}: {e}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(config.TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())