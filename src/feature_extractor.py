import numpy as np

def extract(window):
    ids = [m["id"] for m in window]
    data = [m["data"] for m in window]
    times = [m["time"] for m in window]

    return [
        np.mean(ids),
        np.mean(data),
        np.mean(np.diff(times)) if len(times) > 1 else 0
    ]