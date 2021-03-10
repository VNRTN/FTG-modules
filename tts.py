import io
import requests
from .. import loader, utils

def register(cb):
    cb(TTSMod())


class TTSMod(loader.Module):
    """Озвучивание текста"""

    strings = {"name": "Text to speech",
               "tts_lang_cfg": "Set your language code for the TTS here.",
               "tts_needs_text": "<code>I need some text to convert to speech!</code>",
               "no_text": "Мне нечего говорить"}

    def __init__(self):
        self.config = loader.ModuleConfig("TTS_LANG", "en", lambda m: self.strings("tts_lang_cfg", m))

    async def say(self, message, speaker, text, file=".dtts.mp3"):
        if not text:
            return await utils.answer(message, self.strings["no_text"])

        reply = await message.get_reply_message()
        await message.delete()
        data = {"text": text}
        if speaker:
            data.update({"speaker": speaker})

        # creating file in memory
        f = io.BytesIO(requests.get("https://station.aimylogic.com/generate", data=data).content)
        f.name = file

        await message.client.send_file(message.to_id, f, voice_note=True, reply_to=reply)

    async def ttslcmd(self, message):
        """Levitan voice"""
        await self.say(message, "levitan", utils.get_args_raw(message))

    async def ttsocmd(self, message):
        """Oksana voice"""
        await self.say(message, "oksana", utils.get_args_raw(message))

    async def ttsycmd(self, message):
        """Yandex voice"""
        await self.say(message, None, utils.get_args_raw(message))