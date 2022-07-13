from z3 import *

LEN = 40
arr = [BitVec('x%d'%i, 32) for i in range(LEN)] + [0] * 4

table = [0x00534DC4, 0x00660725, 0x00331C8E, 0x00A46325, 0x0097B543, 0x00D84417, 0x007E4A2B, 0x00339B72, 0x0077BEBF, 0x00DCC234, 0x0000F5C0, 0x00130F6A, 0x00CD1118, 0x00DE4FFA, 0x00A6464C, 0x00D61295, 0x00799010, 0x00A418F9, 0x00F190A0, 0x001F4032,0,0,0,0,0]

s = Solver()
    
for i in range(20):
    result = 0xFFFFFF
    for v1 in range(3):
        result ^= arr[i * 2 + v1]
        for _ in range(8):
            v4 = result >> 1
            v4 ^= (result & 1) * 0xFCC0E1
            result = v4 & 0xFFFFFF
    s.add(table[i] == result)

for i in range(len(arr)):
    s.add(arr[i] == arr[i] & 0xff)

print(s.check())

m = s.model()
for i in range(len(arr) - 4):
    print(chr(int(str(m.evaluate(arr[i])))), end='')