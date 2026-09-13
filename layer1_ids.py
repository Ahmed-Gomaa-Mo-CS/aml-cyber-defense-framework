def rule_based_detector(row):
    # baseline rules
    if row.mean() > 1000:
        return "MALICIOUS"
    return "UNKNOWN"
