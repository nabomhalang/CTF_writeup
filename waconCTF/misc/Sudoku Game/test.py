insert = [(x, y) for x in range(9)for y in range(9)]

def spiral(R, C):
    grid = [[None] * C for _ in range(R)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dirIdx = 0
    r, c = 0, 0
    
    for i in range(1, R*C+1):
        grid[r][c] = i
        nr, nc = r+directions[dirIdx][0], c+directions[dirIdx][1]
        if nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] is not None:
            dirIdx = (dirIdx + 1) % 4
            nr, nc = r + directions[dirIdx][0], c + directions[dirIdx][1]
        r, c = nr, nc
    return grid




s = spiral(9, 9)
flag = list()
for row in s:
    flag.append(row)
    
answer = sum(flag, [])

# print(answer)

for row in flag:
    print(row)
    
for x in range(9):
    for y in range(9):
        insert[flag[x][y] - 1] = (x, y)
print(insert)