from models.onefactoriser import OneFactoriser
from itertools import permutations
from models.pairing import Pairing


class TournamentScheduler:
    def __init__(self, teamsAvailabilities: dict):
        self.library = {}
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
        self.oneFactorScores = self.calcOneFactorScores()

    def getOneFactorScores(self):
        return dict(self.oneFactorScores)

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

    def calcOneFactorScores(self):
        oneFactorMap = {}
        for oneFactor in self.onefactoriser.getAllOneFactors():
            weekScores = []
            for i in self._rangeNumWeeks:
                weekScores.append(0)
            for match in oneFactor:
                tMatch = tuple(match)
                for i in self._rangeNumWeeks:
                    weekScores[i] += self.pairings[tMatch[0]][
                        tMatch[1]
                    ].getWeekScores()[i]
            oneFactorMap[oneFactor] = weekScores
        return oneFactorMap

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

    def cbs1F(self, onefactorisation, weeksRemaining):
        try:
            return self.library[frozenset(weeksRemaining)][frozenset(onefactorisation)]
        except:
            pass

        localBestScore = 10000

        for oneFactor in onefactorisation:
            for weekNum in weeksRemaining:
                if len(weeksRemaining) == 1:
                    return (
                        {weekNum: oneFactor},
                        self.oneFactorScores[oneFactor][weekNum],
                    )

                weeksRemaining.remove(weekNum)
                onefactorisation.remove(oneFactor)

                (currentSol, currentScore) = self.cbs1F(
                    onefactorisation, weeksRemaining
                )

                currentSol[weekNum] = oneFactor
                currentScore += self.oneFactorScores[oneFactor][weekNum]

                if currentScore < localBestScore:
                    localBestScore = currentScore
                    localBestSol = currentSol

                weeksRemaining.add(weekNum)
                onefactorisation.add(oneFactor)

        try:
            self.library[frozenset(weeksRemaining)][frozenset(onefactorisation)] = (
                localBestSol,
                localBestScore,
            )
        except:
            self.library[frozenset(weeksRemaining)] = {}
            self.library[frozenset(weeksRemaining)][frozenset(onefactorisation)] = (
                localBestSol,
                localBestScore,
            )

        return (localBestSol, localBestScore)

    def calcBestSchedule(self):
        i = 0
        for onefactorisation in self.onefactoriser.oneFactorisations():
            (nextSol, nextSolScore) = self.cbs1F(
                set(onefactorisation), {0, 1, 2, 3, 4, 5, 6}
            )

            if nextSolScore < self.getBestSolScore():
                print(i)
                self.setBestSol(nextSol)
                self.setBestSolScore(nextSolScore)
            i += 1

        return (self.getBestSol(), self.getBestSolScore())

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
