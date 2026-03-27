import datetime

def log(msg, result):
    with open("log.txt", "a") as f:
        time = datetime.datetime.now()
        f.write(f"{time} | {msg} | {result}\n")