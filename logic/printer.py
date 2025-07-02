from datetime import timedelta
import random
from logic.simulator import simulate_match
from logic.standing import update_standings

def print_matchweek(week, matches, alias_to_full, alias_to_stadium, match_date, time_options, standings, update_standings):
    print(f"\nPremier League - Match Week {week}")
    for home, away in matches:
        home_full = alias_to_full[home]
        away_full = alias_to_full[away]
        stadium = alias_to_stadium[home]
        time = random.choice(time_options)
        date_str = match_date.strftime("%d/%m/%Y")
        home_goals, away_goals = simulate_match(home, away)

        print(f"{home_full} {home_goals} - {away_goals} {away_full} - {date_str} - {time} - {stadium}")

        update_standings(standings, home, away, home_goals, away_goals)

def print_standings(standings, alias_to_full):
    print("\n STANDING BOARD")
    header = f"{'Pos':<4}{'Team':<25}{'P':>3}{'W':>3}{'D':>3}{'L':>3}{'GF':>4}{'GA':>4}{'GD':>4}{'Pts':>5}"
    print(header)
    print("-" * len(header))

    sorted_teams = sorted(standings.items(), key=lambda x: (-x[1]["Pts"], -x[1]["GD"], -x[1]["GF"]))

    for i, (team, stats) in enumerate(sorted_teams, 1):
        name = alias_to_full[team]
        print(f"{i:<4}{name:<25}{stats['P']:>3}{stats['W']:>3}{stats['D']:>3}{stats['L']:>3}"
            f"{stats['GF']:>4}{stats['GA']:>4}{stats['GD']:>4}{stats['Pts']:>5}")
