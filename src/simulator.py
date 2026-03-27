import pandas as pd
import time

def stream():
    df = pd.read_csv("final_dataset.csv")

    for _, row in df.iterrows():
        yield {
            "id": row["id"],
            "data": row["data"],
            "time": row["time"],
            "label": row["label"],
            "type": row["type"]
        }
        time.sleep(0.1)