import json


def main():
    teamData = readJsonFile("data.json")["teamAvailabilities"]
    pairingsData = createPairings(teamData)
    print(pairingsData)
    # print(fillScheduleDFS(pairingsData, len(teamData)))
    # print(fillScheduleBF(pairingsData, len(teamData)))


def readJsonFile(filePath):
    # Parameters:
    #
    # filePath: string - a string indicating the file to be read
    #
    # Returns:
    #
    # dict - containing the result of parsing the file as json

    with open(filePath) as jsonFile:
        return json.load(jsonFile)


def createPairings(teamData):
    # Parameters:
    #
    # teamData: dict {string: list[]} - teamData[teamName][x][y] gives
    #   teamName's availability on day y of week x (0 indexed)
    #
    # Returns:
    #
    # list [frozenset, list] - a list where the first element of each entry is
    #   a frozenset containing the name of both teams involved in the pairing
    #   and the second element of each entry is a list of boolean values indicating
    #   whether that matchup can take place on that week

    numTeams = len(teamData)
    numWeeks = numTeams - 1
    teamData = [list(teamData.keys()), list(teamData.values())]

    pairingsData = []

    # create list of possible matchups and list of matchup availabilities
    # in each time period (week)
    for team1 in range(numTeams):
        for team2 in range(team1, numTeams):
            if team1 == team2:
                continue

            matchupData = [frozenset([teamData[0][team1], teamData[0][team2]]), []]

            for week in range(numWeeks):
                bestDayValue = 0
                bestDay = 0

                for day in range(7):
                    dayValue = float(teamData[1][team1][week][day]) + float(
                        teamData[1][team2][week][day]
                    )
                    if dayValue > bestDayValue:
                        bestDayValue = dayValue
                        bestDay = day

                matchupData[1].append([bestDayValue, bestDay])

            pairingsData.append(matchupData)
    return pairingsData


def fillScheduleDFS(pairingsData, numTeams, curSolution=None, depth=0):
    # Parameters:
    #
    # curSolution: List | None - the current progress on the curSolution, as
    #     a list of sets, with curSolution[x] giving the set of pairings on week x
    #
    # depth: int - the recursion depth, equal to the number of pairings
    #     placed in curSolution
    #
    # Returns:
    #
    # List | None - The full schedule, if there is one, or None otherwise

    # create empty solution if just starting
    if curSolution == None:
        curSolution = []
        # create an empty set to hold pairings for the week
        for i in range(numTeams - 1):
            curSolution.append(set())

    pairingToPlace = pairingsData[depth]

    for i in range(numTeams - 1):
        # check if the pairing can happen in that week
        if not pairingToPlace[1][i]:
            continue

        # check if neither team already has a match that week
        bothTeamsFree = True
        for pairing in curSolution[i]:
            if not pairing.isdisjoint(pairingToPlace[0]):
                bothTeamsFree = False
                break

        if bothTeamsFree:
            curSolution[i].add(pairingToPlace[0])

            # check if solution is now finished
            solutionFinished = True
            for week in curSolution:
                if len(week) != numTeams / 2:
                    solutionFinished = False
                    break

            if solutionFinished:
                return curSolution
            else:
                nextSol = fillScheduleDFS(
                    pairingsData, numTeams, curSolution, depth + 1
                )
                if nextSol != None:
                    return nextSol
                else:
                    # if the next iteration couldn't find a valid solution,
                    # remove the last pairing and continue trying to place
                    # on subsequent weeks
                    curSolution[i].remove(pairingToPlace[0])
    print("cannot place pairing:", pairingToPlace, "at depth", depth)
    print("current solution:", curSolution)


def fillScheduleBF(pairingsData, numTeams):
    pass


if __name__ == "__main__":
    main()
