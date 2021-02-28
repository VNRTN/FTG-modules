from .. import loader, utils

@loader.tds
class LinkInTextMod(loader.Module):
	strings = {"name": "Хуй знает"}
	@loader.owner
	async def mldcmd(self, message):
		text = utils.get_args_raw(message)
		await message.edit(f'LOL')
		await sleep(8)
		await message.edit(f'LOL1')