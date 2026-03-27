def fuse(rule_result, ml_result):
    if rule_result == 1 and ml_result == -1:
        return 1
    if rule_result == 1 or ml_result == -1:
        return 1
    return 0