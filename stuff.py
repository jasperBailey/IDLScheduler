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


def main():
    subData()


if __name__ == "__main__":
    main()
