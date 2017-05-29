from command import Command

class ShowDirectory(Command.Command):
	cmdName = "ShowDirectory"

	def getCommandName(self):
		return self.cmdName

	def executeCommand(self):
		return "Execute Show Directory"
