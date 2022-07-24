#!/usr/bin/env python3
import re
import os
import base64
import hashlib
import uuid
from jinja2 import Template

def checkFilename(s):
    if('/' in s or not 5 < len(s) < 30):
        raise 'Bad filename'

def printMenu():
    print('1. Create')
    print('2. Rename')
    print('3. List')
    print('4. Compile')
    print('5. Flag')
    print('6. Exit')

def handleCreateFile():
    filename = input('Filename > ')
    fileContent = base64.b64decode(input('Base64 encoded content > '))

    checkFilename(filename)
    if(len(fileContent) > 500):
        raise 'too large'

    with open('./'+filename,'wb') as f:
        f.write(fileContent)

    print('Created the file!')

def handleRenameFile():
    sFilename = input('From filename > ')
    tFilename = input('To filename > ')
    
    checkFilename(sFilename)
    checkFilename(tFilename)

    os.rename(sFilename,tFilename)
    print('Renamed the file!')

def handleCompile():
    tFilename = input('Enter template filename > ')
    oFilename = input('Enter output filename > ')
    checkFilename(tFilename)
    checkFilename(oFilename)

    with open('./'+tFilename) as f:
        fileContent = f.read()
        if('(' in fileContent or '.' in fileContent):
            raise 'Ahh not allowed sorry!'
        t = Template(fileContent).render()
        with open(oFilename,'w') as ff:
            ff.write(t)
    print('Template compiled!')

def handleFlag():
    with open('./flag.txt','w') as f:
        f.write(open('/flag').read())
    print('Wrote the flag file!')

def handleListdir():
    print('\n'.join(os.listdir()))


def getUserFolderDir(userUUID):
    r = os.path.dirname(os.path.abspath(__file__))
    r += '/files/'+hashlib.md5(userUUID.encode()).hexdigest()
    return r
    
if(__name__ == '__main__'):
    inp = input('Enter your uuid or ENTER to create a new environment: ')
    userUUID = None

    if(len(inp) == 0):
        userUUID = uuid.uuid4().__str__()
        print(f'Your UUID is {userUUID}')
    else:
        if(not re.match('^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',inp)):
            print('Incorrect UUID')
            exit(0)
        userUUID = inp

    cwdDir = getUserFolderDir(userUUID)
    if(not os.path.exists(cwdDir)):
        os.makedirs(cwdDir)

    os.chdir(cwdDir)

    handlers = [handleCreateFile,handleRenameFile,handleListdir,handleCompile,handleFlag,exit]
    while(1):
        printMenu()
        handlers[int(input('Input Selection\n> '))-1]()        
