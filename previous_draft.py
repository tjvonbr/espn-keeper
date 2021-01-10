"""
For testing purposes, team will be limited to my team's
1st 5 draft picks in a 12-team league with 16 rounds.
the league is a .5 PPR ESPN league--should be enough
information for now
"""

from pick_values import pick_values
from players import roster

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

def draftOrder(draft_pick: int, rounds: int, teams: int):
    draft = [[i for i in range(1, teams + 1)]]

    print(draft)

print(draftOrder(10, 16, 12))

def pickTwo(cur_roster, draft_results, projections):
    keepers = []

    for player in cur_roster:
        cur_player = player["name"]
        projection = draft_results[cur_player]["projected_points"]
        expected_points = projections
        print(projection)
        
    
print(pickTwo(draft_2019, roster, pick_values ))