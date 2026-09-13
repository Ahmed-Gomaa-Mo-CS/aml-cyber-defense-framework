from data_loader import load_data
from preprocessing import preprocess
from layer2_ml import MLDetector
from escalation import escalation_logic

# 1. Load dataset (path)
df = load_data("data.csv")

# 2. Preprocess
X = preprocess(df)

# 3. Train ML model
ml = MLDetector()
ml.train(X)

# 4. Run system
results = []

for i in range(len(X)):
    row = X.iloc[i]

    rule_result = "UNKNOWN"
    if row.mean() > 1000:
        rule_result = "MALICIOUS"

    ml_result = ml.predict([row])[0]

    decision = escalation_logic(rule_result, ml_result)
    results.append(decision)

print("Sample output:", results[:20])
