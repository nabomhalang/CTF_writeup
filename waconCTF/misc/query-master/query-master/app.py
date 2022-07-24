#!/usr/bin/python3
import random
import string
import subprocess

def randName():
    return ''.join([random.choice(string.hexdigits) for i in range(16)])

dbpath = f'1.db'

query = input("Query >> ")

ban = ['.', 'lo', ';']

for x in ban:
    if x in query:
        print("Filtered..")
        exit()

proc = subprocess.Popen(["sqlite3", dbpath, query], stdout=subprocess.PIPE)
(out, err) = proc.communicate()

print(out.decode())
