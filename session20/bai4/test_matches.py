def determine_winner(match):
    if match["status"] == "Pending":
        return "Not Started"

    if match["score_a"] > match["score_b"]:
        return match["team_a"]

    if match["score_b"] > match["score_a"]:
        return match["team_b"]

    return "Draw"


match_1 = {
    "team_a": "T1",
    "team_b": "GenG",
    "score_a": 2,
    "score_b": 0,
    "status": "Completed"
}

match_2 = {
    "team_a": "T1",
    "team_b": "GenG",
    "score_a": 1,
    "score_b": 1,
    "status": "Completed"
}

match_3 = {
    "team_a": "T1",
    "team_b": "GenG",
    "score_a": 0,
    "score_b": 0,
    "status": "Pending"
}

print(determine_winner(match_1))
print(determine_winner(match_2))
print(determine_winner(match_3))