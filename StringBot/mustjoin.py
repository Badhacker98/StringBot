# Copyright (C) 2024 by Badhacker98@Github, < https://github.com/Badhacker98 >.
#
# This file is part of < https://github.com/Badhacker98/StringBot > project,
# and is released under the license agreement specified in:
# < https://github.com/Badhacker98/StringBot/blob/main/LICENSE >
#
# All rights reserved.

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from config import MUST_JOIN

@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(Client: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await Client.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await Client.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://files.catbox.moe/ok9a17.jpg",
                    caption=(f"**👋 ʜᴇʟʟᴏ {msg.from_user.mention},**\n\n**ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ [ᴄʜᴀɴɴᴇʟ]({link}) ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇs ɪɴ ᴛʜɪs ʙᴏᴛ.**"),
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("๏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ๏", url=link)]]))
        
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_Jᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")
