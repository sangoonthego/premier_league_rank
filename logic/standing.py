from collections import defaultdict

def create_standings(team_aliases):
    standings = {}
    for team in team_aliases.values():
        standings[team]= {
            "P": 0,   
            "W": 0,   
            "D": 0,   
            "L": 0,   
            "GF": 0,  
            "GA": 0,  
            "GD": 0,  
            "Pts": 0
        }
    return standings

def update_standings(standings, home, away, home_goals, away_goals):
    standings[home]["P"] += 1
    standings[away]["P"] += 1
    standings[home]["GF"] += home_goals
    standings[home]["GA"] += away_goals
    standings[away]["GF"] += away_goals
    standings[away]["GA"] += home_goals

    if home_goals > away_goals:
        standings[home]["W"] += 1
        standings[home]["Pts"] += 3
        standings[away]["L"] += 1
    elif away_goals > home_goals:
        standings[away]["W"] += 1
        standings[away]["Pts"] += 3
        standings[home]["L"] += 1
    else:
        standings[home]["D"] += 1
        standings[home]["Pts"] += 1
        standings[away]["D"] += 1
        standings[away]["Pts"] += 1

    standings[home]["GD"] = standings[home]["GF"] - standings[home]["GA"]
    standings[away]["GD"] = standings[away]["GF"] - standings[away]["GA"]

