import json
from itertools import *
import matplotlib.pyplot as plt
import numpy as np


def plot():
    n_bins = 20

    fig, axs = plt.subplots(1, 1, sharey=True, tight_layout=True)

    y = [
        1434,
        1674,
        433,
        148,
        616,
        4,
        21,
        4680,
        593,
        2611,
        195,
        1,
        170,
        717,
        23,
        270,
        1379,
        996,
        886,
        452,
        217,
        1183,
        22,
        294,
        8,
        5933,
        773,
        423,
        890,
        4863,
        102,
        629,
        2630,
        503,
        0,
        2829,
        4,
        692,
        58,
        4591,
        1114,
        583,
        1150,
        5,
        3,
        3352,
        34,
        61,
        56,
        1641,
    ]
    # We can set the number of bins with the *bins* keyword argument.
    axs.hist(y, bins=n_bins)

    plt.show()


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
    plot()


if __name__ == "__main__":
    main()
