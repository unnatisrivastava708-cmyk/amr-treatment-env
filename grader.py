def grade(state):
    score = state["patient_condition"]

    # penalize high resistance
    if state["resistance_level"] > 0.7:
        score -= 0.2

    return round(max(0, min(1, score)), 2)