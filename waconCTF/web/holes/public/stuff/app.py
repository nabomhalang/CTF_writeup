#!/usr/bin/env python3
import os
import hashlib
import re
from flask import Flask,request,send_from_directory

def getUserFolderDir(userUUID):
    r = os.path.dirname(os.path.abspath(__file__))
    r += '/files/'+hashlib.md5(userUUID.encode()).hexdigest()
    return r
    
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
	pathes = path.split('/')
	userUUID = pathes[0]
	del pathes[0]
	path = '/'.join(pathes)

	if(not re.match('^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',userUUID)):
		return "Incorrect UUID",400,{'Content-Type': 'text/plain;charset=utf-8'}

	if('..' in path):
		return "Dangerous path",400,{'Content-Type': 'text/plain;charset=utf-8'}

	if(path == ''):
		path = 'index.html'

	userDir = getUserFolderDir(userUUID)+'/'+path
	if(not os.path.exists(userDir)):
		return 'Folder not found :? Create one with the management console',404,{'Content-Type': 'text/plain;charset=utf-8'}

	try:
		with open(userDir) as f:
			content = f.read()
			if('flag' in content):
				return 'ᕙ(^▿^-ᕙ)',400,{'Content-Type': 'text/plain;charset=utf-8'}
			return content,200,{'Content-Type':'text/html'} 
	except:
		return 'Smth bad happened',500

if(__name__ == '__main__'):
	app.run(host='0.0.0.0',port=8000)
