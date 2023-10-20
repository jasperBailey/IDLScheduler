from models.pairing import Pairing
from models.solution import Solution
import copy


class TournamentScheduler:
    def __init__(self, teamsAvailabilities: dict):
        self.teamsAvailabilities = teamsAvailabilities
        self._numTeams = len(list(self.teamsAvailabilities))
        self._numWeeks = self._numTeams - 1
        self._pairingsPerWeek = self._numTeams / 2
        self.createPairings()

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
        self.pairings = pairings
        return pairings

    def getScheduleBF(self, curSolution=None, depth=0):
        bestSol = None
        bestSolScore = 0
        # create empty solution if just starting
        if curSolution == None:
            curSolution = Solution(self._numWeeks, self._pairingsPerWeek)

        pairingToPlace = self.getPairings()[depth]
        for i in range(self._numWeeks):
            # if depth < 1:
            #    print(depth, i)
            if not curSolution.isValidPairing(pairingToPlace, i):
                continue

            curSolution.addPairing(pairingToPlace, i)

            if curSolution.isFinished():
                solToReturn = []
                score = curSolution.getScore()
                for week in curSolution.getPairings():
                    solToReturn.append(set(week))
                curSolution.removePairing(pairingToPlace, i)
                return [solToReturn, score]

            [nextSol, nextSolScore] = self.getScheduleBF(curSolution, depth + 1)

            if nextSolScore > bestSolScore:
                bestSol = nextSol
                bestSolScore = nextSolScore

            # remove the last pairing and continue trying to place
            # on subsequent weeks
            curSolution.removePairing(pairingToPlace, i)

        return [bestSol, bestSolScore]

    def getScheduleBFOld(self, curSolution=None, depth=0):
        bestSol = None
        bestSolScore = 0
        # create empty solution if just starting
        if curSolution == None:
            curSolution = []
            # create an empty list to hold pairings for the week
            for i in range(self._numWeeks):
                curSolution.append([])

        pairingToPlace = self.getPairings()[depth]
        pairingTeams = pairingToPlace.getTeams()
        # i = 0
        for week in curSolution:
            # if depth < 3:
            #     print(depth, i)
            # i += 1
            bothTeamsFree = True
            for pairing in week:
                if not pairing.getTeams().isdisjoint(pairingTeams):
                    bothTeamsFree = False
                    break
            if not bothTeamsFree:
                continue

            week.append(pairingToPlace)

            if self.isSolutionFinished(curSolution):
                solToReturn = []
                for week2 in curSolution:
                    solToReturn.append(week2[:])
                week.remove(pairingToPlace)
                return solToReturn

            nextSol = self.getScheduleBFOld(curSolution, depth + 1)
            nextSolScore = self.evaluateSolution(nextSol)

            if nextSolScore > bestSolScore:
                bestSol = nextSol
                bestSolScore = nextSolScore

            # remove the last pairing and continue trying to place
            # on subsequent weeks
            week.remove(pairingToPlace)

        return bestSol

    def isSolutionFinished(self, solution):
        for week in solution:
            if len(week) != self._pairingsPerWeek:
                return False
        # print(f"solution {solution} is finished")
        return True

    # returns the overall score of a solution (higher is better)
    def evaluateSolution(self, solution):
        if solution == None:
            return 0
        solutionScore = 0
        for week in range(self._numWeeks):
            for pairing in solution[week]:
                solutionScore += pairing.getWeekScores()[week]
        return solutionScore
