def escalation_logic(rule_result, ml_result):
    if rule_result == "MALICIOUS":
        return "BLOCK"

    if ml_result == -1:
        return "ALERT"

    return "SAFE"
