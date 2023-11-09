import json
from itertools import *


def subData():
    with open("data/datainv.json") as f:
        data = json.load(f)
    tA = data["teamAvailabilities"]
    result = {}
    for team in tA:
        availToAdd = []
        for week in tA[team]:
            weekAvail = []
            for day in week:
                weekAvail.append(int(day / 10))
            availToAdd.append(weekAvail)
        result[team] = availToAdd
    print(result)


def hasNoRepeatedTeam(week):
    teams = []
    for pairing in week:
        for team in pairing:
            if team not in teams:
                teams.append(team)
            else:
                return False
    return True


def removePairings(removeFrom, pairingsToRem):
    result = removeFrom[:]
    for week in removeFrom:
        for pairing in pairingsToRem:
            if pairing in week:
                result.remove(week)
                break

    return result


def printPerms():
    teams = [1, 2, 3, 4, 5, 6, 7, 8]

    pairings = list(combinations(teams, 2))

    possibleWeeks = list(filter(hasNoRepeatedTeam, combinations(pairings, 4)))
    for i in range(len(possibleWeeks)):
        possibleWeeks[i] = set(possibleWeeks[i])
    solution = [possibleWeeks[0]]
    possibleWeeks = removePairings(possibleWeeks, solution[0])
    pWeeks = []
    for i in range(6):
        pWeeks.append(possibleWeeks[i * 10 : (i * 10) + 9])

    solGen = solutionGenerator(solution, pWeeks)

    print(next(solGen))


def solutionGenerator(initialSol, possibleWeeks):
    solution = initialSol[:]
    for weekset in possibleWeeks:
        for week in weekset:
            for solweek in solution:
                if not week.isdisjoint(solweek):
                    break
            else:
                solution.append(week)
    yield solution


def main():
    subData()


if __name__ == "__main__":
    main()
