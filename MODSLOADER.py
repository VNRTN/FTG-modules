from .. import loader, utils

@loader.tds
class loadermodsgit(loader.Module):
	strings = {"name": "loadermodsgit"}
	@loader.owner
	async def mldcmd(self, message):
		text = utils.get_args_raw(message)
		await message.edit(f'LOL')
		await sleep(5)
		await message.edit(f'LOL1')