# O(n) time ---> n is the number of competitions/results
# O(k) space ---> k is the number of teams
competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
game_results = [0, 0, 1]


def solve(competitions, game_results):
    scores = {}
    best_team = ""
    best_score = 0

    for i in range(len(game_results)):
        home_team, away_team = competitions[i]

        winning_team = home_team if game_results[i] == 1 else away_team

        if winning_team not in scores:
            scores[winning_team] = 1
        else:
            scores[winning_team] += 1

        if best_score < scores[winning_team]:
            best_score = scores[winning_team]
            best_team = winning_team

    return [best_team, best_score]


result = solve(competitions, game_results)

print(result)
