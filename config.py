import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env file content into environment variables

# Discord bot token from .env
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN not found in environment variables!")

# XP settings
XP_PER_MESSAGE = 1            # XP gained per eligible message
XP_COOLDOWN_SECONDS = 30      # Cooldown per user before gaining XP again

# Role rewards: map level thresholds to role IDs (Discord snowflake IDs)
# Replace the example IDs with your actual role IDs from your server
ROLE_REWARDS = {
    5: 123456789012345678,    # Level 5 gets this role
    10: 234567890123456789,   # Level 10 role
    20: 345678901234567890    # Level 20 role
}

# Other bot settings
PREFIX = "!"                 # Not used much with slash commands but good to keep

# File paths
XP_DATA_FILE = "leveling.json"

# Optional: Logging level
LOG_LEVEL = "INFO"
