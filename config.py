"""
Configuration file for DEV•ZIKKY Bot
"""

# Telegram Bot Token (set as TOKEN environment variable in Render)
TOKEN = None  # Will be set from environment

# Required channels/groups with numeric IDs
REQUIRED_CHATS = [
    "-1003275779062",  # Channel 1 numeric ID
    "-1002773387023",  # Channel 2 numeric ID  
    "-1002820365462"   # Group numeric ID
]

# Channel usernames for URLs
CHANNELS = {
    "channel1": {
        "name": "@zikkycal",
        "url": "https://t.me/zikkycal"
    },
    "channel2": {
        "name": "@otp_ch1",
        "url": "https://t.me/otp_ch1"
    },
    "group": {
        "name": "@f_9tp1",
        "url": "https://t.me/f_9tp1"
    }
}

# Owner info
OWNER = {
    "username": "@Zikkystar1",
    "url": "https://t.me/Zikkystar1"
}

# Welcome image
WELCOME_IMAGE = "https://ik.imagekit.io/2qum88wz3c/IMG_20251112_224308_546.jpg?updatedAt=1762985017430"

# Songs for random audio
SONGS = [
    "https://archive.org/download/dia-deli-cia_202511/DIA%20DEL%C3%8DCIA.mp3",
    "https://archive.org/download/montagem-xonada_202511/MONTAGEM%20XONADA.m4a",
    "https://archive.org/download/montagem-supersonic-slowed_202511/Montagem%20Supersonic%20%28Slowed%29.m4a",
    "https://archive.org/download/luna-bala-extreme-slowed/sma%24her%2C%20MXZI%20-%20ACELERADA%20%28Lyrics%29%20%28432Hz%29.mp3",
    "https://archive.org/download/luna-bala-extreme-slowed/NO%20BATID%C3%83O.mp3",
    "https://archive.org/download/luna-bala-extreme-slowed/ANDROMEDA%20-%20MONTAGEM%20COMA%20%28OFFICIAL%20MUSIC%20VIDEO%29.mp3",
    "https://archive.org/download/luna-bala-extreme-slowed/LUA%20NA%20PRA%C3%87A%20%28Ultra%20Slowed%29.mp3",
    "https://archive.org/download/montagem-rugada_202511/MONTAGEM%20RUGADA.m4a",
    "https://archive.org/download/montagem-direca-o-extended/MONTAGEM%20DIRE%C3%87%C3%83O%20%28Extended%29.m4a"
]