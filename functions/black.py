import os
import textwrap
import glob
from PIL import Image, ImageDraw, ImageFont

async def amere_B(client, message):
    global edit_img_loc, dir_font, width, height, draw
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]
        for photo in chunk:
            ms = await message.reply_to_message.reply_text("يتم التحميل ....")
            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 100
            lines = textwrap.wrap(text, width=40)
            for line in lines:
                dir_font = "./fonts/Amiri.ttf"
                size_font = 105
                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2
                print(yy)
                print(width, height)
                print(len(lines))
                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "qad3im.png"
                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), line, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            y_bot = (h / 1.8) + (height / 1.8 * len(lines))
            y_top = (y_text / 1.5 - height) / (len(lines))
            font = ImageFont.truetype(dir_font, 40)
            draw.multiline_text((((w - width) /2.4), y_text - 4), "qad3im", fill=(0, 0, 0), font=font,
                                align="right")
            await ms.edit("يتم التحميل ...")
            im.save(edit_img_loc, quality=100)
            xl = 0
            xr = w - 40
            box = (xl, y_top, xr, y_bot)  # left, top, right, bottom
            cropped_image = im.crop(box)
            cropped_image.save(edit_img_loc, quality=100)
            await message.reply_chat_action("upload_photo")
            await ms.delete()
            await message.reply_to_message.reply_photo(edit_img_loc, caption="_")

async def rqaa_B(client, message):
    global edit_img_loc, dir_font, width, height, draw
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]
        for photo in chunk:
            ms = await message.reply_to_message.reply_text("يتم التحميل ....")
            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 100
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/rqaa.ttf"
                size_font = 100
                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2
                print(yy)
                print(width, height)
                print(len(lines))
                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "qad3im.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), line, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            y_bot = (h / 2) + (height / 1.8 * len(lines))
            y_top = (y_text / 1.2 - height) / (len(lines))
            font = ImageFont.truetype(dir_font, 45)
            draw.multiline_text((((w - width) / 2), y_text - (height / 1.8)), "qad3im", fill=(0, 0, 0), font=font,
                                align="right")
            im.save(edit_img_loc, quality=100)
            xl = 0
            xr = w - 80
            box = (xl, y_top, xr, y_bot)  # left, top, right, bottom
            cropped_image = im.crop(box)
            cropped_image.save(edit_img_loc, quality=100)
            await ms.edit("يتم التحميل ...")
            await message.reply_chat_action("upload_photo")
            await ms.delete()
            await message.reply_to_message.reply_photo(edit_img_loc, caption="_")

async def rqaa2_B(client, message):
    global edit_img_loc, dir_font, width, height, draw
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]
        for photo in chunk:
            ms = await message.reply_to_message.reply_text("يتم التحميل ....")
            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 100
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/RQAA2.ttf"
                size_font = 100
                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2
                print(yy)
                print(width, height)
                print(len(lines))
                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "qad3im.png"
                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), line, fill=(0, 0, 0), font=font, align="center")
                im.save(edit_img_loc, quality=100)
                y_text += height
            y_bot = (h / 2) + (height / 1.8 * len(lines))
            y_top = (y_text / 1.2 - height) / (len(lines))
            font = ImageFont.truetype(dir_font, 45)
            draw.multiline_text((((w - width) / 2), y_text - (height / 1.8)), "qad3im", fill=(0, 0, 0), font=font,
                                align="right")
            im.save(edit_img_loc, quality=100)
            xl = 0
            xr = w - 80
            box = (xl, y_top, xr, y_bot)  # left, top, right, bottom
            cropped_image = im.crop(box)
            cropped_image.save(edit_img_loc, quality=100)
            await ms.edit("يتم التحميل ...")
            await message.reply_chat_action("upload_photo")
            await ms.delete()
            await message.reply_to_message.reply_photo(edit_img_loc, caption="_")


async def qran_B(client, message):
    global edit_img_loc, dir_font, width, height
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await message.reply_to_message.reply_text("يتم التحميل ....")
            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 100
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/qraan.ttf"
                size_font = 100
                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2
                print(yy)
                print(width, height)
                print(len(lines))
                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "qad3im.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), line, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            y_bot = (h / 2) + (height / 1.8 * len(lines))
            y_top = (y_text / 1.2 - height) / (len(lines))
            font = ImageFont.truetype(dir_font, 45)
            draw.multiline_text((((w - width) / 2), y_text - (height / 1.8)), "qad3im", fill=(0, 0, 0), font=font,
                                align="right")
            im.save(edit_img_loc, quality=100)
            xl = 0
            xr = w - 80
            box = (xl, y_top, xr, y_bot)  # left, top, right, bottom
            cropped_image = im.crop(box)
            cropped_image.save(edit_img_loc, quality=100)
            await ms.edit("يتم التحميل ...")
            await message.reply_chat_action("upload_photo")
            await ms.delete()
            await message.reply_to_message.reply_photo(edit_img_loc, caption="_")


async def tbaa_B(client, message):
    global edit_img_loc, dir_font, width, height, draw
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]
        for photo in chunk:
            ms = await message.reply_to_message.reply_text("يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 100
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/tbaa.ttf"
                size_font = 100

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                print(yy)
                print(width, height)
                print(len(lines))

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "qad3im.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), line, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            y_bot = (h / 2) + (height / 1.8 * len(lines))
            y_top = (y_text / 1.2 - height) / (len(lines))
            font = ImageFont.truetype(dir_font, 45)
            draw.multiline_text((((w - width) / 2), y_text - (height / 1.8)), "qad3im", fill=(0, 0, 0), font=font,
                                align="right")
            im.save(edit_img_loc, quality=100)
            xl = 0
            xr = w - 80
            box = (xl, y_top, xr, y_bot)  # left, top, right, bottom
            cropped_image = im.crop(box)
            cropped_image.save(edit_img_loc, quality=100)
            await ms.edit("يتم التحميل ...")
            await message.reply_chat_action("upload_photo")
            await ms.delete()
            await message.reply_to_message.reply_photo(edit_img_loc, caption="_")


async def hsha_B(client, message):
    global edit_img_loc, dir_font, width, height, draw
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await message.reply_to_message.reply_text("يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 80

            lines = textwrap.wrap(text, width=25)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/hsha.ttf"
                size_font = 130
                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                print(yy)
                print(width, height)
                print(len(lines))

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")

                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "qad3im.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), line, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            y_bot = (h / 2) + (height / 1.8 * len(lines))
            y_top = (y_text / 1.2 - height) / (len(lines))
            font = ImageFont.truetype(dir_font, 45)
            draw.multiline_text((((w - width) / 2), y_text - (height / 1.8)), "qad3im", fill=(0, 0, 0), font=font,
                                align="right")
            im.save(edit_img_loc, quality=100)
            xl = 0
            xr = w - 80
            box = (xl, y_top, xr, y_bot)  # left, top, right, bottom
            cropped_image = im.crop(box)
            cropped_image.save(edit_img_loc, quality=100)
            await ms.edit("يتم التحميل ...")
            await message.reply_chat_action("upload_photo")
            await ms.delete()
            await message.reply_to_message.reply_photo(edit_img_loc, caption="_")


async def qyass_B(client, message):
    global edit_img_loc, dir_font, width, height, draw
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await message.reply_to_message.reply_text("يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 100
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/qyasee.ttf"
                size_font = 140
                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                print(yy)
                print(width, height)
                print(len(lines))

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "qad3im.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), line, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            y_bot = (h / 2) + (height / 1.8 * len(lines))
            y_top = (y_text / 1.2 - height) / (len(lines))
            font = ImageFont.truetype(dir_font, 45)
            draw.multiline_text((((w - width) / 2), y_text - (height / 1.8)), "qad3im", fill=(0, 0, 0), font=font,
                                align="right")
            im.save(edit_img_loc, quality=100)
            xl = 0
            xr = w - 80
            box = (xl, y_top, xr, y_bot)  # left, top, right, bottom
            cropped_image = im.crop(box)
            cropped_image.save(edit_img_loc, quality=100)
            await ms.edit("يتم التحميل ...")
            await message.reply_chat_action("upload_photo")
            await ms.delete()
            await message.reply_to_message.reply_photo(edit_img_loc, caption="_")


async def qyass2_B(client, message):
    global edit_img_loc, dir_font, width, height, draw
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await message.reply_to_message.reply_text("يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 40
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/qyasee2.ttf"
                size_font = 120

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                print(yy)
                print(width, height)
                print(len(lines))

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "qad3im.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), line, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            y_bot = (h / 2) + (height / 1.8 * len(lines))
            y_top = (y_text / 1.2 - height) / (len(lines))
            font = ImageFont.truetype(dir_font, 45)
            draw.multiline_text((((w - width) / 2), y_text - (height / 1.8)), "qad3im", fill=(0, 0, 0), font=font,
                                align="right")
            im.save(edit_img_loc, quality=100)
            xl = 0
            xr = w - 80
            box = (xl, y_top, xr, y_bot)  # left, top, right, bottom
            cropped_image = im.crop(box)
            cropped_image.save(edit_img_loc, quality=100)
            await ms.edit("يتم التحميل ...")
            await message.reply_chat_action("upload_photo")
            await ms.delete()
            await message.reply_to_message.reply_photo(edit_img_loc, caption="_")


async def hur_B(client, message):
    global edit_img_loc, dir_font, width, height, draw
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await message.reply_to_message.reply_text("يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 100
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/hur.ttf"
                size_font = 100

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                print(yy)
                print(width, height)
                print(len(lines))

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "qad3im.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), line, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            y_bot = (h / 2) + (height / 1.8 * len(lines))
            y_top = (y_text / 1.2 - height) / (len(lines))
            font = ImageFont.truetype(dir_font, 45)
            draw.multiline_text((((w - width) / 2), y_text - (height / 1.8)), "qad3im", fill=(0, 0, 0), font=font,
                                align="right")
            im.save(edit_img_loc, quality=100)
            xl = 0
            xr = w - 80
            box = (xl, y_top, xr, y_bot)  # left, top, right, bottom
            cropped_image = im.crop(box)
            cropped_image.save(edit_img_loc, quality=100)
            await ms.edit("يتم التحميل ...")
            await message.reply_chat_action("upload_photo")
            await ms.delete()
            await message.reply_to_message.reply_photo(edit_img_loc, caption="_")


async def hur2_B(client, message):
    global edit_img_loc, dir_font, width, height, draw
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await message.reply_to_message.reply_text("يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 90
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/hur2.ttf"
                size_font = 100

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                print(yy)
                print(width, height)
                print(len(lines))

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "qad3im.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), line, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            y_bot = (h / 2) + (height / 1.8 * len(lines))
            y_top = (y_text / 1.2 - height) / (len(lines))
            font = ImageFont.truetype(dir_font, 45)
            draw.multiline_text((((w - width) / 2), y_text - (height / 1.8)), "qad3im", fill=(0, 0, 0), font=font,
                                align="right")
            im.save(edit_img_loc, quality=100)
            xl = 0
            xr = w - 80
            box = (xl, y_top, xr, y_bot)  # left, top, right, bottom
            cropped_image = im.crop(box)
            cropped_image.save(edit_img_loc, quality=100)
            await ms.edit("يتم التحميل ...")
            await message.reply_chat_action("upload_photo")
            await ms.delete()
            await message.reply_to_message.reply_photo(edit_img_loc, caption="_")

async def alanat_B(client, message):
    global edit_img_loc, dir_font, width, height, draw
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await message.reply_to_message.reply_text("يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 100
            x_text = w
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/alanat.ttf"
                size_font = 100

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                print(yy)
                print(width, height)
                print(len(lines))

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "qad3im.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), line, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            y_bot = (h / 2) + (height / 1.8 * len(lines))
            y_top = (y_text / 1.2 - height) / (len(lines))
            font = ImageFont.truetype(dir_font, 45)
            draw.multiline_text((((w - width) / 2), y_text - (height / 1.8)), "qad3im", fill=(0, 0, 0), font=font,
                                align="right")
            im.save(edit_img_loc, quality=100)
            xl = 0
            xr = w - 80
            box = (xl, y_top, xr, y_bot)  # left, top, right, bottom
            cropped_image = im.crop(box)
            cropped_image.save(edit_img_loc, quality=100)
            await ms.edit("يتم التحميل ...")
            await message.reply_chat_action("upload_photo")
            await ms.delete()
            await message.reply_to_message.reply_photo(edit_img_loc, caption="_")


async def alanat2_B(client, message):
    global edit_img_loc, dir_font, width, height, draw
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await message.reply_to_message.reply_text("يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 80

            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/alanat2.ttf"
                size_font = 100

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                print(yy)
                print(width, height)
                print(len(lines))

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")

                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "qad3im.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), line, fill=(0, 0, 0), font=font, align="center")
                im.save(edit_img_loc, quality=100)
                y_text += height
            y_bot = (h / 2) + (height / 1.8 * len(lines))
            y_top = (y_text / 1.2 - height) / (len(lines))
            font = ImageFont.truetype(dir_font, 45)
            draw.multiline_text((((w - width) / 2), y_text - (height / 1.8)), "qad3im", fill=(0, 0, 0), font=font,
                                align="right")
            im.save(edit_img_loc, quality=100)
            xl = 0
            xr = w - 80
            box = (xl, y_top, xr, y_bot)  # left, top, right, bottom
            cropped_image = im.crop(box)
            cropped_image.save(edit_img_loc, quality=100)
            await ms.edit("يتم التحميل ...")
            await message.reply_chat_action("upload_photo")
            await ms.delete()
            await message.reply_to_message.reply_photo(edit_img_loc, caption="_")
