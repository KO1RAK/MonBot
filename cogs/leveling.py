import discord
from discord.ext import commands
import json
from pathlib import Path

XP_FILE = Path("leveling.json")

def load_xp():
    if not XP_FILE.exists():
        return {}
    with XP_FILE.open("r") as f:
        return json.load(f)

def save_xp(data):
    with XP_FILE.open("w") as f:
        json.dump(data, f, indent=4)

class Leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.xp_data = load_xp()

    def get_level(self, xp):
        level = 0
        while xp >= self.xp_for_level(level + 1):
            level += 1
        return level

    def xp_for_level(self, level):
        return 5 * (level ** 2) + 50 * level + 100

    async def give_xp(self, user, amount):
        uid = str(user.id)
        if uid not in self.xp_data:
            self.xp_data[uid] = {"xp": 0, "level": 0}
        
        user_data = self.xp_data[uid]
        user_data["xp"] += amount

        new_level = self.get_level(user_data["xp"])
        if new_level > user_data["level"]:
            user_data["level"] = new_level
            await user.send(f"🎉 You leveled up to level {new_level}!")

        save_xp(self.xp_data)

    @commands.command(name="level")
    async def level(self, ctx):
        uid = str(ctx.author.id)
        user_data = self.xp_data.get(uid, {"xp": 0, "level": 0})
        xp = user_data["xp"]
        level = user_data["level"]
        next_xp = self.xp_for_level(level + 1)
        await ctx.send(f"{ctx.author.mention} — Level {level} | {xp}/{next_xp} XP")

@commands.command(name="leaderboard")
async def leaderboard(self, ctx):
    # Get top 10 users sorted by XP
    top = sorted(self.xp_data.items(), key=lambda x: x[1]["xp"], reverse=True)[:10]

    lines = ["🏆 **Leaderboard**"]
    for i, (user_id, data) in enumerate(top, start=1):
        try:
            user = await self.bot.fetch_user(int(user_id))  # Fetch full user object
            name = user.name
        except:
            name = f"User ID: {user_id}"

        lines.append(f"{i}. **{name}** — Level {data['level']} — {data['xp']} XP")

    await ctx.send("\n".join(lines))

async def setup(bot):
    await bot.add_cog(Leveling(bot))
