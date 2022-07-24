from pwn import *
import random
r = remote('114.203.209.119', 9001)
context.log_level='debug'

board = [[0]*9 for _ in range(9)]
index = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (5, 2), (4, 2), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (4, 3), (4, 4)]
numfill = []
# index = [(x, y)for x in range(9)for y in range(9)]
index.reverse()
# print(index)

def print_board(board):
    for row in board:
        s = ''.join(str(x) for x in row)
        print(s.replace('0','.'))


def move():
    random.shuffle(index)
    for k in index:
            x, y = k[0], k[1]
            if(board[x][y] != 0):
                continue
            nums = [i for i in range(1, 10)]
            while nums != []:
                least = nums[0]
                for i in nums:
                    if(numfill.count(least) < numfill.count(i)):
                        least = i
                num = least
    # nums = [i for i in range(1, 10)]
    # random.shuffle(nums)
    # for num in nums:
        # for k in index:
        #     x, y = k[0], k[1]
        #     if(board[x][y] != 0):
        #         continue
                col = [board[x][j] for j in range(9)]
                row = [board[i][y] for i in range(9)]
                if col.count(num) == 0:
                    if row.count(num) == 0:
                        subgrid = [board[m][n] for m in range(3*(x // 3), 3*(x // 3)+3) for n in range(3*(y // 3), 3*(y // 3)+3)]
                        if subgrid.count(num) == 0:
                            board[x][y] = num
                            numfill.append(num)
                            index.remove((x, y))
                            print(index)
                            return x, y, num
                nums.remove(num)
    return index[0][0], index[0][1], random.randint(1, 9)

r.sendlineafter('> ', b'GOD_HGK_GOD')
if r.recvline()[:8] != b'Good job':
    r.sendlineafter(b'> ', str(2))
    r.sendlineafter(b'Do you want to see a board for each moves?(T/F) > ', b'T')
trycnt = 0
while True:
    # pause()
    try:
        trycnt += 1
        # sleep(0.5)
        recv = r.recvuntil(b'> ')
        print(recv)
        if  b'Your turn > ' in recv:
            x, y, num = move()
            pay = str(x) + " " + str(y) + " " + str(num)
            r.sendline(pay.encode())
            
        elif b'AI move' in recv:
            recv_arr = list(map(int, r.recvline().strip().split(b' ')))
            index.remove((recv_arr[0],recv_arr[1]))
            board[recv_arr[0]][recv_arr[1]] = recv_arr[2]
        else:
            sleep(1)
            board = [[0]*9 for _ in range(9)]
            # if(trycnt % 3 == 0):
            index = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (5, 2), (4, 2), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (4, 3), (4, 4)]
            # if(trycnt % 3 == 1):
            #     index = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (5, 2), (4, 2), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (4, 3), (4, 4)]
            index.reverse()
            # if(trycnt % 3 == 2):
            #     index = [(x, y)for x in range(9)for y in range(9)]
            #     random.shuffle(index)
                
            numfill = []
            
            r.sendline(str(2))
            r.sendlineafter(b'Do you want to see a board for each moves?(T/F) > ', b'T')
            continue
    except ValueError:
        pass
        # print(index)
        