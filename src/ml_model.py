import pandas as pd
from sklearn.ensemble import IsolationForest

class Model:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)

    def train(self):
        df = pd.read_csv("final_dataset.csv")

        df = df[df["label"] == 0]

        X = df[["id", "data", "time"]]
        self.model.fit(X)

    def predict(self, x):
        import numpy as np
        return self.model.predict(np.array(x).reshape(1, -1))[0]