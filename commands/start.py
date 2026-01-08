"""
/start command implementation
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from keyboards import get_start_keyboard

logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command - EXACTLY as specified"""
    user = update.effective_user
    
    # First message: greeting (EXACT format)
    greeting_msg = f"<b>💓 Hello 🎖️⚡</b> {user.first_name} <b>!!!🎉, 😁 Welcome to 💨 DEV•ZIKKY Bot✨✨🔥.</b>"
    await update.message.reply_text(greeting_msg, parse_mode="HTML")
    
    # Second message: join requirement (EXACT format)
    requirement_msg = "🚫 <b>You must join the required channels and group first to use our bot.</b>\n\nOnce you've joined all of them, click on 🔄 Refresh Status⚡ to move on💨💨."
    await update.message.reply_text(
        requirement_msg,
        parse_mode="HTML",
        reply_markup=get_start_keyboard()
    )
    
    logger.info(f"User {user.id} started bot")
    return True