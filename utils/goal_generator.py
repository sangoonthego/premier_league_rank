import random

def generate_goals(prob_dict):
    goals = list(prob_dict.keys())
    weights = list(prob_dict.values())
    return random.choices(goals, weights=weights)[0]