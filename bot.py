#!/usr/bin/env python3
"""
DEV•ZIKKY Bot - Main Application
Deploy on Render via GitHub
"""

import os
import logging
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Import configuration
from config import TOKEN
from commands import start_command, next_command

# ================= LOGGING =================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ================= CALLBACK HANDLER =================
async def callback_handler(update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all button callbacks"""
    query = update.callback_query
    data = query.data
    
    if data == "next":
        await next_command(update, context)
    elif data == "menu":
        await query.answer("Menu feature coming soon! ⚡")
    elif data == "ping":
        await query.answer("Pong! 🏓")
    elif data == "ai":
        await query.answer("AI Menu coming soon! 🤖")
    elif data == "profile":
        await query.answer("Profile feature coming soon! 📊")
    elif data == "group":
        await query.answer("Group management coming soon! 👥")
    elif data == "fun":
        await query.answer("Fun menu coming soon! 🤭")
    elif data == "sticker":
        await query.answer("Sticker zone coming soon! 🤪")
    elif data == "sound":
        await query.answer("Sound changer coming soon! 🔊")
    elif data == "economy":
        await query.answer("Economy menu coming soon! 💰")
    elif data == "owner":
        await query.answer("Owner menu coming soon! 🏅")
    elif data == "anime":
        await query.answer("Anime arena coming soon! 🎉")
    elif data == "togroup":
        await query.answer("Add to group feature coming soon! ➕")
    elif data == "download":
        await query.answer("Download menu coming soon! 📥")
    elif data == "game":
        await query.answer("Game center coming soon! 🎮")
    elif data == "premium":
        await query.answer("Premium plan coming soon! 🌈")
    elif data == "special":
        await query.answer("Special commands coming soon! 🔥")
    else:
        await query.answer("Button clicked! ⚡")

# ================= ERROR HANDLER =================
async def error_handler(update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors"""
    logger.error(f"Update {update} caused error {context.error}")

# ================= MAIN =================
def main():
    """Start the bot"""
    print("=" * 50)
    print("🤖 DEV•ZIKKY Bot - Starting...")
    print("=" * 50)
    
    # Get token from environment
    token = os.getenv("TOKEN")
    if not token:
        print("❌ ERROR: TOKEN environment variable not set!")
        print("Please set TOKEN in Render environment variables")
        exit(1)
    
    # Create Application
    app = Application.builder().token(token).build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("next", next_command))
    
    # Add callback handler
    app.add_handler(CallbackQueryHandler(callback_handler))
    
    # Add error handler
    app.add_error_handler(error_handler)
    
    print("✅ Bot configured successfully!")
    print("📁 Commands loaded: /start, /next")
    print("🔄 Starting bot...")
    print("=" * 50)
    
    # Run bot
    app.run_polling(allowed_updates=['message', 'callback_query'])

if __name__ == '__main__':
    main()