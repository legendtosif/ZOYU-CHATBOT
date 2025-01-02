from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from nexichat import OWNER, nexichat


START_BOT = [
    
    [
        InlineKeyboardButton(text="˹ ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅ | ᴍσʀє ɪηғσ ˼", callback_data="HELP"),
    ],
]


DEV_OP = [
    [
        InlineKeyboardButton(
            text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="˹ нєℓρ ˼", callback_data="HELP"),
    ],
    [
        # InlineKeyboardButton(text="˹ ʀєᴘσ ˼", callback_data="SOURCE"),
        InlineKeyboardButton(text="˹ αɓσµƭ ˼", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(text="˹ σρεɳ ᴄσϻϻᴧηᴅ | ᴍσʀє ɪηғσ ˼", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(
            text="⌯ ᴄʟσsє ⌯",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="⌯ ʙαck ⌯", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="˹ cнαƭʙοƭ ˼", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="˹ ᴛσσʟs ˼", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data="enable_chatbot"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data="disable_chatbot"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="sᴏᴏɴ", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="⌯ ʙαck ⌯", callback_data="SBACK"),
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="⌯ ʙαck ⌯", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(text="« ғᴇᴀᴛᴜʀᴇs »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="🎄 sᴜᴘᴘᴏʀᴛ 🎄", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="🍾 ᴏᴡɴᴇʀ 🍾", user_id=OWNER),
        #   InlineKeyboardButton(text="❄️ sᴏᴜʀᴄᴇ ❄️", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="🐳 ᴜᴘᴅᴀᴛᴇs 🐳", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK"),
    ],
]
