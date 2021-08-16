from functions.Processing import edit1
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton,Message

async def MOR(client, codx, message:Message):
    text = message.reply_to_message.text
    await message.reply_text(

        f" ⚜️⚜️ النص الطلوب للتصميم ⚜️⚜️ :- {text}",
        reply_markup=InlineKeyboardMarkup(
            [

                [
                    InlineKeyboardButton(text=" ⚜️ عرض المزيد ⚜️ ", callback_data=f"{codx}"),
                    InlineKeyboardButton(text=" ⚜️ رجوع ⚜️ ", callback_data="cbb.first"),

                ],

                [
                    InlineKeyboardButton(text="اغلاق ❌ ", callback_data="close_e")
                ],
            ]
        ), reply_to_message_id=message.reply_to_message.message_id

    )


async def amiri_B(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/Amiri.ttf"
    color_t = (0, 0, 0)
    size_font = 90
    codx = "amiri_BX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def amiri_W(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/Amiri.ttf"
    color_t = (250, 250, 250)
    size_font = 90
    codx = "amiri_WX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def rqaa_B(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/rqaa.ttf"
    color_t = (0, 0, 0)
    size_font = 90
    codx = "rqaa_BX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def rqaa_W(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/rqaa.ttf"
    color_t = (250, 250, 250)
    size_font = 90
    codx = "rqaa_WX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def rqaa2_B(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/rqaa2.ttf"
    color_t = (0, 0, 0)
    size_font = 95
    codx = "rqaa2_BX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def rqaa2_W(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/rqaa2.ttf"
    color_t = (250, 250, 250)
    size_font = 95
    codx = "rqaa2_WX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def qran_B(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/qraan.ttf"
    color_t = (0, 0, 0)
    size_font = 90
    codx = "qran_BX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def qran_W(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/qraan.ttf"
    color_t = (250, 250, 250)
    size_font = 90
    codx = "qran_WX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def tbaa_B(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/tbaa.ttf"
    color_t = (0, 0, 0)
    size_font = 80
    codx = "tbaa_BX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def tbaa_W(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/tbaa.ttf"
    color_t = (250, 250, 250)
    size_font = 80
    codx = "tbaa_WX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def hsha_B(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/hsha.ttf"
    color_t = (0, 0, 0)
    size_font = 70
    codx = "hsha_BX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def hsha_W(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/hsha.ttf"
    color_t = (250, 250, 250)
    size_font = 70
    codx = "hsha_WX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def qyass_B(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/qyasee.ttf"
    color_t = (0, 0, 0)
    size_font = 90
    codx = "qyass_BX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def qyass_W(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/qyasee.ttf"
    color_t = (250, 250, 250)
    size_font = 90
    codx = "qyass_WX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def qyass2_B(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/qyasee2.ttf"
    color_t = (0, 0, 0)
    size_font = 100
    codx = "qyass2_BX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def qyass2_W(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/qyasee2.ttf"
    color_t = (250, 250, 250)
    size_font = 100
    codx = "qyass2_WX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def hur_B(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/hur.ttf"
    color_t = (0, 0, 0)
    size_font = 100
    codx = " hur_BX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def hur_W(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/hur.ttf"
    color_t = (250, 250, 250)
    size_font = 100
    codx = "hur_WX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def hur2_B(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/hur2.ttf"
    color_t = (0, 0, 0)
    size_font = 100
    codx = "hur2_BX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def hur2_W(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/hur2.ttf"
    color_t = (250, 250, 250)
    size_font = 100
    codx = "hur2_WX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def alanat_B(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/alanat.ttf"
    color_t = (250, 250, 250)
    size_font = 70
    codx = "alanat_BX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def alanat_W(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/alanat.ttf"
    color_t = (250, 250, 250)
    size_font = 70
    codx = "alanat_WX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def alanat2_B(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/alanat2.ttf"
    color_t = (250, 250, 250)
    size_font = 70
    codx = "alanat2_BX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)


async def alanat2_W(client, message):
    dir_bg = "./bg"
    dir_font = "./fonts/alanat2.ttf"
    color_t = (250, 250, 250)
    size_font = 70
    codx = "alanat2_WX"
    await edit1(client, dir_bg, dir_font, color_t, size_font, message)
    await MOR(client, codx, message)
