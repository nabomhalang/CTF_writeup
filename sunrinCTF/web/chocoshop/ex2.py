import jwt
import json
from time import time
from requests import get

server = "http://host1.dreamhack.games:13900"

res_session = json.loads(get(server + "/session").text)["session"]
res_claim = json.loads(
    get(server + "/coupon/claim", headers={"Authorization": res_session}).text
)["coupon"]
res_jwt = jwt.decode(res_claim, algorithms="HS256", options={"verify_signature": False})

print(f"session: {res_session}")
print(f"rawjwt: {res_claim}")
print(f"jwt: {res_jwt}")