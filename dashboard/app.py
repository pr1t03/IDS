from flask import Flask, jsonify, render_template, request
import time

app = Flask(__name__)

data_store = {
    "attacks": 0,
    "total": 0,
    "status": "Running",
    "current_attack": 0,
    "attack_type": "None",
    "last_update": time.time(),
    "last_attack_time": 0,
    "history": [],   # NEW
    "type_count": {"DoS": 0, "Replay": 0, "Fuzzing": 0}  # NEW
}

ATTACK_COOLDOWN = 2  # seconds

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    if time.time() - data_store["last_update"] > 2:
        data_store["status"] = "Stopped"
    else:
        data_store["status"] = "Running"

    return jsonify(data_store)

@app.route("/update", methods=["POST"])
def update():
    content = request.json

    data_store["total"] += 1
    data_store["last_update"] = time.time()

    attack = content["attack"]
    attack_type = content["type"]

    if attack == 1:
        data_store["current_attack"] = 1
        data_store["attack_type"] = attack_type

        # COUNT WITH COOLDOWN
        if time.time() - data_store["last_attack_time"] > ATTACK_COOLDOWN:
            data_store["attacks"] += 1
            data_store["last_attack_time"] = time.time()

            # ADD TO HISTORY
            entry = {
                "time": time.strftime("%H:%M:%S"),
                "type": attack_type
            }
            data_store["history"].insert(0, entry)

            # KEEP ONLY LAST 10
            data_store["history"] = data_store["history"][:10]

            # COUNT TYPES
            if attack_type in data_store["type_count"]:
                data_store["type_count"][attack_type] += 1

    else:
        data_store["current_attack"] = 0
        data_store["attack_type"] = "None"

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)