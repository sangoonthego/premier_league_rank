import numpy as np
from data.team_power import team_power

BIG_SIX = {"MUN", "MCI", "LIV", "ARS", "CHE", "TOT"}

def simulate_match(home, away):
    home_power = team_power.get(home, 75)
    away_power = team_power.get(away, 75)

    home_goal_avg = (home_power / 100) * 3
    away_goal_avg = (away_power / 100) * 3

    if home_power < 75 and away == "MUN":
        home_power += 10
    if away_power < 75 and home == "MUN":
        away_power += 5

    if home == "BHA" and away in BIG_SIX:
        home_power += 10
    if away == "BHA" and home in BIG_SIX:
        away_power += 10
        
    if home == "TOT" and away == "MCI":
        home_power += 10
    if away == "TOT" and home == "MCI":
        away_power += 10
            
    home_goals = np.random.poisson(home_goal_avg)
    away_goals = np.random.poisson(away_goal_avg)

    return min(home_goals, 12), min(away_goals, 12)

#  from utils.goal_generator import generate_goals

# BIG_SIX = ("MUN", "MCI", "LIV", "ARS", "CHE", "TOT")

# goal_prob_big = {
#     0: 0.01, 1: 0.05, 2: 0.15, 3: 0.2, 4: 0.2, 5: 0.15,
#     6: 0.1, 7: 0.06, 8: 0.04, 9: 0.02, 10: 0.01, 11: 0.005, 12: 0.005
# }

# goal_prob_small = {
#     0: 0.25, 1: 0.25, 2: 0.2, 3: 0.1, 4: 0.07, 5: 0.04,
#     6: 0.03, 7: 0.02, 8: 0.015, 9: 0.005, 10: 0.002, 11: 0.001, 12: 0.001
# }

# def simulate_match(home, away):
#     home_prob = goal_prob_big if home in BIG_SIX else goal_prob_small
#     away_prob = goal_prob_big if away in BIG_SIX else goal_prob_small

#     home_goals = generate_goals(home_prob)
#     away_goals = generate_goals(away_prob)

#     return home_goals, away_goals
