def create_round_robin(team_aliases):
    teams = list(team_aliases.values())
    if len(teams) % 2 != 0:
        teams.append("Ronaldo")

    n = len(teams)
    rounds = []
    for round_idx in range(n - 1):
        round_matches = []
        for i in range(n // 2):
            home = teams[i]
            away = teams[n - 1 - i]
            if round_idx % 2 == 0:
                round_matches.append((home, away))
            else:
                round_matches.append((away, home))
        teams = [teams[0]] + [teams[-1]] + teams[1:-1]
        rounds.append(round_matches)
    return rounds

def create_full_schedule(team_aliases):
    first_leg = create_round_robin(team_aliases)
    second_leg = [[(away, home) for home, away in round] for round in first_leg]
    return first_leg + second_leg
