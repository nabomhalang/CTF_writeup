from re import X
from pwn import *

p = remote("114.203.209.119", 9001)
context.log_level='debug'

board = [[0]*9 for _ in range(9)]
INDEX = [(x, y) for x in range(0, 9) for y in range(0, 9)]
INDEX_ELE = [ [ [i for i in range(1, 10)] for _ in range(9) ] for _ in range(9) ]

def print_arr(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end='')
        print()


def delete(X, Y, num): # 0 0 1
    board[X][Y] = num
    for i in range(9):
        try:
            INDEX_ELE[i][Y].pop(INDEX_ELE[i][Y].index(num)) # y축을 바꾸고 싶음 y가 고정이여야함
            INDEX_ELE[X][i].pop(INDEX_ELE[X][i].index(num))
        except ValueError:
            pass

    INDEX.pop(INDEX.index((X, Y)))

def select():
    idx = random.randint(0, len(INDEX))
    x = INDEX[idx][0]
    y = INDEX[idx][1]
    print(INDEX_ELE[x][y])
    val = random.choice(INDEX_ELE[x][y])
    num = INDEX_ELE[x][y][INDEX_ELE[x][y].index(val)]
    
    print_arr(board)
    print_arr(INDEX_ELE)
    print(INDEX)
    
    print(f'idx : {idx}, x : {x}, y : {y}, val : {val}, num : {num}')
    delete(x, y, num)
    return x, y, num

for _ in range(81):
    x, y, num = select()
    # select()
    print(f'x : {x} y : {y} num : {num}')


p.sendlineafter(b'Please submit your team token >', b'GOD_HGK_GOD')

p.sendlineafter(b'> ', str(2))

p.sendlineafter(b'Do you want to see a board for each moves?(T/F) > ', b'T')

while True:
    recv = p.recvuntil(b'> ')
    if b'Your turn' in recv:
        x, y, num = select()
        board[x][y] = num
        delete(x, y, num)
        payload = str(x) + " " + str(y) + " " + str(num)
        p.sendline(payload.encode())
        
        print_arr(board)
        print_arr(INDEX_ELE)
        print(INDEX)

    elif b'AI move' in recv:
        AI = list(map(int, p.recvline().strip().split(b' ')))
        board[AI[0]][AI[1]] = AI[2]
        delete(AI[1], AI[0], AI[2])
        
        
        print_arr(board)
        print_arr(INDEX_ELE)
        print(INDEX)
    # pause()

p.interactive()