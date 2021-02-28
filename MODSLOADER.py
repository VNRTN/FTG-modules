from .. import loader, utils

@loader.tds
class LinkInTextMod(loader.Module):
	strings = {"name": "MODSLOADER"}
	@loader.owner
	async def MLDcmd(self, message):
		text = utils.get_args_raw(message)
		await message.edit(f'LOL')