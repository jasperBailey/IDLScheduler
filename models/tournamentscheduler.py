import copy


class TournamentScheduler:
    def __init__(self, teamsAvailabilities: dict):
        self.teamsAvailabilities = teamsAvailabilities
        self._numTeams = len(list(self.teamsAvailabilities))
        self._numWeeks = self._numTeams - 1
        self._pairingsPerWeek = self._numTeams / 2
        self.pairings = None

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

        teamsAvailabilities = self.getTeamsAvailabilities()
        teamNames = list(teamsAvailabilities)
        numTeams = len(teamNames)
        numWeeks = numTeams - 1
        pairingsData = []

        # create list of possible matchups and list of matchup availabilities
        # in each time period (week)
        for team1 in range(numTeams):
            for team2 in range(team1, numTeams):
                if team1 == team2:
                    continue

                matchupData = [frozenset([teamNames[team1], teamNames[team2]]), []]
                for week in range(numWeeks):
                    bestDayValue = 0
                    bestDay = 0

                    for day in range(7):
                        dayValue = float(
                            teamsAvailabilities[teamNames[team1]][week][day]
                        ) + float(teamsAvailabilities[teamNames[team2]][week][day])
                        if dayValue > bestDayValue:
                            bestDayValue = dayValue
                            bestDay = day

                    matchupData[1].append([bestDayValue, bestDay])

                pairingsData.append(matchupData)
        self.pairings = pairingsData
        return pairingsData

    def getScheduleBF(self, curSolution=None, depth=0):
        bestSol = None
        bestSolScore = 0
        # create empty solution if just starting
        if curSolution == None:
            curSolution = []
            # create an empty list to hold pairings for the week
            for i in range(self._numWeeks):
                curSolution.append([])

        pairingToPlace = self.getPairings()[depth]
        pairingTeams = pairingToPlace[0]

        for week in curSolution:
            bothTeamsFree = True
            for pairing in week:
                if not pairing[0].isdisjoint(pairingTeams):
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

            nextSol = self.getScheduleBF(curSolution, depth + 1)
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
                solutionScore += pairing[1][week][0]
        return solutionScore
