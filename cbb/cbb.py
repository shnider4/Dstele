from functions.black import(
amere_B,
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
qyass_B


)
from functions.white import(
amere_W,
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
                            text="لون الخط أسود ◼️ ", callback_data="amere_B"
                        ),
                        InlineKeyboardButton(
                            text="لون الاخط أبيض ◻️ ", callback_data="amere_W"
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
        await query.message.delete()
        if query.data == "amere_B":
            await amere_B(client, query.message)
        elif query.data == "amere_W":
            await amere_W(client, query.message)

        elif query.data == "rqaa_B":
            await rqaa_B (client, query.message)
        elif query.data == "rqaa_W":
            await rqaa_W (client, query.message)

        elif query.data == "rqaa2_B":
            await rqaa2_B (client, query.message)
        elif query.data == "rqaa2_W":
            await rqaa2_W (client, query.message)

        elif query.data == "qran_B":
            await qran_B (client, query.message)
        elif query.data == "qran_W":
            await qran_W (client, query.message)

        elif query.data == "tbaa_B":
            await tbaa_B (client, query.message)
        elif query.data == "tbaa_W":
            await tbaa_W (client, query.message)

        elif query.data == "hsha_B":
            await hsha_B (client, query.message)
        elif query.data == "hsha_W":
            await hsha_W (client, query.message)

        elif query.data == "qyass_B":
            await qyass_B (client, query.message)
        elif query.data == "qyass_W":
            await qyass_W (client, query.message)

        elif query.data == "qyass2_B":
            await qyass2_B (client, query.message)
        elif query.data == "qyass2_W":
            await qyass2_W (client, query.message)

        elif query.data == "hur_B":
            await hur_B (client, query.message)
        elif query.data == "hur_W":
            await hur_W (client, query.message)

        elif query.data == "hur2_B":
            await hur2_B (client, query.message)
        elif query.data == "hur2_W":
            await hur2_W (client, query.message)

        elif query.data == "alanat_B":
            await alanat_B (client, query.message)
        elif query.data == "alanat_W":
            await alanat_W (client, query.message)

        elif query.data == "alanat2_B":
            await alanat2_B (client, query.message)
        elif query.data == "alanat2_W":
            await alanat2_W (client, query.message)










