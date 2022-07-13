from z3 import *

s = Solver()

f = "SUNRIN{FA?KEFLAG}"

inp = [BitVec('x%d'%i,8) for i in range(len(f))]

for i in range(len(f)):
    s.add(inp[i] == ord(f[i]))

print(s.check())

m = s.model()
for i in range(len(inp)):
    print(chr(int(str(m.evaluate(inp[i])))),end='')