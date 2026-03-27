import pandas as pd

def parse_line(line):
    try:
        parts = line.strip().split()
        timestamp = float(parts[0].strip("()"))

        can_part = parts[2]
        can_id, data = can_part.split('#')

        return {
            "time": timestamp,
            "id": int(can_id, 16),
            "data": int(data, 16)
        }
    except:
        return None


def process_file(path, label, attack_type):
    rows = []
    with open(path, "r") as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                parsed["label"] = label
                parsed["type"] = attack_type
                rows.append(parsed)
    return pd.DataFrame(rows)


def load_vehicle_data(base_path):
    normal = process_file(base_path + "training.log", 0, "Normal")

    dos = process_file(base_path + "dosattack.log", 1, "DoS")
    replay = process_file(base_path + "replay.log", 1, "Replay")
    fuzz1 = process_file(base_path + "fuzzing_canid.log", 1, "Fuzzing")
    fuzz2 = process_file(base_path + "fuzzing_payload.log", 1, "Fuzzing")

    return pd.concat([normal, dos, replay, fuzz1, fuzz2])


clio = load_vehicle_data("data/RenaultClio/")
astra = load_vehicle_data("data/OpelAstra/")

df = pd.concat([clio, astra])

# BALANCE DATA
normal = df[df["label"] == 0].sample(10000)
attack = df[df["label"] == 1].sample(10000)

df = pd.concat([normal, attack])

df = df.sample(frac=1).reset_index(drop=True)

df.to_csv("final_dataset.csv", index=False)

print("Dataset ready:", df.shape)