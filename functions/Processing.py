import os
import textwrap
import glob
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client, filters

async def edit1(client:Client,dir_bg,dir_font,color_t,size_font, message):
    chat_id = message.chat.id
    userid = str(message.reply_to_message.from_user["id"])
    text = message.reply_to_message.text

    # dir_bg = "./bg"
    bg = glob.glob(f"{dir_bg}/*.png")
    for i in range(0, len(bg), 1):
        chunk = bg[i:i +1]
        for photo in chunk:

            im = Image.open(photo)
            print(im)
            w, h = im.size
            y_text = 370
            lines = textwrap.wrap(text, width=40)
            if len (lines) > 1:
                y_text =y_text -70
            for line in lines:
                # dir_font = "./fonts/Amiri.ttf"
                # size_font = 105
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

                draw.multiline_text((yy, y_text), line, fill=color_t, font=font, align="right")
                im.save(edit_img_loc, quality=100)
                y_text += height
            ms = await client.send_message(chat_id, "يتم التحميل ....")
            y_top = (y_text  -  2*height) / (len(lines))
            y_bot = h - (y_top/2)
            dir_fot = "./fonts/Amiri.ttf"
            fot = ImageFont.truetype(dir_fot, 40)
            draw.multiline_text((((w - width) /2.4), y_text - 4), "ABDSH96", fill=color_t, font=fot,
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
