def _generate():
    linux = b""

    for filename in "machine-id", "boot_id":
        try:
            with open(filename, "rb") as f:
                value = f.readline().strip()
        except OSError:
            continue

        if value:
            linux += value
            break

    try:
        with open("cgroup", "rb") as f:
            linux += f.readline().strip().rpartition(b"/")[2]
    except OSError:
        pass

    if linux:
        return linux

print(_generate())