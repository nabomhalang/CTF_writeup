v34 = 0x24C5BCA11E1850DB
v33 = 0x3B809DECD4534499

def rev(x, y, z): # v33 = v31 - ((v32 + ((v32 << 8) ^ (v32 >> 10))) ^ 0xE1F569BFF12757Ci64)
    return (x + (((y + ((((y << 8) & 0xffffffffffffffff ) ^ ( (y >> 10)& 0xffffffffffffffff ))) & 0xffffffffffffffff ) ^ z) & 0xffffffffffffffff)) & 0xffffffffffffffff

v32 = rev(v34, v33, 0xDEADBEEFDEADBEEF)
v31 = rev(v33, v32, 0xE1F569BFF12757C)
v30 = rev(v32, v31, 0x4C2E96AC3D21B58C)
v29 = rev(v31, v30, 0x996F32897B55704A)
v28 = rev(v30, v29, 0x792EF6AA5B15346B)
v27 = rev(v29, v28, 0xE6AFCE66B9892B08)
v26 = rev(v28, v27, 0xE6AFCE66B9892B08)
v25 = rev(v27, v26, 0xE0D01B42A49C96C5)
v24 = rev(v26, v25, 0x13B02E64D77CA9E7) 
v22 = rev(v24, v23, 0x8131062135F0A084)
v21 = rev(v23, v22, 0xAE31661F53E41F63)
v20 = rev(v22, v21, 0xAE31661F53E41F63)
v19 = rev(v21, v20, 0xDDA2FDCB7448D5F0)
v18 = rev(v20, v19, 0x1BB23DDBB2581600)
v17 = rev(v19, v18, 0x68F2D9B8F08BD0BE)
v16 = rev(v18, v17, 0x48B29DD9D04B94DF)
v15 = rev(v17, v16, 0xB63375962EBF8B7C)
v14 = rev(v16, v15, 0xB63375962EBF8B7C)
v13 = rev(v15, v14, 0xB053C27219D2F739)
v12 = rev(v14, v13, 0xE333D5944CB30A5B)
v11 = rev(v13, v12, 0x307471718AE6C519)
v10 = rev(v12, v11, 0x50B4AD50AB2700F8)
v9 = rev(v11, v10, 0x7DB50D4EC91A7FD7)
v8 = rev(v10, v9, 0x7DB50D4EC91A7FD7)
v7 = rev(v9, v8, 0xAD26A4FAE97F3664)
v6 = rev(v8, v7, 0xEB35E50B278E7674)
v5 = rev(v7, v6, 0x387680E865C23132)
v4 = rev(v6, v5, 0x183645094581F553)
v3 = rev(v5, v4, 0x85B71CC5A3F5EBF0)

print(v3)

flag = [0] * 2
flag[0] = rev(v4, v3, 0x85B71CC5A3F5EBF0)
flag[1] = rev(v3, flag[0], 0x7FD769A18F0957AD)

print([hex(i) for i in flag])

# easyy_inverse_op