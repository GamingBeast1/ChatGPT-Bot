from pyrogram import Client, filters
from config import LOG_CHANNEL
from plugins.database import db
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)


LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""

@Client.on_message(filters.command('start'))
async def start_message(c,m):
    await db.is_user_exist(m.from_user.id)
    await db.add_user(m.from_user.id, m.from_user.first_name)
    await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    await m.reply_photo(f"https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg"),
        caption="**ʜɪ** 👋\n\n**ɪ ᴀᴍ ᴀ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ**\n\n⭕ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :-** **[Tᴇᴄʜ VJ](https://t.me/vj_botz)**",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('💝 sᴜʙsᴄʀɪʙᴇ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ', url='https://youtube.com/@Tech_VJ')
                    ],  
                    [
                        InlineKeyboardButton("❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url='https://t.me/Kingvj01'),
                        InlineKeyboardButton("🤖 ᴜᴘᴅᴀᴛᴇ", callback_data='about')
                    ]
                ]
            )
        
ABOUT_TXT = """Hello"""
  
elif query.data == "about":
        buttons = [[
            InlineKeyboardButton('📄Sᴏᴜʀᴄᴇ', callback_data='source'),
            InlineKeyboardButton('👨🏻‍💻Oᴡɴᴇʀ', callback_data='owner')
        ],[
            InlineKeyboardButton('Hᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('🔒 Cʟᴏsᴇ', callback_data='close_data')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto("https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="■ ▣ ▣"
        )
        await query.message.edit_text(
            text="■ ■ ▣"
        )
        await query.message.edit_text(
            text="■ ■ ■"
        )
        me2 = (await client.get_me()).mention
        await query.message.edit_text(
            text=ABOUT_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )