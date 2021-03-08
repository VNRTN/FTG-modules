import io
import os
import subprocess
import random
import requests
import asyncio
import logging
import string
from random import choice, randint
from .. import loader, utils
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO
from textwrap import wrap
from gsbl.stick_bug import StickBug
from random import randrange as r

logger = logging.getLogger(__name__)

backgrouds = ["https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor2.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor3.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor4.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor5.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor6.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor7.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor8.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor9.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor10.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor11.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor12.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor13.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor14.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor15.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor16.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor17.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor18.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor19.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor20.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor21.png",
              "https://raw.githubusercontent.com/Fl1yd/FTG-modules/master/stuff/impostor22.png"]
background = requests.get(f"{choice(backgrouds)}").content

class ZapomniMod(loader.Module):
	strings = {'name': 'Memes',
			   "reply": "Reply to video!",
			   "error": "ERROR! TRY AGAIN!!",
			   "processing": "DataDataMoshMosh!"}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    async def zcmd(self, message):
        ufr = requests.get("http://d4n13l3k00.ml/Modules/zfont.ttf")
        f = ufr.content

        reply = await message.get_reply_message()
        txet = utils.get_args_raw(message)
        if not txet:
            if not reply:
                await message.edit("text?")
            else:
                txt = reply.raw_text
        else:
            txt = utils.get_args_raw(message)

        await message.edit("<b>Извиняюсь...</b>")
        pic = requests.get("https://www.meme-arsenal.com/memes/5a06f172486c5b4008c75774717a6c95.jpg")
        pic.raw.decode_content = True
        img = Image.open(io.BytesIO(pic.content)).convert("RGB")
        black = Image.new("RGBA", img.size, (0, 0, 0, 100))
        img.paste(black, (0, 0), black)

        W, H = img.size
        txt = txt.replace("\n", "𓃐")
        text = "\n".join(wrap(txt, 40))
        t = "Запомните твари:\n" + text
        t = t.replace("𓃐", "\n")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(io.BytesIO(f), 32, encoding='UTF-8')
        w, h = draw.multiline_textsize(t, font=font)
        imtext = Image.new("RGBA", (w + 20, h + 20), (0, 0, 0, 0))
        draw = ImageDraw.Draw(imtext)
        draw.multiline_text((10, 10), t, (255, 255, 255), font=font, align='center')
        imtext.thumbnail((W, H))
        w, h = imtext.size
        img.paste(imtext, ((W - w) // 2, (H - h) // 2), imtext)
        out = io.BytesIO()
        out.name = "out.jpg"
        img.save(out)
        out.seek(0)
        await message.client.send_file(message.to_id, out, reply_to=reply)
        await message.delete()

    async def impcmd(self, message):
        """Используй: .imp <@ или текст или реплай>."""
        try:
            font = requests.get("https://github.com/Fl1yd/FTG-modules/blob/master/stuff/font2.ttf?raw=true").content
            await message.edit("Минуточку...")
            reply = await message.get_reply_message()
            args = utils.get_args_raw(message)
            imps = ['wasn`t the impostor', 'was the impostor']
            if not args and not reply:
                user = await message.client.get_me()
                text = (f"{user.first_name} {choice(imps)}.\n"
                        f"{randint(1, 2)} impostor(s) remain.")
            if reply:
                user = await utils.get_user(await message.get_reply_message())
                text = (f"{user.first_name} {choice(imps)}.\n"
                        f"{randint(1, 2)} impostor(s) remain.")
            if args:
                user = await message.client.get_entity(args)
                text = (f"{user.first_name} {choice(imps)}.\n"
                        f"{randint(1, 2)} impostor(s) remain.")
            font = io.BytesIO(font)
            font = ImageFont.truetype(font, 30)
            image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
            draw = ImageDraw.Draw(image)
            w, h = draw.multiline_textsize(text=text, font=font)
            image = Image.open(io.BytesIO(background))
            x, y = image.size
            draw = ImageDraw.Draw(image)
            draw.multiline_text(((x - w) // 2, (y - h) // 2), text=text, font=font, fill="white", align="center")
            output = io.BytesIO()
            output.name = "impostor.png"
            image.save(output, "png")
            output.seek(0)
            await message.client.send_file(message.to_id, output, reply_to=reply)
            await message.delete()
        except:
            text = args
            font = io.BytesIO(font)
            font = ImageFont.truetype(font, 30)
            image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
            draw = ImageDraw.Draw(image)
            w, h = draw.multiline_textsize(text=text, font=font)
            image = Image.open(io.BytesIO(background))
            x, y = image.size
            draw = ImageDraw.Draw(image)
            draw.multiline_text(((x - w) // 2, (y - h) // 2), text=text, font=font, fill="white", align="center")
            output = io.BytesIO()
            output.name = "impostor.png"
            image.save(output, "png")
            output.seek(0)
            await message.client.send_file(message.to_id, output, reply_to=reply)
            await message.delete()

    async def ruimpcmd(self, message):
        """Используй: .ruimp <@ или текст или реплай>."""
        try:
            font = requests.get("https://github.com/Fl1yd/FTG-modules/blob/master/stuff/font2.ttf?raw=true").content
            await message.edit("Минуточку...")
            reply = await message.get_reply_message()
            args = utils.get_args_raw(message)
            imps = ['не был предателем', 'оказался одним из предалатей']
            remain = randint(1, 2)
            if remain == 1:
                if not args and not reply:
                    user = await message.client.get_me()
                    text = (f"{user.first_name} {choice(imps)}.\n"
                            "1 предатель остался.")
                if reply:
                    user = await utils.get_user(await message.get_reply_message())
                    text = (f"{user.first_name} {choice(imps)}.\n"
                            "1 предатель остался.")
                if args:
                    user = await message.client.get_entity(args)
                    text = (f"{user.first_name} {choice(imps)}.\n"
                            "1 предатель остался.")
            else:
                if not args and not reply:
                    user = await message.client.get_me()
                    text = (f"{user.first_name} {choice(imps)}.\n"
                            "2 предателя осталось.")
                if reply:
                    user = await utils.get_user(await message.get_reply_message())
                    text = (f"{user.first_name} {choice(imps)}.\n"
                            "2 предателя осталось.")
                if args:
                    user = await message.client.get_entity(args)
                    text = (f"{user.first_name} {choice(imps)}.\n"
                            "2 предателя осталось.")
            font = io.BytesIO(font)
            font = ImageFont.truetype(font, 30)
            image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
            draw = ImageDraw.Draw(image)
            w, h = draw.multiline_textsize(text=text, font=font)
            image = Image.open(io.BytesIO(background))
            x, y = image.size
            draw = ImageDraw.Draw(image)
            draw.multiline_text(((x - w) // 2, (y - h) // 2), text=text, font=font, fill="white", align="center")
            output = io.BytesIO()
            output.name = "impostor.png"
            image.save(output, "png")
            output.seek(0)
            await message.client.send_file(message.to_id, output, reply_to=reply)
            await message.delete()
        except:
            text = args
            font = io.BytesIO(font)
            font = ImageFont.truetype(font, 30)
            image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
            draw = ImageDraw.Draw(image)
            w, h = draw.multiline_textsize(text=text, font=font)
            image = Image.open(io.BytesIO(background))
            x, y = image.size
            draw = ImageDraw.Draw(image)
            draw.multiline_text(((x - w) // 2, (y - h) // 2), text=text, font=font, fill="white", align="center")
            output = io.BytesIO()
            output.name = "impostor.png"
            image.save(output, "png")
            output.seek(0)
            await message.client.send_file(message.to_id, output, reply_to=reply)
            await message.delete()

    async def jakcmd(self, message):
        """.jak <реплай на изображение.>"""
        reply = await message.get_reply_message()
        txet = utils.get_args_raw(message)
        if not txet:
            if not reply:
                await message.edit("где реплай на медиа. или текст.")
            else:
                pic = await check_media(message, reply)
                if not pic:
                    await utils.answer(message, 'это не изображение лол.')
                    return
                what = haha(pic)
                await message.delete()
                await message.client.send_file(message.to_id, what)
        else:
            pic = requests.get(
                "https://github.com/SpyderJabro/SpYD3R/blob/master/modul/photo_2020-09-02_13-18-13.jpg?raw=true")
            pic.raw.decode_content = True
            img = Image.open(io.BytesIO(pic.content)).convert("RGB")
            if len(txet) < 5:
                W, H = 900, 1050
            elif len(txet) < 10:
                W, H = 700, 1000
            elif len(txet) < 20:
                W, H = 500, 1000
            elif len(txet) < 30:
                W, H = 300, 1000
            elif len(txet) < 60:
                W, H = 300, 950
            elif len(txet) < 120:
                W, H = 300, 900
            else:
                W, H = 600, 700
            ufr = requests.get("https://github.com/LaciaMemeFrame/FTG-Modules/raw/master/zfont.ttf")
            f = ufr.content
            txt = utils.get_args_raw(message)
            txt = txt.replace("\n", "𓃐")
            text = "\n".join(wrap(txt, 30))
            t = text
            t = t.replace("𓃐", "\n")
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(io.BytesIO(f), 72, encoding='UTF-8')
            w, h = draw.multiline_textsize(t, font=font)
            imtext = Image.new("RGBA", (w, h), (0, 0, 0, 0))
            draw = ImageDraw.Draw(imtext)
            draw.multiline_text((1, 1), t, (0, 0, 0), font=font, align='center')
            imtext.thumbnail((600, 300))
            w, h = 150, 300
            img.paste(imtext, ((W - w) // 3, (H - h) // 2), imtext)
            out = io.BytesIO()
            out.name = "out.jpg"
            img.save(out)
            out.seek(0)
            await message.client.send_file(message.to_id, out)
            await message.delete()

    async def gsblcmd(self, event):
        """Используй .gsbl <реплай на картинку/стикер>."""
        try:
            reply = await event.get_reply_message()
            if not reply:
                return await event.edit("Нет реплая на картинку/стикер.")
            await event.edit("Минуточку...")
            im = io.BytesIO()
            await event.edit("Скачиваю...")
            await event.client.download_file(reply, im)
            await event.edit("Обрабатываю...")
            im = Image.open(im)
            sb = StickBug(im)
            sb.save_video("get_stick_bugged_lol.mp4")
            await event.edit("Отправляю...")
            await event.client.send_file(event.to_id, open("get_stick_bugged_lol.mp4", "rb"), reply_to=reply)
            os.remove("get_stick_bugged_lol.mp4")
            await event.delete()
        except:
            return await event.edit("Это не картинка/стикер.")

    async def haircmd(self, message):
        """Волос!"""
        reply = await message.get_reply_message()
        if not reply: return await message.edit("Нет реплая на картинку/стикер.")
        if reply.file.mime_type.split('/')[0] == "image":
            im = Image.open(io.BytesIO(await message.client.download_file(reply, bytes)))
            draw = ImageDraw.Draw(im)
            w, h = im.size
            draw.arc((r(w), r(h), r(w) + r(300), r(h) + r(550)), r(350), 180 + r(350), fill="black", width=1)
            out = io.BytesIO()
            out.name = f"witHair{reply.file.ext}"
            im.save(out)
            out.seek(0) 
            await message.client.send_file(message.to_id, out, reply_to=reply.id if reply else None) 
            await message.delete()
        else: return await message.edit("Это не картинка/стикер.")

    async def vshcmd(self, m):
	    ".vsh <реплай на видео> <уровень от 1 до 6 (по умолчанию 3)>\
	    \nСшакалить видео"
	    lvls = {
	        "1":"0.1M",
	        "2":"0.08M",
	        "3":"0.05M",
	        "4":"0.03M",
	        "5":"0.02M",
	        "6":"0.01M"
	    }
	    reply = await m.get_reply_message()
	    if not reply: return await m.edit("reply...")
	    if reply.file.mime_type.split("/")[0]=="video":
	        args = utils.get_args_raw(m)
	        if args:
	            if args in lvls:
	                lvl = lvls[args]
	            else:
	                await message.edit("не знаю такого")
	                return
	        else:
	            lvl = lvls["3"]
	        await m.edit("[Шакал] Качаю...")
	        vid = await reply.download_media("".join([random.choice(string.ascii_letters) for i in range(25)])+".mp4")
	        out = "".join([random.choice(string.ascii_letters) for i in range(25)])+".mp4"
	        await m.edit("[Шакал] Шакалю...")
	        os.system(f"ffmpeg -y -i \"{vid}\" -b:v {lvl} -maxrate:v {lvl} -b:a {lvl} -maxrate:a {lvl} \"{out}\"")
	        await m.edit("[Шакал] Отправляю...")
	        await reply.reply(file=out)
	        await m.delete()
	        os.remove(vid)
	        os.remove(out)
	    else:
	        await m.edit("shit...")
	        return

    async def datamoshcmd(self, message):
        """. datamosh lvl: int <reply to video>"""
        fn = "if_you_see_it_then_delete_it"
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("".join([ random.choice(html).format(ch) for ch in self.strings("reply", message)]))
            return
        if not reply.video:
            await message.edit("".join([ random.choice(html).format(ch) for ch in self.strings("reply", message)]))
            return
        else:
            await reply.download_media(fn+"1.mp4")
        
        lvl = 1
        fp = False
        args = utils.get_args(message)
        if args:
            if len(args) == 1:
                if args[0].isdigit():
                    lvl = int(args[0])
                    if lvl <= 0:
                        lvl = 1
                else:
                    fp = True
            if len(args) > 1:
                fp = True
                if args[0].isdigit():
                    lvl = int(args[0])
                    if lvl <= 0:
                        lvl = 1
                elif args[1].isdigit():
                    fp = True
                    lvl = int(args[1])
                    if lvl <= 0:
                        lvl = 1

        await message.edit("".join([ random.choice(html).format(ch) for ch in self.strings("processing", message)]))
        subprocess.call(f'ffmpeg -loglevel quiet -y -i {fn}1.mp4 -crf 0 -bf 0 {fn}1.avi', shell=True)
        try:
            _f = open(fn+'1.avi', 'rb')
            f_ = open(fn+'2.avi', 'wb')
        except FileNotFoundError:
            await message.edit("".join([ random.choice(html).format(ch) for ch in self.strings("error", message)]))
            os.system(f"rm -f {fn}*")
            return
            
        frs = _f.read().split(b'00dc')
        fi = b'\x00\x01\xb0'
        cf = 0
        for _, fr in enumerate(frs):
            if fp == False:
                f_.write(fr + b'00dc')
                cf += 1
                if fr[5:8] == fi:
                    fp = True
            else:
                if fr[5:8] != fi:
                    cf += 1
                    for i in range(lvl):
                        f_.write(fr + b'00dc')
        f_.close()
        _f.close()
        
        subprocess.call(f'ffmpeg -loglevel quiet -y -i {fn}2.avi {fn}2.mp4', shell=True)
        await reply.reply(file=fn+"2.mp4")
        os.system(f"rm -f {fn}*")
        await message.delete()
        
html = ["<b>{}<b>", "<code>{}</code>", "<i>{}</i>", "<del>{}</del>", "<u>{}</u>", '<a href="https://bruh.moment">{}</a>']

def lol(background, image, cords, size):
    overlay = Image.open(BytesIO(image))
    overlay = overlay.resize((size * 7, size * 4))
    background.paste(overlay, cords)


def haha(image):
    pics = requests.get("https://github.com/SpyderJabro/SpYD3R/blob/master/modul/photo_2020-09-02_13-18-13.jpg?raw=true")
    pics.raw.decode_content = True
    img = Image.open(io.BytesIO(pics.content)).convert("RGBA")
    lol(img, image, (30, 140), 90)
    out = io.BytesIO()
    out.name = "outsider.png"
    img.save(out)
    return out.getvalue()




async def check_media(message, reply):
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if reply.gif or reply.video or reply.audio or reply.voice:
                return None
            data = reply.media.document
        else:
            return None
    else:
        return None
    if not data or data is None:
        return None
    else:
        data = await message.client.download_media(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None