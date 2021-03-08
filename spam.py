from .. import loader, utils
from asyncio import sleep, gather
from telethon import events

def register(cb):
    cb(SpamMod())

class SpamMod(loader.Module):
    """Спам модуль"""
    strings = {'name': 'Spam'}

    async def spamcmd(self, message):
        """Обычный спам. Используй .spam <кол-во:int> <текст или реплай>."""
        try:
            await message.delete()
            args = utils.get_args(message)
            count = int(args[0].strip())
            reply = await message.get_reply_message()
            if reply:
                if reply.media:
                    for _ in range(count):
                        await message.client.send_file(message.to_id, reply.media)
                    return
                else:
                    for _ in range(count):
                        await message.client.send_message(message.to_id, reply)
            else:
                message.message = " ".join(args[1:])
                for _ in range(count):
                    await gather(*[message.respond(message)])
        except: return await message.client.send_message(message.to_id, '.spam <кол-во:int> <текст или реплай>.')


    async def cspamcmd(self, message):
        """Спам символами. Используй .cspam <текст или реплай>."""
        await message.delete()
        reply = await message.get_reply_message()
        if reply:
            msg = reply.text
        else:
            msg = utils.get_args_raw(message)
        msg = msg.replace(' ', '')
        for m in msg:
            await message.respond(m)


    async def wspamcmd(self, message):
        """Спам словами. Используй .wspam <текст или реплай>."""
        await message.delete()
        reply = await message.get_reply_message()
        if reply:
            msg = reply.text
        else:
            msg = utils.get_args_raw(message)
        msg = msg.split()
        for m in msg:
            await message.respond(m)


    async def delayspamcmd(self, message):
        """Спам с задержкой. Используй .delayspam <время:int> <кол-во:int> <текст или реплай>."""
        try:
            await message.delete()
            args = utils.get_args_raw(message)
            reply = await message.get_reply_message()
            time = int(args.split(' ', 2)[0])
            count = int(args.split(' ', 2)[1])
            if reply:
                if reply.media:
                    for _ in range(count):
                        await message.client.send_file(message.to_id, reply.media, reply_to=reply.id)
                        await sleep(time)
                else:
                    for _ in range(count):
                        await reply.reply(args.split(' ', 2)[2])
                        await sleep(time)
            else:
                spammsg = args.split(' ', 2)[2]
                for _ in range(count):
                    await message.respond(spammsg)
                    await sleep(time)
        except: return await message.client.send_message(message.to_id, '.delayspam <время:int> <кол-во:int> <текст или реплай>')

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    async def mediaspamcmd(self, message):
        """.mediaspam <количество> + реплай на медиа(стикер/гиф/фото/видео/войс/видеовойс)"""
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("<code>.mediaspam <количество> + реплай на медиа(стикер/гиф/фото/видео/войс/видеовойс</code>")
            return
        if not reply.media:
            await message.edit("<code>.mediaspam <количество> + реплай на медиа(стикер/гиф/фото/видео/войс/видеовойс</code>")
            return
        media = reply.media
	
        args = utils.get_args(message)
        if not args:
            await message.edit("<code>.mediaspam <количество> + реплай на медиа(стикер/гиф/фото/видео/войс/видеовойс</code>")
            return
        count = args[0]
        count = count.strip()
        if not count.isdigit():
            await message.edit("<code>.mediaspam <количество> + реплай на медиа(стикер/гиф/фото/видео/войс/видеовойс</code>")
            return
        count = int(count)
		
        await message.delete()
        for _ in range(count):
            await message.client.send_file(message.to_id, media)