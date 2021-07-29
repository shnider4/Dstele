import os
import time

from __main__ import app

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, UserBannedInChannel

# CH force Sbs
update_channel = "-1001152587608"


async def chack(client, message):
    user_id = message.from_user["id"]
    user_name = message.from_user["first_name"]

    if update_channel:
        try:
            user = await client.get_chat_member(update_channel, user_id)

            if user.status in ["member", "creator", "administrator"]:
                await message.reply_text(
                    f"اهلا بك عزيزي {user_name} \n\n يمنكنك انشاء منشورات منسقة وجميلة \n\n فقط ارسلي نص (عبارة - شعر - اقتباس ) ")
                return
        except UserNotParticipant:
            link = link = "t.me/qad3im"
            # await update.reply_text(f"Join @{update_channel} To Use Me")
            await message.reply_text(
                text="**لطفا انضم في القناة حتى تستخدمني  😎 🤭**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="انضمام الان ✅ ", url=link)]
                ])
            )
            return
        except Exception:
            await message.reply_text("حدث خطا ما راسل الدعم  @qad3im ")
            return


@app.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    try:
        await chack(client, message)
    except Exception:
        pass


async def first(client, message):
    try:
        await message.reply_text(

            text=" ⚜️⚜️ اختر نوع الخط ⚜️⚜️  ",
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


@app.on_message(filters.text & filters.private)
async def chack(client, message):
    user_id = message.from_user["id"]
    user_name = message.from_user["first_name"]

    if update_channel:
        try:
            user = await client.get_chat_member(update_channel, user_id)

            if user.status in ["member", "creator", "administrator"]:
                await first(client, message)
                return
        except UserNotParticipant:
            link = link = "t.me/qad3im"
            # await update.reply_text(f"Join @{update_channel} To Use Me")
            await message.reply_text(
                text="**لطفا انضم في القناة حتى تستخدمني  😎 🤭**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="انضمام الان ✅ ", url=link)]
                ])
            )
            return
        except Exception:
            await message.reply_text("حدث خطا ما راسل الدعم  @qad3im ")
            return
