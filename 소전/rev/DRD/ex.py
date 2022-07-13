qword_201080 = list()
for i in range(256):
    v3 = i
    for j in range(8):
        if ( v3 & 1 ):
            v3 = (v3 >> 1) ^ 0xC96C5795D7870F42
        else:
            v3 = v3 >> 1
    qword_201080.append(v3)


table = [0xB7C6299B74EAE139, 0x7E31ABA88285E864, 0x138A22BE0C2BA396, 0x5CC16A4C389C9524, 0xF2A3353DE1622B9E]

def find(x):
    for a in qword_201080:
        if a >> 56 == x >> 56:
            return a

for i in table:
    key = []
    v3 = i
    for j in range(8):
        found = find(v3)
        v3 ^= found
        v3 <<= 8
        # print("0x%016x"%(found))    
        key.append(found)
    key.reverse()

    v3 = 0xFFFFFFFFFFFFFFFF
    
    for j in key:
        idx = qword_201080.index(j)
        input_in = (v3 ^ idx) & 0xff
        
        v3 = (v3 >> 8) ^ j
        print(chr(input_in), end='')
        