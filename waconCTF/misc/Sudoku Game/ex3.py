import random
from sudoku import Sudoku
from pwn import *

p = remote("114.203.209.119", 9001)
context.log_level='debug'

INDEX = [[x, y] for x in range(0, 9) for y in range(0, 9)]

def z3_solving(sudoku):
    """ Function solving the given sudoku puzzle using Z3 """

    from z3 import Solver, Int, Or, Distinct, sat
    symbols = {pos: Int(pos) for pos in sudoku.positions}
    s = Solver()

    for symbol in symbols.values():
        s.add(Or([symbol == i for i in range(1, 10)]))

    for row in "ABCDEFGHI":
        s.add(Distinct([symbols[row + col] for col in "123456789"]))

    for col in "123456789":
        s.add(Distinct([symbols[row + col] for row in "ABCDEFGHI"]))

    for i in range(3):
        for j in range(3):
            s.add(Distinct([symbols["ABCDEFGHI"[m + i * 3] + "123456789"[n + j * 3]] for m in range(3) for n in range(3)]))

    for pos, value in sudoku.grid.items():
        if value in "123456789":
            s.add(symbols[pos] == value)

    if s.check() != sat:
        raise Exception("unsolvable")

    model = s.model()
    values = {pos: model.evaluate(s).as_string() for pos, s in symbols.items()}
    return Sudoku(values)

BORAD = "".join(['.'*9 for _ in range(9)])

def select(arr):
    idx = random.choice(INDEX)
    temp = INDEX.pop(INDEX.index(idx))
    x = temp[0]
    y = temp[1]
    num = arr[x][y]
    
    return x, y, num

def change(arr):
    
    temp = ""
    for i in arr:
        for j in i:
            temp += j
    return temp


for _ in range(81):
    print("[+] parsing puzzle:", BORAD)
    s = Sudoku.parse(BORAD)
    
    print("[+] start solving using Z3")

    s_solved = z3_solving(s)

    print("[+] solved:", s_solved.is_solved())
    sov = str(s_solved)
    print(s_solved)

    arr_sol = [ [sov[i] for i in range(9)] for _ in range(9) ]
    arr_bor = [ [BORAD[i] for i in range(9)] for _ in range(9) ]

    x, y, num = select(arr_sol)
    print(x, y, num)
    arr_bor[x][y] = num
    
    BORAD = change(arr_bor)
    print(BORAD)


    

# p.sendlineafter(b'Please submit your team token >', b'GOD_HGK_GOD')

# p.sendlineafter(b'> ', str(2))

# p.sendlineafter(b'Do you want to see a board for each moves?(T/F) > ', b'T')

# while True:
#     recv = p.recvuntil(b'> ')
#     if b'Your turn' in recv:
#         x, y, num = select()
#         grid[x][y] = num
#         puzzle(grid)
        
#         payload = str(x) + " " + str(y) + " " + str(num)
#         p.sendline(payload.encode())

#     elif b'AI move' in recv:
#         AI = list(map(int, p.recvline().strip().split(b' ')))
#         grid[AI[0]][AI[1]] = AI[2]
        
#     pause()

# p.interactive()