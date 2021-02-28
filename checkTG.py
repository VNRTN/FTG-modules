from .. import loader, utils
import requests
def register(cb):
    cb(CheckerTGMod())
class CheckerTGMod(loader.Module):
    """CheckerTG"""
    strings = {
        'name': 'CheckerTG',
        'check': '<b>[CheckerAPI]</b> Делаем запрос к API...',
        'response':'<b>[CheckerAPI]</b> Ответ API: <code>{}</code>\nВремя выполнения: <code>{}</code>'
        }
    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()
    async def checkcmd(self, m):
        """ Проверить id на слитый номер
        Жуёт либо <reply> либо <uid>
        """
        reply = await m.get_reply_message()
        if utils.get_args_raw(m): user = utils.get_args_raw(m)
        elif reply:
            try: user = str(reply.sender.id)
            except: return await m.edit("<b>Err</b>")    
        else: return await m.edit("[CheckerAPI] А кого чекать?")
        await m.edit(self.strings['check'])
        r = requests.get('http://d4n13l3k00.ml/api/checkTgId?uid=' + user).json()
        await m.edit(self.strings['response'].format(r['data'], str(round(r['time'], 3))+"ms"))