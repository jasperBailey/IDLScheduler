import csv

teamData = [[], []]
numTeams = 8
numWeeks = numTeams - 1

with open("data.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile)

    for row in spamreader:
        teamData[0].append(row[0])

        weekData = []

        for i in range(numWeeks):
            weekData.append(row[7 * i + 1 : 7 * i + 8])

        teamData[1].append(weekData)


pairingsData = []

# create list of possible matchups and list of matchup availabilities
# in each time period (week)
for team1 in range(numTeams):
    for team2 in range(team1, numTeams):
        if team1 == team2:
            continue

        matchupData = [frozenset([teamData[0][team1], teamData[0][team2]]), []]

        for week in range(numWeeks):
            isWeekPossible = False

            for day in range(7):
                if (
                    float(teamData[1][team1][week][day])
                    + float(teamData[1][team2][week][day])
                    == 10
                ):
                    isWeekPossible = True
                    break

            matchupData[1].append(isWeekPossible)

        pairingsData.append(matchupData)

# order matchups by number of possible weeks
pairingsData.sort(key=lambda e: e[1].count(True))
print(pairingsData)


def fillScheduleDFS(curSolution=None, depth=0):
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

    # set empty solution if just starting
    if curSolution == None:
        curSolution = []
        # create an empty set to hold pairings for the week
        for i in range(numWeeks):
            curSolution.append(set())

    pairingToPlace = pairingsData[depth]

    for i in range(numWeeks):
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
                nextSol = fillScheduleDFS(curSolution, depth + 1)
                if nextSol != None:
                    return nextSol
                else:
                    # if the next iteration couldn't find a valid solution,
                    # remove the last pairing and continue trying to place
                    # on subsequent weeks
                    curSolution[i].remove(pairingToPlace[0])
    print("cannot place pairing:", pairingToPlace, "at depth", depth)
    print("current solution:", curSolution)


print(fillScheduleDFS())
