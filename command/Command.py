class Command:

	def getCommandName(self):
		raise NotImplementedError()

	def executeCommand(self):
		raise NotImplementedError()