
import os
from __main__ import app
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from pyrogram.errors import UserNotParticipant

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
    update_channel = "-1001152587608"
    text = message.text

    if update_channel:
        try:
            user = await client.get_chat_member(update_channel, user_id)

            if user.status in ["member", "creator", "administrator"]:
                if text != "/start" :
                    await first(client, message)
                elif text == "/start" :
                    await message.reply_text(
                        f"اهلا بك عزيزي {user_name} \n\n يمنكنك انشاء منشورات منسقة وجميلة \n\n فقط ارسلي نص (عبارة - شعر - اقتباس ) ")
#                 else:
#                     await message.reply_text(
#                         "🚸| عذرا عزيزي هذة النسخة مدفوعة $$  \n🔰| للحصول على نسختك الخاصة من البوت 🤖⚡️ \n\n🔰| راسل المطور 👨🏻‍💻 "
#                         , reply_markup=InlineKeyboardMarkup(
#                             [
#                                 [
#                                     InlineKeyboardButton(
#                                         text="  Developer ‍💻   ", url="https://t.me/shnider_bots"
#                                     )
#                                 ]
#                             ]
#                         )
#                         )
                    return
        except UserNotParticipant:
            link = "t.me/qad3im"
            # await update.reply_text(f"Join @{update_channel} To Use Me")
            await message.reply_text(
                text="**لطفا انضم في القناة حتى تستخدمني  😎 🤭**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="انضمام الان ✅ ", url=link)]
                ])
            )
            return
        except Exception:
            await message.reply_text("حدث خطا ما راسل الدعم  @shnider_bots ")
            return
