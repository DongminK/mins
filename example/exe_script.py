import os
import subprocess

command = 'dir'

result = os.system(command)

print('==================')
print(result)
print('==================')

result = subprocess.call(command, shell=True)

print('>>>>>>>>>>>>>>>>>>>==================')
print(result)
print('>>>>>>>>>>>>>>>>>>>==================')

result = subprocess.check_output(command, shell=True)

print('==================')
print(result)
print('==================')
