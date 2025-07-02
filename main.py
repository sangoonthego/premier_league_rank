from data.team_data import teams_info
from logic.scheduler import create_full_schedule
from logic.printer import print_matchweek, print_standings
from logic.standing import create_standings, update_standings
from datetime import datetime, timedelta

alias_map = {team: alias for team, (alias, _) in teams_info.items()} 
alias_to_full = {alias: team for team, (alias, _) in teams_info.items()}
alias_to_stadium = {alias: stadium for team, (alias, stadium) in teams_info.items()}

schedule = create_full_schedule(alias_map)
start_date = datetime(2025, 8, 10)
time_options = ["18:30", "20:00", "21:00", "22:00", "02:00"]

standings = create_standings(alias_map)

for week, matches in enumerate(schedule, 1):
    match_date = start_date + timedelta(days=(week - 1) * 7)
    print_matchweek(
        week=week,
        matches=matches,
        alias_to_full=alias_to_full,
        alias_to_stadium=alias_to_stadium,
        match_date=match_date,
        time_options=time_options,
        standings=standings,
        update_standings=update_standings
    )
    print_standings(standings, alias_to_full)