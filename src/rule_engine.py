def check(window):
    ids = [m["id"] for m in window]

    if len(ids) > 15:
        return 1

    if max(ids) > 2000:
        return 1

    return 0