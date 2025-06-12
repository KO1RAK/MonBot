import discord
from discord.ext import commands
import json
from pathlib import Path

XP_FILE = Path("leveling.json")

class CustomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.xp_data = self.load_xp()

    def load_xp(self):
        if not XP_FILE.exists():
            return {}
        with XP_FILE.open("r") as f:
            return json.load(f)

    def get_level(self, xp):
        level = 0
        while xp >= self.xp_for_level(level + 1):
            level += 1
        return level

    def xp_for_level(self, level):
        return 5 * (level ** 2) + 50 * level + 100

    @commands.command(name="hi")
    async def hi(self, ctx):
        await ctx.send(f"Hey {ctx.author.mention}, hope you're doing great!")

    @commands.command(name="hello")
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}! 👋")

    @commands.command(name="canwebebesties")
    async def canwebebesties(self, ctx):
        await ctx.send(f"yes we can bestie {ctx.author.mention}! ❤")

    @commands.command(name="killlewis")
    async def killlewis(self, ctx):
        await ctx.send(f"yes master i will kill lewis")

    @commands.command(name="gather")
    async def gather(self, ctx):
        await ctx.send(f"good day people it is now time for our gathering")

async def setup(bot):
    await bot.add_cog(CustomCommands(bot))
