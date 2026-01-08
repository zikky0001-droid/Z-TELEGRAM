"""
Keyboard layouts for DEV•ZIKKY Bot
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import CHANNELS, OWNER

def get_start_keyboard():
    """Keyboard for /start command"""
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel 1", url=CHANNELS["channel1"]["url"])],
        [InlineKeyboardButton("📢 Join Channel 2", url=CHANNELS["channel2"]["url"])],
        [InlineKeyboardButton("👥 Join Group", url=CHANNELS["group"]["url"])],
        [InlineKeyboardButton("🔄 Refresh Status ⚡", callback_data="next")],
        [InlineKeyboardButton("💬 Contact Owner/Developer", url=OWNER["url"])]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_welcome_keyboard():
    """Main welcome menu keyboard (2x2 layout)"""
    keyboard = [
        [
            InlineKeyboardButton("🌟 BOT-MENU", callback_data="menu"),
            InlineKeyboardButton("💨 PING", callback_data="ping")
        ],
        [
            InlineKeyboardButton("🤖 AI MENU", callback_data="ai"),
            InlineKeyboardButton("📊 PROFILE INFO", callback_data="profile")
        ],
        [
            InlineKeyboardButton("👥 GROUP MANAGEMENT", callback_data="group"),
            InlineKeyboardButton("🤭 FUN MENU", callback_data="fun")
        ],
        [
            InlineKeyboardButton("🤪 STICKER ZONE", callback_data="sticker"),
            InlineKeyboardButton("🔊 SOUND CHANGER", callback_data="sound")
        ],
        [
            InlineKeyboardButton("💰 ECONOMY MENU", callback_data="economy"),
            InlineKeyboardButton("🏅 OWNER MENU", callback_data="owner")
        ],
        [
            InlineKeyboardButton("🎉 ANIME ARENA", callback_data="anime"),
            InlineKeyboardButton("➕ ADD TO GROUP CHAT", callback_data="togroup")
        ],
        [
            InlineKeyboardButton("📩 DOWNLOAD MENU", callback_data="download"),
            InlineKeyboardButton("🎮 GAME CENTER", callback_data="game")
        ],
        [
            InlineKeyboardButton("🌈 PREMIUM PLAN 🍀", callback_data="premium"),
            InlineKeyboardButton("🔥 SPECIAL COMMANDS", callback_data="special")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)