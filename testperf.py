import timeit
import json
from models.tournamentscheduler import TournamentScheduler


def benchBF():
    with open("data.json") as f:
        data = json.load(f)
    scheduler = TournamentScheduler(data["teamAvailabilities"])
    scheduler.createPairings()
    print(timeit.Timer(scheduler.getScheduleBF).timeit(number=1))


def benchIsDisjoint():
    with open("data6.json") as f:
        data = json.load(f)
    scheduler = TournamentScheduler(data["teamAvailabilities"])
    scheduler.createPairings()
    print(timeit.Timer(scheduler.getScheduleBFDummy).timeit(number=100))


def benchTypeConversion():
    def TC():
        hi = frozenset(["str1", "str2"])
        for i in range(1000000):
            hi2 = frozenset(hi)

    print(timeit.Timer(TC).timeit(number=100))


def benchReadListVsTuple():
    def RL():
        hi = ["str1", "str2", "str2", "str2", "str2", "str2", "str2"]
        for i in range(1000000):
            hi2 = hi[5]

    def RL():
        hi = ("str1", "str2", "str2", "str2", "str2", "str2", "str2")
        for i in range(1000000):
            hi2 = hi[5]

    print("list: ", timeit.Timer(RL).timeit(number=100))
    print("tuple: ", timeit.Timer(RL).timeit(number=100))


def main():
    benchReadListVsTuple()


if __name__ == "__main__":
    main()
