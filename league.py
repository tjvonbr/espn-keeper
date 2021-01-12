from pick_values import pick_values
from players import roster

num_teams = 12
draft_rounds = 16
pick = 10
draft = [[i for i in range(1, num_teams + 1)]]
picks = []
keepers = []
keepers_values = []

# creates the draft based on how many rounds and teams in league
for i in range(2, draft_rounds + 1):
    round = []
    for i in draft[-1]:
        round.append(i + num_teams)
    draft.append(round)

# creates a list of an owner's absolute picks based on previous year's standing
for i in range(len(draft)):
    if i % 2 == 0:
        picks.append(draft[i][pick - 1])
    else:
        picks.append(draft[i][num_teams-pick])

# print(picks)

draft_2019 = [
    {
        "name": "Christian McCaffrey",
        "round": 1,
        "pick": 5
    },
    {
        "name": "Adam Thielen",
        "round": 2,
        "pick": 20
    },
    {
        "name": "Chris Godwin",
        "round": 3,
        "pick": 29
    },
    {
        "name": "J.K. Dobbins",
        "round": 4,
        "pick": 44
    },
    {
        "name": "DeVante Parker",
        "round": 4,
        "pick": 53
    },
]

for player in draft_2019:
    total_player = {}
    cur_player = (player["name"])
    round_drafted = player["round"]
    next_years_draft = picks[round_drafted - 1]
    next_years_value = pick_values[next_years_draft]["value"]
    projection = roster[cur_player]["projected_points"]

    # Prints the players project and expected value of his draft position
    total_player["player"] = cur_player
    total_player["draft_round"] = round_drafted
    total_player["projection"] = projection
    total_player["exp_value"] = projection - next_years_value
    keepers.append(total_player)

print(keepers)

keepers.sort(key=lambda keeper: keeper["exp_value"], reverse=True)
print(keepers[:2])
