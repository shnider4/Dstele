# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
import bidi.algorithm
from PIL import Image, ImageFilter
import textwrap
import glob
from main  import app






async def amere_B (client, message):

   chat_id = message.chat.id
   userid =str( message.from_user["id"])
   text =message.reply_to_message.text
   dir_bg = "./bg"
   bg = glob.glob(f"{dir_bg}/*.png")
   for i in range(0, len(bg), 11):
      chunk = bg[i:i + 11]

      for photo in chunk:
         ms = await app.send_message(chat_id, "يتم التحميل ....")

         im = Image.open(photo)
         print(im)
         w, h = im.size
         y_text = 180
         x_text = w
         lines = textwrap.wrap(text, width=30)
         await ms.edit("يتم التحميل .....")
         for line in lines:
             dir_font = "./fonts/Amiri.ttf"
             size_font =100
             if len(lines) == 1:
                 size_font = size_font +50
                 y_text = y_text + 80
             else:
                 size_font = 105

             font = ImageFont.truetype(dir_font, size_font)
             width, height = font.getsize(line)
             yy = (w - width) / 2

             yy = yy + 190
             print(yy)
             print(width, height)
             print(len(lines))
             stext = arabic_reshaper.reshape(line)
             text1 = bidi.algorithm.get_display(stext, encoding="utf-8")

             if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                 os.makedirs(f"./DOWNLOADS/{userid}")
             download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
             edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.png"

             draw = ImageDraw.Draw(im)
             draw.multiline_text((yy, y_text), text1, fill=(0, 0, 0), font=font, align="right")
             im.save(edit_img_loc, quality=100)
             y_text += height
         await ms.edit("يتم التحميل ...")
         await ms.delete()
         await app.send_chat_action(chat_id=chat_id,action="upload_photo")
         await app.send_photo(chat_id, photo=edit_img_loc, caption="_")



async def rqaa_B (client, message):
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await app.send_message(chat_id, "يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 180
            x_text = w
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/rqaa.ttf"
                size_font = 100
                if len(lines) == 1:
                    size_font = size_font + 70
                    y_text = y_text +120
                else:
                    size_font = 130

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                yy = yy + 140
                print(yy)
                print(width, height)
                print(len(lines))
                stext = arabic_reshaper.reshape(line)
                text1 = bidi.algorithm.get_display(stext, encoding="utf-8")

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), text1, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += (height * 1.2)
            await ms.edit("يتم التحميل ...")
            await ms.delete()
            await app.send_chat_action(chat_id=chat_id, action="upload_photo")
            await app.send_photo(chat_id, photo=edit_img_loc, caption="_")


async def rqaa2_B (client, message):
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await app.send_message(chat_id, "يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 180
            x_text = w
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/rqaa2.ttf"
                size_font = 100
                if len(lines) == 1:
                    size_font = size_font + 50
                    y_text = y_text + 100
                else:
                    size_font = 100

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                yy = yy + 140
                print(yy)
                print(width, height)
                print(len(lines))
                stext = arabic_reshaper.reshape(line)
                text1 = bidi.algorithm.get_display(stext, encoding="utf-8")

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), text1, fill=(0, 0, 0), font=font, align="center")
                im.save(edit_img_loc, quality=100)
                y_text += (height * 2)
            await ms.edit("يتم التحميل ...")
            await ms.delete()
            await app.send_chat_action(chat_id=chat_id, action="upload_photo")
            await app.send_photo(chat_id, photo=edit_img_loc, caption="_")


async def qran_B  (client, message):
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await app.send_message(chat_id, "يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 180
            x_text = w
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/qraan.ttf"
                size_font = 100
                if len(lines) == 1:
                    size_font = size_font + 50
                else:
                    size_font = 130

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                yy = yy + 130
                print(yy)
                print(width, height)
                print(len(lines))
                stext = arabic_reshaper.reshape(line)
                text1 = bidi.algorithm.get_display(stext, encoding="utf-8")

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), text1, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            await ms.edit("يتم التحميل ...")
            await ms.delete()
            await app.send_chat_action(chat_id=chat_id, action="upload_photo")
            await app.send_photo(chat_id, photo=edit_img_loc, caption="_")

async def tbaa_B (client, message):
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await app.send_message(chat_id, "يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 180
            x_text = w
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/tbaa.ttf"
                size_font = 100
                if len(lines) == 1:
                    size_font = size_font + 50
                    y_text = y_text + 60
                else:
                    size_font = 100

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                yy = yy + 130
                print(yy)
                print(width, height)
                print(len(lines))
                stext = arabic_reshaper.reshape(line)
                text1 = bidi.algorithm.get_display(stext, encoding="utf-8")

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), text1, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            await ms.edit("يتم التحميل ...")
            await ms.delete()
            await app.send_chat_action(chat_id=chat_id, action="upload_photo")
            await app.send_photo(chat_id, photo=edit_img_loc, caption="_")


async def hsha_B (client, message):
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await app.send_message(chat_id, "يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 150
            x_text = w
            lines = textwrap.wrap(text, width=25)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/hsha.ttf"
                size_font = 100
                if len(lines) == 1:
                    size_font = size_font + 50
                    y_text =y_text +100
                else:
                    size_font = 130

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                yy = yy + 50
                print(yy)
                print(width, height)
                print(len(lines))
                stext = arabic_reshaper.reshape(line)
                text1 = bidi.algorithm.get_display(stext, encoding="utf-8")

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), text1, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            await ms.edit("يتم التحميل ...")
            await ms.delete()
            await app.send_chat_action(chat_id=chat_id, action="upload_photo")
            await app.send_photo(chat_id, photo=edit_img_loc, caption="_")

async def qyass_B (client, message):
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await app.send_message(chat_id, "يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 180
            x_text = w
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/qyasee.ttf"
                size_font = 100
                if len(lines) == 1:
                    size_font = size_font + 60
                    y_text =y_text +90
                else:
                    size_font = 140

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                yy = yy + 110
                print(yy)
                print(width, height)
                print(len(lines))
                stext = arabic_reshaper.reshape(line)
                text1 = bidi.algorithm.get_display(stext, encoding="utf-8")

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), text1, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            await ms.edit("يتم التحميل ...")
            await ms.delete()
            await app.send_chat_action(chat_id=chat_id, action="upload_photo")
            await app.send_photo(chat_id, photo=edit_img_loc, caption="_")



async def qyass2_B (client, message):
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await app.send_message(chat_id, "يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 60
            x_text = w
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/qyasee2.ttf"
                size_font = 120
                if len(lines) == 1:
                    size_font = size_font + 50
                    y_text =  y_text +100
                else:
                    size_font = 130

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                yy = yy + 110
                print(yy)
                print(width, height)
                print(len(lines))
                stext = arabic_reshaper.reshape(line)
                text1 = bidi.algorithm.get_display(stext, encoding="utf-8")

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), text1, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            await ms.edit("يتم التحميل ...")
            await ms.delete()
            await app.send_chat_action(chat_id=chat_id, action="upload_photo")
            await app.send_photo(chat_id, photo=edit_img_loc, caption="_")


async def hur_B(client, message):
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await app.send_message(chat_id, "يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 180
            x_text = w
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/hur.ttf"
                size_font = 100
                if len(lines) == 1:
                    size_font = size_font + 60
                    y_text = y_text + 80
                else:
                    size_font = 140

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                yy = yy + 190
                print(yy)
                print(width, height)
                print(len(lines))
                stext = arabic_reshaper.reshape(line)
                text1 = bidi.algorithm.get_display(stext, encoding="utf-8")

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), text1, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            await ms.edit("يتم التحميل ...")
            await ms.delete()
            await app.send_chat_action(chat_id=chat_id, action="upload_photo")
            await app.send_photo(chat_id, photo=edit_img_loc, caption="_")


async def hur2_B(client, message):
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await app.send_message(chat_id, "يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 120
            x_text = w
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/hur2.ttf"
                size_font = 100
                if len(lines) == 1:
                    size_font = size_font + 50
                    y_text = y_text + 100
                else:
                    size_font = 100 + 30

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                yy = yy + 100
                print(yy)
                print(width, height)
                print(len(lines))
                stext = arabic_reshaper.reshape(line)
                text1 = bidi.algorithm.get_display(stext, encoding="utf-8")

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), text1, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            await ms.edit("يتم التحميل ...")
            await ms.delete()
            await app.send_chat_action(chat_id=chat_id, action="upload_photo")
            await app.send_photo(chat_id, photo=edit_img_loc, caption="_")


async def alanat_B(client, message):
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await app.send_message(chat_id, "يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 180
            x_text = w
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/alanat.ttf"
                size_font = 100
                if len(lines) == 1:
                    size_font = size_font + 50
                else:
                    size_font = 100

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                yy = yy + 140
                print(yy)
                print(width, height)
                print(len(lines))
                stext = arabic_reshaper.reshape(line)
                text1 = bidi.algorithm.get_display(stext, encoding="utf-8")

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), text1, fill=(0, 0, 0), font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            await ms.edit("يتم التحميل ...")
            await ms.delete()
            await app.send_chat_action(chat_id=chat_id, action="upload_photo")
            await app.send_photo(chat_id, photo=edit_img_loc, caption="_")


async def alanat2_B(client, message):
    chat_id = message.chat.id
    userid = str(message.from_user["id"])
    text = message.reply_to_message.text
    dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 11):
        chunk = bg[i:i + 11]

        for photo in chunk:
            ms = await app.send_message(chat_id, "يتم التحميل ....")

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 110
            x_text = w
            lines = textwrap.wrap(text, width=30)
            await ms.edit("يتم التحميل .....")
            for line in lines:
                dir_font = "./fonts/alanat2.ttf"
                size_font = 100
                if len(lines) == 1:
                    size_font = size_font + 70
                    y_text = y_text +90
                else:
                    size_font = 150

                font = ImageFont.truetype(dir_font, size_font)
                width, height = font.getsize(line)
                yy = (w - width) / 2

                yy = yy + 240
                print(yy)
                print(width, height)
                print(len(lines))
                stext = arabic_reshaper.reshape(line)
                text1 = bidi.algorithm.get_display(stext, encoding="utf-8")

                if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                    os.makedirs(f"./DOWNLOADS/{userid}")
                download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".png"
                edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.png"

                draw = ImageDraw.Draw(im)
                draw.multiline_text((yy, y_text), text1, fill=(0, 0, 0), font=font, align="center")
                im.save(edit_img_loc, quality=100)
                y_text += height
            await ms.edit("يتم التحميل ...")
            await ms.delete()
            await app.send_chat_action(chat_id=chat_id, action="upload_photo")
            await app.send_photo(chat_id, photo=edit_img_loc, caption="_")

