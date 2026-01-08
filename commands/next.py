"""
/next command implementation with channel verification
"""

import logging
import random
from telegram import Update
from telegram.ext import ContextTypes
from config import REQUIRED_CHATS, SONGS, WELCOME_IMAGE, OWNER
from keyboards import get_start_keyboard, get_welcome_keyboard

logger = logging.getLogger(__name__)

async def check_membership(user_id: int, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """
    Check if user is member of all required chats
    Uses numeric chat IDs and validates allowed statuses
    """
    for chat_id in REQUIRED_CHATS:
        try:
            member = await context.bot.get_chat_member(
                chat_id=int(chat_id),
                user_id=user_id
            )
            
            # Accept only statuses that mean user is actually in the chat
            if member.status not in ["creator", "administrator", "member"]:
                logger.info(f"User {user_id} not in chat {chat_id}, status: {member.status}")
                return False
                
        except Exception as e:
            logger.error(f"Error checking membership for chat {chat_id}: {e}")
            # If bot can't access chat, assume not member for security
            return False
    
    return True

async def next_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle /next command - Check membership and show welcome menu
    """
    user = update.effective_user
    
    # Check if called from callback query or command
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        chat_id = query.message.chat_id
        message_id = query.message.message_id
    else:
        chat_id = update.message.chat_id
        message_id = None
    
    # Show checking message
    if update.callback_query:
        await context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="🔍 <b>Checking your membership...</b>\n⏳ Please wait...",
            parse_mode="HTML"
        )
    else:
        temp_msg = await context.bot.send_message(
            chat_id=chat_id,
            text="🔍 <b>Checking your membership...</b>\n⏳ Please wait...",
            parse_mode="HTML"
        )
        message_id = temp_msg.message_id
    
    # Verify membership
    is_member = await check_membership(user.id, context)
    
    if not is_member:
        error_msg = "🚫 You still haven't joined all required channels/groups.\n\nPlease join them first, then click 🔄 Refresh Status⚡ again."
        
        if update.callback_query:
            await context.bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=error_msg,
                reply_markup=get_start_keyboard()
            )
        else:
            await context.bot.send_message(
                chat_id=chat_id,
                text=error_msg,
                reply_markup=get_start_keyboard()
            )
        return
    
    # ✅ User has joined all required chats
    
    # Send welcome image
    try:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=WELCOME_IMAGE,
            caption="🥂 Welcome Dear User😊 to <b>DEV•ZIKKY Bot</b> ✅",
            parse_mode="HTML"
        )
    except Exception as e:
        logger.error(f"Error sending welcome image: {e}")
    
    # Send welcome message with menu
    welcome_text = (
        "<b>🥂 Welcome Dear User😊 to DEV•ZIKKY Bot ✅</b>\n\n"
        "🤖 About This Bot;\n"
        "Hey there! 👋 I'm a smart Telegram bot built to make things easier for you — fast, simple, and reliable.\n\n"
        "I can:\n"
        "• Help you download media or get information 🔍\n"
        "• Work 24/7 without needing rest ⚡\n\n"
        "🚀 Type /menu to see the bot's list of commands\n\n"
        f"🔥 <b>Powered By: <a href=\"{OWNER['url']}\">DEV•ZIKKY🥂</a></b> ❤️"
    )
    
    if update.callback_query:
        await context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=welcome_text,
            parse_mode="HTML",
            disable_web_page_preview=False,
            reply_markup=get_welcome_keyboard()
        )
    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text=welcome_text,
            parse_mode="HTML",
            disable_web_page_preview=False,
            reply_markup=get_welcome_keyboard()
        )
    
    # Send random audio
    random_song_url = random.choice(SONGS)
    
    try:
        await context.bot.send_audio(
            chat_id=chat_id,
            audio=random_song_url,
            title="RANDOM AUDIO.mp3",
            performer="DEV•ZIKKY",
            caption="▶ Play / Download 📥",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Download / Open", url=random_song_url)]
            ])
        )
    except Exception as e:
        logger.error(f"Error sending audio: {e}")
    
    logger.info(f"User {user.id} verified and shown welcome menu")
    return True