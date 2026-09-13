from sklearn.ensemble import IsolationForest

class MLDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05)

    def train(self, X):
        self.model.fit(X)

    def predict(self, X):
        return self.model.predict(X)  # -1 anomaly, 1 normal
