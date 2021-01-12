class DraftGenerator:
    def __init__(self, rounds, pick, teams): 
        self.rounds = rounds
        self.pick = pick
        self.teams = teams
        self.picks = []
        self.draft = [[i for i in range(1, self.teams + 1)]]

    def generateDraft(self):
        # outer loop generates a new round
        for i in range(2, self.rounds + 1):
            round = []
            for i in self.draft[-1]:
                round.append(i + self.teams)
            self.draft.append(round)

        # inner loop determines absolute picks in each round
        for j in range(len(self.draft)):
            if j % 2 == 0:
                self.picks.append(self.draft[j][self.pick - 1])
            else:
                self.picks.append(self.draft[j][self.teams - self.pick])

    def printPicks(self):
        print(self.picks)

d = DraftGenerator(16, 10, 12)
d.generateDraft()
d.printPicks()