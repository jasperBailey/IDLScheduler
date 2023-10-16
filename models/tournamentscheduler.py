class TournamentScheduler:
    def __init__(self, teamsAvailabilities: dict):
        self.teamsAvailabilities = teamsAvailabilities
        self._numTeams = len(list(self.teamsAvailabilities))
        self._numWeeks = self._numTeams - 1
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
        isFinalLayer = False
        bestSol = None
        bestSolScore = 0
        # create empty solution if just starting
        if curSolution == None:
            curSolution = []
            # create an empty list to hold pairings for the week
            for i in range(self._numWeeks):
                curSolution.append([])

        pairingToPlace = self.getPairings()[depth]

        for i in range(self._numWeeks):
            bothTeamsFree = True
            for pairing in curSolution[i]:
                if not pairing[0].isdisjoint(pairingToPlace[0]):
                    bothTeamsFree = False
                    break
            if not bothTeamsFree:
                continue

            curSolution[i].append(pairingToPlace)

            if self.isSolutionFinished(curSolution):
                isFinalLayer = True
                return curSolution

            nextSol = self.getScheduleBF(curSolution, depth + 1)
            nextSolScore = self.evaluateSolution(nextSol)
            if nextSolScore > bestSolScore:
                bestSol = nextSol
                bestSolScore = nextSolScore

            # remove the last pairing and continue trying to place
            # on subsequent weeks
            curSolution[i].remove(pairingToPlace)
        return bestSol

    def isSolutionFinished(self, solution):
        for week in solution:
            if len(week) != self._numTeams / 2:
                return False
        return True

    # returns the overall score of a solution (higher is better)
    @staticmethod
    def evaluateSolution(solution):
        if solution == None:
            return 0
        solutionScore = 0
        for week in range(len(solution)):
            for pairing in solution[week]:
                solutionScore += pairing[1][week][0]
        return solutionScore

    # def getScheduleDFS(self, curSolution=None, depth=0, minScore=):
    #     # Parameters:
    #     #
    #     # curSolution: List | None - the current progress on the curSolution, as
    #     #     a list of sets, with curSolution[x] giving the set of pairings on week x
    #     #
    #     # depth: int - the recursion depth, equal to the number of pairings
    #     #     placed in curSolution
    #     #
    #     # Returns:
    #     #
    #     # List | None - The full schedule, if there is one, or None otherwise

    #     # create empty solution if just starting
    #     if curSolution == None:
    #         curSolution = []
    #         # create an empty set to hold pairings for the week
    #         for i in range(self._numWeeks):
    #             curSolution.append(set())

    #     pairingToPlace = self.getPairings()[depth]

    #     for i in range(self._numWeeks):
    #         # check if the pairing can happen in that week
    #         if not pairingToPlace[1][i]:
    #             continue

    #         # check if neither team already has a match that week
    #         bothTeamsFree = True
    #         for pairing in curSolution[i]:
    #             if not pairing.isdisjoint(pairingToPlace[0]):
    #                 bothTeamsFree = False
    #                 break

    #         if bothTeamsFree:
    #             curSolution[i].add(pairingToPlace[0])

    #             # check if solution is now finished
    #             solutionFinished = True
    #             for week in curSolution:
    #                 if len(week) != self._numTeams / 2:
    #                     solutionFinished = False
    #                     break

    #             if solutionFinished:
    #                 return curSolution
    #             else:
    #                 nextSol = self.fillScheduleDFS(curSolution, depth + 1)
    #                 if nextSol != None:
    #                     return nextSol
    #                 else:
    #                     # if the next iteration couldn't find a valid solution,
    #                     # remove the last pairing and continue trying to place
    #                     # on subsequent weeks
    #                     curSolution[i].remove(pairingToPlace[0])
    #     print("cannot place pairing:", pairingToPlace, "at depth", depth)
    #     print("current solution:", curSolution)
