from models.pairing import Pairing
from models.solution import Solution
import copy


class TournamentScheduler:
    def __init__(self, teamsAvailabilities: dict):
        self.teamsAvailabilities = teamsAvailabilities
        self._numTeams = len(list(self.teamsAvailabilities))
        self._numWeeks = self._numTeams - 1
        self._pairingsPerWeek = self._numTeams // 2
        self.createPairings()
        self.numIters = 0
        self.bestSol = None
        self.bestSolScore = 10000

    def getBestSol(self):
        return self.bestSol

    def setBestSol(self, value):
        self.bestSol = value

    def getBestSolScore(self):
        return self.bestSolScore

    def setBestSolScore(self, value):
        self.bestSolScore = value

    def emptySolution(self) -> Solution:
        return Solution(self._numWeeks, self._pairingsPerWeek)

    def getTeamsAvailabilities(self) -> dict:
        return dict(self.teamsAvailabilities)

    def getPairings(self) -> list:
        return self.pairings[:]

    def createPairings(self) -> list:
        # Returns:
        #
        # list [frozenset, list] - a list where the first element of each entry is
        #   a frozenset containing the name of both teams involved in the pairing
        #   and the second element of each entry is a list of boolean values indicating
        #   whether that matchup can take place on that week

        teamsAvail = self.getTeamsAvailabilities()
        teamNames = list(teamsAvail)
        pairings = []

        # create list of possible matchups and list of matchup availabilities
        # in each time period (week)
        for i in range(self._numTeams):
            for j in range(i, self._numTeams):
                if i == j:
                    continue
                team1 = teamNames[i]
                team2 = teamNames[j]
                pairings.append(
                    Pairing.fromTeamAvailabilities(
                        team1, team2, teamsAvail[team1], teamsAvail[team2]
                    )
                )

        def evalPairingDifficulty(pairing):
            return pairing.getWeekScores().count(0)

        pairings.sort(key=evalPairingDifficulty)

        self.pairings = pairings
        return pairings

    def getScheduleBF(self, curSolution, depth=0):
        self.numIters += 1
        pairingToPlace = self.getPairings()[depth]
        for i in pairingToPlace.getBestWeeks():
            if not curSolution.isValidPairing(pairingToPlace, i):
                continue

            curSolution.addPairing(pairingToPlace, i)

            if curSolution.getScore() >= self.getBestSolScore():
                curSolution.removePairing(pairingToPlace, i)
                continue

            if curSolution.isFinished():
                solToReturn = []
                self.setBestSolScore(curSolution.getScore())
                for week in range(self._numWeeks):
                    solToReturn.append(curSolution.getTeamsPlayingInWeek(week)[:])
                self.setBestSol(solToReturn)
                curSolution.removePairing(pairingToPlace, i)
                break

            self.getScheduleBF(curSolution, depth + 1)

            curSolution.removePairing(pairingToPlace, i)

        if depth == 0:
            print(self.numIters)
            return [self.bestSol, self.bestSolScore]
