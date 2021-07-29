from functions.edit import (
    amiri_B,
    rqaa_B,
    rqaa2_B,
    qran_B,
    tbaa_B,
    alanat2_B,
    alanat_B,
    hsha_B,
    hur2_B,
    hur_B,
    qyass2_B,
    qyass_B,
    amiri_W,
    rqaa_W,
    rqaa2_W,
    qran_W,
    tbaa_W,
    alanat2_W,
    alanat_W,
    hsha_W,
    hur2_W,
    hur_W,
    qyass2_W,
    qyass_W
)
from functions.edit1 import (
    amiri_BX,
    rqaa_BX,
    rqaa2_BX,
    qran_BX,
    tbaa_BX,
    alanat2_BX,
    alanat_BX,
    hsha_BX,
    hur2_BX,
    hur_BX,
    qyass2_BX,
    qyass_BX,
    amiri_WX,
    rqaa_WX,
    rqaa2_WX,
    qran_WX,
    tbaa_WX,
    alanat2_WX,
    alanat_WX,
    hsha_WX,
    hur2_WX,
    hur_WX,
    qyass2_WX,
    qyass_WX,

)
from functions.edit2 import (
    amiri_BXX,
    rqaa_BXX,
    rqaa2_BXX,
    qran_BXX,
    tbaa_BXX,
    alanat2_BXX,
    alanat_BXX,
    hsha_BXX,
    hur2_BXX,
    hur_BXX,
    qyass2_BXX,
    qyass_BXX,
    amiri_WXX,
    rqaa_WXX,
    rqaa2_WXX,
    qran_WXX,
    tbaa_WXX,
    alanat2_WXX,
    alanat_WXX,
    hsha_WXX,
    hur2_WXX,
    hur_WXX,
    qyass2_WXX,
    qyass_WXX
)

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "amiri":
        await query.message.edit_text(
            "**اختر لون الخط 🌈 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="لون الخط أسود ◼️ ", callback_data="amiri_B"
                        ),
                        InlineKeyboardButton(
                            text="لون الاخط أبيض ◻️ ", callback_data="amiri_W"
                        ),
                    ],

                    [InlineKeyboardButton(text="رجوع 🔙", callback_data="cbb.first")],
                ]
            ),
        )
    elif query.data == "alanat2":
        await query.message.edit(
            "**اختر لون الخط 🌈 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="لون الخط أسود ◼️ ", callback_data="alanat2_B"),
                        InlineKeyboardButton(
                            text="لون الاخط أبيض ◻️ ", callback_data="alanat2_W"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="رجوع 🔙", callback_data="cbb.first"
                        )
                    ],
                ]
            ),
        )
    elif query.data == "alanat":
        await query.message.edit(
            "**اختر لون الخط 🌈 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="لون الخط أسود ◼️ ", callback_data="alanat_B"),
                        InlineKeyboardButton(
                            text="لون الاخط أبيض ◻️ ", callback_data="alanat_W"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="رجوع 🔙", callback_data="cbb.first"
                        )
                    ],
                ]
            ),
        )
    elif query.data == "hur":
        await query.message.edit(
            "**اختر لون الخط 🌈 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="لون الخط أسود ◼️ ", callback_data="hur_B"),
                        InlineKeyboardButton(
                            text="لون الاخط أبيض ◻️ ", callback_data="hur_W"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="رجوع 🔙", callback_data="cbb.first"
                        )
                    ],
                ]
            ),
        )
    elif query.data == "hur2":
        await query.message.edit(
            "**اختر لون الخط 🌈 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="لون الخط أسود ◼️ ", callback_data="hur2_B"),
                        InlineKeyboardButton(
                            text="لون الاخط أبيض ◻️ ", callback_data="hur2_W"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="رجوع 🔙", callback_data="cbb.first"
                        )
                    ],
                ]
            ),
        )
    elif query.data == "qyass":
        await query.message.edit(
            "**اختر لون الخط 🌈 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="لون الخط أسود ◼️ ", callback_data="qyass_B"),
                        InlineKeyboardButton(
                            text="لون الاخط أبيض ◻️ ", callback_data="qyass_W"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="رجوع 🔙", callback_data="cbb.first"
                        )
                    ],
                ]
            ),
        )
    elif query.data == "qyass2":
        await query.message.edit(
            "**اختر لون الخط 🌈 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="لون الخط أسود ◼️ ", callback_data="qyass2_B"),
                        InlineKeyboardButton(
                            text="لون الاخط أبيض ◻️ ", callback_data="qyass2_W"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="رجوع 🔙", callback_data="cbb.first"
                        )
                    ],
                ]
            ),
        )
    elif query.data == "hsha":
        await query.message.edit(
            "**اختر لون الخط 🌈 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="لون الخط أسود ◼️ ", callback_data="hsha_B"),
                        InlineKeyboardButton(
                            text="لون الاخط أبيض ◻️ ", callback_data="hsha_W"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="رجوع 🔙", callback_data="cbb.first"
                        )
                    ],
                ]
            ),
        )
    elif query.data == "tbaa":
        await query.message.edit(
            "**اختر لون الخط 🌈 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="لون الخط أسود ◼️ ", callback_data="tbaa_B"),
                        InlineKeyboardButton(
                            text="لون الاخط أبيض ◻️ ", callback_data="tbaa_W"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="رجوع 🔙", callback_data="cbb.first"
                        )
                    ],
                ]
            ),
        )
    elif query.data == "rqaa":
        await query.message.edit(
            "**اختر لون الخط 🌈 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="لون الخط أسود ◼️ ", callback_data="rqaa_B"),
                        InlineKeyboardButton(
                            text="لون الاخط أبيض ◻️ ", callback_data="rqaa_W"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="رجوع 🔙", callback_data="cbb.first"
                        )
                    ],
                ]
            ),
        )
    elif query.data == "rqaa2":
        await query.message.edit(
            "**اختر لون الخط 🌈 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="لون الخط أسود ◼️ ", callback_data="rqaa2_B"),
                        InlineKeyboardButton(
                            text="لون الاخط أبيض ◻️ ", callback_data="rqaa2_W"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="رجوع 🔙", callback_data="cbb.first"
                        )
                    ],
                ]
            ),
        )
    elif query.data == "qran":
        await query.message.edit(
            "**اختر لون الخط 🌈 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="لون الخط أسود ◼️ ", callback_data="qran_B"),
                        InlineKeyboardButton(
                            text="لون الاخط أبيض ◻️ ", callback_data="qran_W"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="رجوع 🔙", callback_data="cbb.first"
                        )
                    ],
                ]
            ),
        )

    elif query.data == "cbb.first":
        await query.message.edit_text(

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
            )
        )

    if query.data not in [
        "rqaa",
        "amiri",
        "cbb.first",
        "qran",
        "tbaa",
        "hsha",
        "rqaa2",
        "qyass2",
        "qyass",
        "hur2",
        "hur",
        "alanat",
        "alanat2",

    ]:
        await query.message.edit("⚜️⚜️النص المطلوب للتصميم ⚜️⚜️")
        if query.data == "amiri_B":
            await amiri_B(client, query.message)
        elif query.data == "amiri_W":
            await amiri_W(client, query.message)

        elif query.data == "amiri_WX":
            await amiri_WX(client, query.message)
        elif query.data == "amiri_BX":
            await amiri_BX(client, query.message)

        elif query.data == "amiri_BXX":
            await amiri_BXX(client, query.message)
        elif query.data == "amiri_WXX":
            await amiri_WXX(client, query.message)

        elif query.data == "rqaa_B":
            await rqaa_B(client, query.message)
        elif query.data == "rqaa_W":
            await rqaa_W(client, query.message)

        elif query.data == "rqaa_BX":
            await rqaa_BX(client, query.message)
        elif query.data == "rqaa_WX":
            await rqaa_WX(client, query.message)

        elif query.data == "rqaa_BXX":
            await rqaa_BXX(client, query.message)
        elif query.data == "rqaa_WXX":
            await rqaa_WXX(client, query.message)

        elif query.data == "rqaa2_B":
            await rqaa2_B(client, query.message)
        elif query.data == "rqaa2_W":
            await rqaa2_W(client, query.message)

        elif query.data == "rqaa2_BX":
            await rqaa2_BX(client, query.message)
        elif query.data == "rqaa2_WX":
            await rqaa2_WX(client, query.message)

        elif query.data == "rqaa2_BXX":
            await rqaa2_BXX(client, query.message)
        elif query.data == "rqaa2_WXX":
            await rqaa2_WXX(client, query.message)

        elif query.data == "qran_B":
            await qran_B(client, query.message)
        elif query.data == "qran_W":
            await qran_W(client, query.message)

        elif query.data == "qran_BX":
            await qran_BX(client, query.message)
        elif query.data == "qran_WX":
            await qran_WX(client, query.message)

        elif query.data == "qran_BXX":
            await qran_BXX(client, query.message)
        elif query.data == "qran_WXX":
            await qran_WXX(client, query.message)

        elif query.data == "tbaa_B":
            await tbaa_B(client, query.message)
        elif query.data == "tbaa_W":
            await tbaa_W(client, query.message)

        elif query.data == "tbaa_BX":
            await tbaa_BX(client, query.message)
        elif query.data == "tbaa_WX":
            await tbaa_WX(client, query.message)

        elif query.data == "tbaa_BXX":
            await tbaa_BXX(client, query.message)
        elif query.data == "tbaa_WXX":
            await tbaa_WXX(client, query.message)

        elif query.data == "hsha_B":
            await hsha_B(client, query.message)
        elif query.data == "hsha_W":
            await hsha_W(client, query.message)

        elif query.data == "hsha_BX":
            await hsha_BX(client, query.message)
        elif query.data == "hsha_WX":
            await hsha_WX(client, query.message)

        elif query.data == "hsha_BXX":
            await hsha_BXX(client, query.message)
        elif query.data == "hsha_WXX":
            await hsha_WXX(client, query.message)

        elif query.data == "qyass_B":
            await qyass_B(client, query.message)
        elif query.data == "qyass_W":
            await qyass_W(client, query.message)

        elif query.data == "qyass_BX":
            await qyass_BX(client, query.message)
        elif query.data == "qyass_WX":
            await qyass_WX(client, query.message)

        elif query.data == "qyass_BXX":
            await qyass_BXX(client, query.message)
        elif query.data == "qyass_WXX":
            await qyass_WXX(client, query.message)

        elif query.data == "qyass2_B":
            await qyass2_B(client, query.message)
        elif query.data == "qyass2_W":
            await qyass2_W(client, query.message)

        elif query.data == "qyass2_BX":
            await qyass2_BX(client, query.message)
        elif query.data == "qyass2_WX":
            await qyass2_WX(client, query.message)

        elif query.data == "qyass2_BXX":
            await qyass2_BXX(client, query.message)
        elif query.data == "qyass2_WXX":
            await qyass2_WXX(client, query.message)

        elif query.data == "hur_B":
            await hur_B(client, query.message)
        elif query.data == "hur_W":
            await hur_W(client, query.message)

        elif query.data == "hur_BX":
            await hur_BX(client, query.message)
        elif query.data == "hur_WX":
            await hur_WX(client, query.message)
        elif query.data == "hur_BXX":
            await hur_BXX(client, query.message)
        elif query.data == "hur_WXX":
            await hur_WXX(client, query.message)

        elif query.data == "hur2_B":
            await hur2_B(client, query.message)
        elif query.data == "hur2_W":
            await hur2_W(client, query.message)
        elif query.data == "hur2_BX":
            await hur2_BX(client, query.message)
        elif query.data == "hur2_WX":
            await hur2_WX(client, query.message)
        elif query.data == "hur2_BXX":
            await hur2_BXX(client, query.message)
        elif query.data == "hur2_WXX":
            await hur2_WXX(client, query.message)

        elif query.data == "alanat_B":
            await alanat_B(client, query.message)
        elif query.data == "alanat_W":
            await alanat_W(client, query.message)

        elif query.data == "alanat_BX":
            await alanat_BX(client, query.message)
        elif query.data == "alanat_WX":
            await alanat_WX(client, query.message)

        elif query.data == "alanat_BXX":
            await alanat_BXX(client, query.message)
        elif query.data == "alanat_WXX":
            await alanat_WXX(client, query.message)

        elif query.data == "alanat2_B":
            await alanat2_B(client, query.message)
        elif query.data == "alanat2_W":
            await alanat2_W(client, query.message)

        elif query.data == "alanat2_BX":
            await alanat2_BX(client, query.message)
        elif query.data == "alanat2_WX":
            await alanat2_WX(client, query.message)

        elif query.data == "alanat2_BXX":
            await alanat2_BXX(client, query.message)
        elif query.data == "alanat2_WXX":
            await alanat2_WXX(client, query.message)
