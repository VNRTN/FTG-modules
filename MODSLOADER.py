from .. import loader, utils

@loader.tds
class MODSLOADER(loader.Module):
	strings = {"name": "MODSLOADER"}
	@loader.owner
	async def MLDcmd(self, message):
		text = utils.get_args_raw(message)
		await message.edit(f'LOL')
		await message.edit(f'LOL1')