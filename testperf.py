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


def main():
    benchBF()


if __name__ == "__main__":
    main()
