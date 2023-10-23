import json
import itertools


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
                weekAvail.append(int(day * 100))
            availToAdd.append(weekAvail)
        result[team] = availToAdd
    print(result)


def printPerms():
    teams = ["t1", "t2", "t3", "t4", "t5", "t6"]

    # Generate all possible permutations of the teams
    team_permutations = list(itertools.permutations(teams, 2))

    # Create a list to store the schedules
    schedules = []

    # Iterate through the permutations and create schedules
    for i in range(len(teams) - 1):
        round_schedule = []
        for j in range(len(team_permutations)):
            round_schedule.append(team_permutations[j])
            if len(round_schedule) == len(teams) // 2:
                schedules.append(round_schedule)
                round_schedule = []
            team_permutations = [team_permutations[-1]] + team_permutations[:-1]

    # Display the schedules
    for idx, schedule in enumerate(schedules):
        print(f"Schedule {idx + 1}:")
        for match in schedule:
            print(f"{match[0]} vs {match[1]}")
        print()


def main():
    printPerms()


if __name__ == "__main__":
    main()
