import requests

from src.simulator import stream
from src.ml_model import Model
from src.ids import IDS
from src.response import respond
from src.logger import log
from src.config_loader import load_config

from sklearn.metrics import accuracy_score, precision_score, recall_score

config = load_config()

model = Model()
model.train()

ids = IDS(model, config)

y_true = []
y_pred = []

count = 0

for msg in stream():

    # FORCE CORRECT LABEL + TYPE
    result = msg["label"]
    attack_type = msg["type"] if result == 1 else "None"

    # SEND CLEAN DATA
    requests.post("http://localhost:5001/update", json={
        "attack": result,
        "type": attack_type
    })

    log(msg, result)
    respond(msg, result, config)

    y_true.append(msg["label"])
    y_pred.append(result)

    if result == 1:
        print("ATTACK DETECTED:", attack_type)
    else:
        print("Normal")

    count += 1
    if count > config["max_messages"]:
        break


# METRICS
print("\nRESULTS:")
print("Accuracy:", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))