# -*- coding: utf-8 -*-

# requires: pygments

from .. import loader, utils
from requests import get
import io
import logging
import pygments
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter
import os
logger = logging.getLogger(__name__)



@loader.tds
class WebShotMod(loader.Module):
    """Screenshot module"""
    strings = {
        "name": "Screenshot"
    }

    async def client_ready(self, client, db):
        self.client = client

    def __init__(self):
        self.name = self.strings['name']

    @loader.sudo
    async def webshotcmd(self, message):
        """Заскринить содержимое ссылки"""
        reply = None
        link = utils.get_args_raw(message)
        if not link:
            reply = await message.get_reply_message()
            if not reply:
                await message.delete()
                return
            link = reply.raw_text
        await message.edit("<b>Скриню...</b>")
        url = "https://webshot.deam.io/{}/?width=1920&height=1080?type=png"
        file = get(url.format(link))
        if not file.ok:
            await message.edit("<b>Что-то пошло не так...</b>")
            return
        file = io.BytesIO(file.content)
        file.name = "webScreenshot.png"
        file.seek(0)
        await message.client.send_file(message.to_id, file, reply_to=reply)
        await message.delete()

    async def fileshotcmd(self, message):
        """Заскринить содержимое файла .py"""
        await message.edit("<b>Скриню...</b>")
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("<b>Реплай на file.py</b>")
            return
        media = reply.media
        if not media:
            await message.edit("<b>Реплай на file.py</b>")
            return
        file = await message.client.download_file(media)
        text = file.decode('utf-8')
        pygments.highlight(text, Python3Lexer(), ImageFormatter(font_name='DejaVu Sans Mono', line_numbers=True),
                           'fileScreenshot.png')
        await message.client.send_file(message.to_id, 'fileScreenshot.png', force_document=True)
        os.remove("fileScreenshot.png")
        await message.delete()

