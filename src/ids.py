from collections import deque
from src.feature_extractor import extract
from src.rule_engine import check

class IDS:
    def __init__(self, model, config):
        self.window = deque(maxlen=config["window_size"])
        self.model = model
        self.config = config

    def process(self, msg):
        self.window.append(msg)

        if len(self.window) < 5:
            return None

        features = extract(self.window)

        r = check(self.window)
        m = self.model.predict(features)

        # Fusion logic (advanced)
        if r == 1 and m == -1:
            return 1   # strong attack
        elif r == 1 or m == -1:
            return 1   # probable attack
        return 0