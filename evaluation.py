import time

def evaluate(model, X):
    start = time.time()
    preds = model.predict(X)
    end = time.time()

    latency = end - start

    return {
        "predictions": preds,
        "latency": latency
    }
