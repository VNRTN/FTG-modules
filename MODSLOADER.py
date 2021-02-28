from .. import loader, utils

@loader.tds
class mld(loader.Module):
	strings = {"name": "MODSLOADER"}
	@loader.owner
	async def mldcmd(self, message):
		text = utils.get_args_raw(message)
		await message.edit(f'LOL')