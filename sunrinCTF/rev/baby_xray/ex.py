from z3 import *
from ctypes import *

libc = CDLL("msvcrt")

def sub_401100(v7):
    v14 = libc.rand() % 24;
    v12 = *a1;
    if ( v14 & 0x20 )
    {
        LODWORD(v12) = *(a1 + 1);
        HIDWORD(v12) = *a1;
    }
    if ( v14 & 0x1F )
    {
        v1 = v12;
        LODWORD(v12) = __PAIR__(v12, HIDWORD(v12)) << (v14 & 0x1F) >> 32;
        HIDWORD(v12) = (v1 << (v14 & 0x1F)) >> 32;
    }
    *a1 = v12;
    v13 = rand() % 24;
    v11 = *a1;
    if ( v13 & 0x20 )
    {
        LODWORD(v11) = *(a1 + 1);
        HIDWORD(v11) = *a1;
    }
    if ( v13 & 0x1F )
    {
        v2 = v11;
        LODWORD(v11) = v11 >> (v13 & 0x1F);
        HIDWORD(v11) = __PAIR__(v2, HIDWORD(v2)) >> (v13 & 0x1F);
    }
    *a1 = v11;
    v3 = *(a1 + 1);
    *a1 ^= 0x63u;
    *(a1 + 1) = v3;
    *a1 += 99i64;
    *a1 -= 101i64;
    v4 = *(a1 + 1);
    *a1 ^= 0x32u;
    *(a1 + 1) = v4;
    *a1 += 48i64;
    *a1 -= 50i64;
    v5 = *(a1 + 1);
    *a1 ^= 0x31u;
    *(a1 + 1) = v5;
    *a1 += 123i64;
    *a1 -= 88i64;
    v6 = *(a1 + 1);
    *a1 ^= 0x2Du;
    *(a1 + 1) = v6;
    *a1 += 82i64;
    *a1 -= 97i64;
    v7 = *(a1 + 1);
    *a1 ^= 0x79u;
    *(a1 + 1) = v7;
    *a1 += 45i64;
    *a1 -= 66i64;
    *a1 += 101i64;
    v8 = *(a1 + 1);
    *a1 += 97;
    *(a1 + 1) = v8;
    *a1 -= 109i64;
    v10 = *a1 - 125;
    result = v10;
    *a1 = v10;
    return result;


table_list = [0xCC584D71, 0x598E188D, 0x8D94D461, 0xD8C99999, 0x8C472C8B, 0x66CCACA6, 0x64373702, 0x32623738, 0xC0CCCA1E, 0x9598D4D4, 0x62363102, 0x33656138, 0x4CCC4D25, 0x9918D94C, 0xCD595922, 0x598C4C58]

arr = [BitVec("x_%d" %i, 8 * 4) for i in range(64)]

for i in range(0, 16, 2):
    sub_401100(v7[i])
    