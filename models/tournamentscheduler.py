from models.onefactoriser import OneFactoriser
from itertools import permutations
from models.pairing import Pairing


class TournamentScheduler:
    def __init__(self, teamsAvailabilities: dict):
        self.teams = list(teamsAvailabilities)
        self.teamsAvailabilities = [teamsAvailabilities[name] for name in self.teams]
        self._numTeams = len(list(self.teamsAvailabilities))
        self._numWeeks = self._numTeams - 1
        self._pairingsPerWeek = self._numTeams // 2
        self.bestSol = None
        self.bestSolScore = 10000
        self.onefactoriser = OneFactoriser(self._numTeams)
        self._rangeNumWeeks = range(self._numWeeks)
        self.pairings = self.createPairings()

    def getBestSol(self):
        return self.bestSol

    def setBestSol(self, value):
        self.bestSol = value

    def getBestSolScore(self):
        return self.bestSolScore

    def setBestSolScore(self, value):
        self.bestSolScore = value

    def getTeamsAvailabilities(self) -> list:
        return self.teamsAvailabilities

    def getTeams(self):
        return self.teams

        # for schedule in permutations(onefactorisation):
        #     # solScore = self.calcSolScore(schedule)
        #     score = 0
        #     for i in self._rangeNumWeeks:
        #         for match in schedule[i]:
        #             score += self.pairings[match[0]][match[1]].getWeekScores()[i]
        #         if score >= self.bestSolScore:
        #             break
        #     else:
        #         self.setBestSolScore(score)
        #         self.setBestSol(schedule)

    def cbs1F(
        self,
        onefactorisation,
        currentSol,
        currentScore,
        library,
        weeksRemaining,
        oneFactorsRemaining,
        depth=0,
    ):
        if (
            frozenset(weeksRemaining) not in library.keys()
        ):
            library[frozenset(weeksRemaining)] = {}
        if (
            frozenset(oneFactorsRemaining)
            in library[frozenset(weeksRemaining)].keys()
        ):
            print("hi")
            return library[weeksRemaining][oneFactorsRemaining]

        for oneFactorNum in oneFactorsRemaining:
            for weekNum in weeksRemaining:
                # currentScore += onefactorisation[oneFactorNum]
                # FUCK NEED WEEK SCORES FOR EACH 1FACTOR, CALC FOR EACH ONEFACTOR
                # BEFOREHAND AND MAKE DICT WITH ONEFACTOR FROZENSET AS KEYS

                if currentScore >= self.bestSolScore:
                    # currentScore -= onefactorisation[oneFactorNum]
                    continue

                weeksRemaining.remove(weekNum)
                oneFactorsRemaining.remove(oneFactorNum)

                if depth == 6:  # finished
                    currentSol[weekNum] = onefactorisation[oneFactorNum]

                    if #BLAHG
                    library[frozenset(weeksRemaining)][
                        frozenset[oneFactorsRemaining]
                    ] = currentScore

                    currentSol[weekNum] = None  # might be able to remove this
                    # currentScore -= onefactorisation[oneFactorNum]

                self.cbs1F(
                    onefactorisation,
                    currentSol,
                    currentScore,
                    library,
                    weeksRemaining,
                    oneFactorsRemaining,
                    depth + 1,
                )

                weeksRemaining.add(weekNum)
                oneFactorsRemaining.add(oneFactorNum)

    def calcBestSchedule(self):
        for onefactorisation in self.onefactoriser.oneFactorisations():
            self.cbs1F(
                onefactorisation,
                {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None},
                0,
                {},
                {0, 1, 2, 3, 4, 5, 6},
                {0, 1, 2, 3, 4, 5, 6},
            )
        return [self.getBestSol(), self.getBestSolScore()]

    def createPairings(self) -> list:
        # Returns:
        #
        # list [frozenset, list] - a list where the first element of each entry is
        #   a frozenset containing the name of both teams involved in the pairing
        #   and the second element of each entry is a list of boolean values indicating
        #   whether that matchup can take place on that week

        teamsAvail = self.getTeamsAvailabilities()
        teamNames = self.getTeams()
        pairings = {}

        # create list of possible matchups and list of matchup availabilities
        # in each time period (week)
        for i in range(self._numTeams):
            pairings[i] = {}
            for j in range(i, self._numTeams):
                if i == j:
                    continue
                team1 = teamNames[i]
                team2 = teamNames[j]
                pairings[i][j] = Pairing.fromTeamAvailabilities(
                    team1, team2, teamsAvail[i], teamsAvail[j]
                )

        return pairings
