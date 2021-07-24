import os
import time
from  config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from __main__ import app

@app.on_message(filters.private & filters.command(["start"]))
async def mak (client, message):

   chat_id = message.chat.id
   userid =int( message.from_user["id"])
   text =message.text
   print(userid)
   if userid in OWNER_ID:

       await app.send_message(chat_id,
                              "اهلا بك عزيزي المالك \n\n يمنكنك انشاء منشورات منسقة وجميلة \n\n فقط ارسلي نص (عبارة - شعر - اقتباس ) ")
   else:
       await app.send_message(chat_id, "عذرا هذه النسخه مدفوعة$$ \n\n لشراء نسختك الخاصة راسل المطور @NNN2B")

@app.on_message(filters.text & filters.private & filters.user(OWNER_ID))
async def first(client,  message: Message):

    try:
        await message.reply_text(

            text="اختر نوع الخط                    ✅✅ㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=" ⚜️ خط الاميري ⚜️ ", callback_data="amiri"),
                        InlineKeyboardButton(text=" ⚜️ خط القرآن ⚜️ ", callback_data="qran"),

                    ],
                    [
                        InlineKeyboardButton(text=" ⚜️ خط الرقعة 2 ⚜️ ", callback_data="rqaa2"),
                        InlineKeyboardButton(text=" ⚜️ خط الرقعة ⚜️ ", callback_data="rqaa"),

                    ],
                    [
                        InlineKeyboardButton(text="⚜️ خط الطباعة ⚜️ ", callback_data="tbaa"),
                        InlineKeyboardButton(text=" ⚜️ خط هاكين ⚜️ ", callback_data="hsha"),

                    ],
                    [
                        InlineKeyboardButton(text=" ⚜️ خط القياسي 2 ⚜️ ", callback_data="qyass2"),
                        InlineKeyboardButton(text=" ⚜️ خط القياسي  ⚜️ ", callback_data="qyass"),

                    ],
                    [
                        InlineKeyboardButton(text=" ⚜️ خط الحر 2 ⚜️ ", callback_data="hur2"),
                        InlineKeyboardButton(text=" ⚜️ خط الحر  ⚜️ ", callback_data="hur"),

                    ],
                    [
                        InlineKeyboardButton(text=" ⚜️ خط اعلانات 2 ⚜️ ", callback_data="alanat2"),
                        InlineKeyboardButton(text=" ⚜️ خط اعلانات  ⚜️ ", callback_data="alanat"),

                    ],

                    [
                        InlineKeyboardButton(text="اغلاق ❌ ", callback_data="close_e"),
                    ],
                    ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("Something went wrong!", quote=True)
            except Exception:
                return
