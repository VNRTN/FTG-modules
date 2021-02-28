from .. import loader, utils

	async def litcmd(self, message):
		text = utils.get_args_raw(message)
		link=text.split(' ')[0]
		text=text.split(' ')[1]
		await message.edit(f'<a href="{link}">{text}</a>')