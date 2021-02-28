from .. import loader, utils
import os, string, random
@loader.tds
class VSHAKALMod(loader.Module):
  strings = {"name": "Video Shakal"}
  @loader.owner
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