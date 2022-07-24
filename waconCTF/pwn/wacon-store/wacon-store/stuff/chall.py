#!/usr/bin/python3.9
import wacon_store
import sys


print('Input your payload: (Ended with "\\nEOF\\n")')
buf = ""
mapsFile = open('/proc/self/maps')
while(True):
	f = input()
	if(f == 'EOF'):
		break
	buf += f+'\n'

def gift():
	return mapsFile.read()

if(len(buf) > 500):
	raise Exception(':(')

for module in set(sys.modules.keys()):
    if module in sys.modules:
        del sys.modules[module]

wacon_store.open_store()
exec(buf,{'__builtins__' : None},{'buy':wacon_store.buy,'print':print,'int':int,'gift':gift})
