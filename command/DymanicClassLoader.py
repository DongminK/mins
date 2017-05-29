import os, sys

PKG_PATH = 'list'

def getClass(name):
	pkgFullName = PKG_PATH + "." + name
	pkg = __import__(pkgFullName, fromlist=[''])
	return getattr(pkg, name)

def loadClass():

	mapClz = {}

	for root, dirs, files in os.walk(PKG_PATH):
		for file in files:
			if not file.startswith("__") and file.endswith(".py"):
				clzName = file.replace(".py", "")
				clz = getClass(clzName)
				mapClz[clzName] = clz

	return mapClz


if __name__ == "__main__":

	arg = sys.argv

	# Argument가 2개 (파일명, Argument)가 아닐경우 오류를 발생시킨다.
	if len(arg) != 2:
		print("Invalid argument - %s" % arg)
	else:
		mapClz = loadClass()

		# Argument에 따른 명령어 분기 (명령어 이해는 앞단에서 처리)
		command = arg[1]

		print(mapClz[command].getCommandName(mapClz[command]))
		print(mapClz[command].executeCommand(mapClz[command]))
