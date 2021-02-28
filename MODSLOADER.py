from .. import loader, utils

@loader.tds
class MODSLOADER(loader.Module):
	strings = {"name": "MODSLOADER"}
	@loader.owner
	async def MLDcmd(self, message):
        Delay = float('5')
		text = utils.get_args_raw(message)
		await message.edit(f'LOL')
		await sleep (Delay)
		await message.edit(f'LOL1')