import unittest
import json
from models.tournamentscheduler import *


class TestFunctions(unittest.TestCase):
    def setUp(self):
        with open("data.json") as f:
            data = json.load(f)
        self.scheduler = TournamentScheduler(data["teamAvailabilities"])

    def testBruteForce(self):
        self.scheduler.createPairings()
        self.assertEqual(self.scheduler.getScheduleBF(), [[], [], [], [], [], [], []])

    # def testDepthFirstSearch(self):
    #     self.scheduler.createPairings()
    #     self.assertEqual(self.scheduler.getScheduleDFS(), [])

    def testCreatePairings(self):
        self.scheduler.createPairings()
        self.assertEqual(
            self.scheduler.getPairings(),
            [
                [
                    frozenset({"HIGHPIE", "SEMMEL"}),
                    [
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [9.0, 0],
                        [9.0, 3],
                        [10.0, 3],
                    ],
                ],
                [
                    frozenset({"HUNTEDDO", "SEMMEL"}),
                    [
                        [10.0, 4],
                        [9.0, 0],
                        [10.0, 4],
                        [10.0, 0],
                        [10.0, 0],
                        [10.0, 4],
                        [10.0, 0],
                    ],
                ],
                [
                    frozenset({"CUSTARD", "SEMMEL"}),
                    [
                        [10.0, 6],
                        [9.0, 0],
                        [10.0, 4],
                        [10.0, 0],
                        [9.0, 0],
                        [9.0, 4],
                        [10.0, 4],
                    ],
                ],
                [
                    frozenset({"DEATH_ROE", "SEMMEL"}),
                    [
                        [10.0, 3],
                        [8.0, 3],
                        [9.1, 4],
                        [10.0, 3],
                        [9.1, 3],
                        [10.0, 4],
                        [10.0, 3],
                    ],
                ],
                [
                    frozenset({"PARAKEATS", "SEMMEL"}),
                    [
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [9.1, 3],
                        [9.1, 4],
                        [10.0, 3],
                    ],
                ],
                [
                    frozenset({"HANA", "SEMMEL"}),
                    [
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [9.1, 3],
                        [9.0, 3],
                        [10.0, 3],
                    ],
                ],
                [
                    frozenset({"MAT{MELON}", "SEMMEL"}),
                    [
                        [10.0, 3],
                        [9.0, 3],
                        [9.0, 3],
                        [10.0, 0],
                        [9.1, 3],
                        [9.0, 4],
                        [10.0, 3],
                    ],
                ],
                [
                    frozenset({"HUNTEDDO", "HIGHPIE"}),
                    [
                        [9.0, 0],
                        [10.0, 2],
                        [9.0, 2],
                        [10.0, 2],
                        [9.0, 0],
                        [10.0, 0],
                        [9.0, 2],
                    ],
                ],
                [
                    frozenset({"CUSTARD", "HIGHPIE"}),
                    [
                        [9.0, 2],
                        [9.0, 2],
                        [9.0, 2],
                        [10.0, 6],
                        [8.0, 0],
                        [9.0, 0],
                        [9.0, 2],
                    ],
                ],
                [
                    frozenset({"DEATH_ROE", "HIGHPIE"}),
                    [
                        [10.0, 3],
                        [8.0, 2],
                        [9.0, 3],
                        [10.0, 3],
                        [9.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                    ],
                ],
                [
                    frozenset({"PARAKEATS", "HIGHPIE"}),
                    [
                        [10.0, 2],
                        [10.0, 2],
                        [10.0, 2],
                        [10.0, 3],
                        [9.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                    ],
                ],
                [
                    frozenset({"HANA", "HIGHPIE"}),
                    [
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [9.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                    ],
                ],
                [
                    frozenset({"MAT{MELON}", "HIGHPIE"}),
                    [
                        [10.0, 2],
                        [9.0, 2],
                        [9.0, 2],
                        [10.0, 2],
                        [9.0, 2],
                        [9.0, 2],
                        [10.0, 2],
                    ],
                ],
                [
                    frozenset({"HUNTEDDO", "CUSTARD"}),
                    [
                        [10.0, 6],
                        [10.0, 0],
                        [10.0, 0],
                        [10.0, 0],
                        [9.0, 0],
                        [9.0, 0],
                        [10.0, 4],
                    ],
                ],
                [
                    frozenset({"DEATH_ROE", "HUNTEDDO"}),
                    [
                        [10.0, 4],
                        [8.0, 2],
                        [10.0, 6],
                        [10.0, 4],
                        [10.0, 4],
                        [10.0, 4],
                        [10.0, 4],
                    ],
                ],
                [
                    frozenset({"HUNTEDDO", "PARAKEATS"}),
                    [
                        [10.0, 5],
                        [10.0, 2],
                        [10.0, 5],
                        [10.0, 5],
                        [10.0, 5],
                        [10.0, 5],
                        [10.0, 5],
                    ],
                ],
                [
                    frozenset({"HANA", "HUNTEDDO"}),
                    [
                        [10.0, 4],
                        [9.1, 0],
                        [10.0, 4],
                        [9.1, 2],
                        [10.0, 4],
                        [10.0, 6],
                        [10.0, 4],
                    ],
                ],
                [
                    frozenset({"MAT{MELON}", "HUNTEDDO"}),
                    [
                        [9.0, 0],
                        [9.0, 0],
                        [9.0, 4],
                        [10.0, 0],
                        [10.0, 4],
                        [9.0, 2],
                        [10.0, 4],
                    ],
                ],
                [
                    frozenset({"DEATH_ROE", "CUSTARD"}),
                    [
                        [9.0, 4],
                        [8.0, 4],
                        [10.0, 6],
                        [10.0, 4],
                        [9.0, 4],
                        [9.0, 3],
                        [10.0, 4],
                    ],
                ],
                [
                    frozenset({"CUSTARD", "PARAKEATS"}),
                    [
                        [10.0, 6],
                        [10.0, 5],
                        [10.0, 5],
                        [10.0, 5],
                        [9.0, 5],
                        [9.0, 3],
                        [10.0, 5],
                    ],
                ],
                [
                    frozenset({"HANA", "CUSTARD"}),
                    [
                        [10.0, 6],
                        [9.1, 0],
                        [10.0, 4],
                        [9.0, 3],
                        [9.0, 4],
                        [9.0, 3],
                        [10.0, 4],
                    ],
                ],
                [
                    frozenset({"MAT{MELON}", "CUSTARD"}),
                    [
                        [9.0, 2],
                        [9.0, 0],
                        [9.0, 4],
                        [10.0, 0],
                        [9.0, 2],
                        [8.0, 2],
                        [10.0, 4],
                    ],
                ],
                [
                    frozenset({"DEATH_ROE", "PARAKEATS"}),
                    [
                        [10.0, 3],
                        [8.0, 2],
                        [9.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                    ],
                ],
                [
                    frozenset({"HANA", "DEATH_ROE"}),
                    [
                        [10.0, 3],
                        [8.0, 3],
                        [9.1, 4],
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                    ],
                ],
                [
                    frozenset({"DEATH_ROE", "MAT{MELON}"}),
                    [
                        [10.0, 3],
                        [7.0, 2],
                        [8.1, 4],
                        [10.0, 3],
                        [10.0, 3],
                        [9.0, 3],
                        [10.0, 3],
                    ],
                ],
                [
                    frozenset({"HANA", "PARAKEATS"}),
                    [
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                    ],
                ],
                [
                    frozenset({"MAT{MELON}", "PARAKEATS"}),
                    [
                        [10.0, 1],
                        [9.0, 1],
                        [9.0, 1],
                        [10.0, 1],
                        [10.0, 1],
                        [9.0, 3],
                        [10.0, 3],
                    ],
                ],
                [
                    frozenset({"HANA", "MAT{MELON}"}),
                    [
                        [10.0, 3],
                        [9.0, 3],
                        [9.0, 3],
                        [10.0, 3],
                        [10.0, 3],
                        [9.0, 3],
                        [10.0, 3],
                    ],
                ],
            ],
        )

    def testGetTeams(self):
        self.assertEqual(
            self.scheduler.getTeamsAvailabilities(),
            {
                "SEMMEL": [
                    [4, 4, 3.1, 5, 5, 3, 5],
                    [4, 4, 3.1, 5, 3, 2, 3],
                    [3, 3, 3.1, 5, 5, 3, 4],
                    [5, 4, 3.1, 5, 5, 3, 4],
                    [5, 4, 3.1, 4.1, 3, 2, 3],
                    [3, 3, 3.1, 4, 5, 3, 4],
                    [5, 4, 3.1, 5, 5, 3, 5],
                ],
                "HIGHPIE": [
                    [4, 3, 5, 5, 4, 3, 3],
                    [3, 4, 5, 5, 4, 4, 3],
                    [3, 3, 5, 5, 4, 4, 3],
                    [3, 4, 5, 5, 4, 4, 5],
                    [4, 3, 4, 4, 3, 3, 4],
                    [5, 3.1, 5, 5, 4, 3, 3.1],
                    [3, 4, 5, 5, 4, 3, 4],
                ],
                "HUNTEDDO": [
                    [5, 2, 4, 4, 5, 5, 5],
                    [5, 2, 5, 4, 5, 5, 5],
                    [5, 2, 4, 4, 5, 5, 5],
                    [5, 2, 5, 4, 5, 5, 5],
                    [5, 2, 4, 4, 5, 5, 5],
                    [5, 2, 5, 4, 5, 5, 5],
                    [5, 2, 4, 4, 5, 5, 5],
                ],
                "CUSTARD": [
                    [4, 3, 4, 3, 4, 4, 5],
                    [5, 3, 4, 4, 5, 5, 5],
                    [5, 3, 4, 4, 5, 5, 5],
                    [5, 3, 4, 4, 5, 5, 5],
                    [4, 3, 4, 3, 4, 4, 4],
                    [4, 3, 4, 4, 4, 4, 4],
                    [4, 3, 4, 4, 5, 5, 5],
                ],
                "DEATH_ROE": [
                    [3.1, 1.2, 4.1, 5, 5, 4, 3],
                    [2.1, 2, 3, 3, 3, 2, 3],
                    [1.1, 2.1, 3.1, 4, 4.1, 4, 5],
                    [3.1, 3, 4, 5, 5, 4, 5],
                    [3.1, 3.1, 4, 5, 5, 4, 5],
                    [3.1, 3, 3, 5, 5, 4, 4],
                    [2.1, 4, 4, 5, 5, 4, 5],
                ],
                "PARAKEATS": [
                    [4, 5, 5, 5, 4.1, 5, 5],
                    [4, 5, 5, 5, 4.1, 5, 5],
                    [3.1, 5, 5, 5, 4.1, 5, 0],
                    [3.1, 5, 3.1, 5, 4.1, 5, 5],
                    [3.1, 5, 3.1, 5, 4.1, 5, 5],
                    [3.1, 5, 3.1, 5, 4.1, 5, 5],
                    [3.1, 5, 3.1, 5, 4.1, 5, 5],
                ],
                "HANA": [
                    [4, 4, 4.1, 5, 5, 4, 5],
                    [4.1, 4, 4.1, 5, 4, 4, 4],
                    [3.2, 4, 4.1, 5, 5, 4, 4],
                    [3.2, 4, 4.1, 5, 4, 3.1, 4],
                    [3.2, 4, 4.1, 5, 5, 3.1, 3.1],
                    [2.2, 3, 4.1, 5, 4, 4, 5],
                    [4.1, 4, 4.1, 5, 5, 4, 5],
                ],
                "MAT{MELON}": [
                    [4, 5, 5, 5, 4, 3, 3],
                    [4, 4, 4, 4, 4, 2, 2],
                    [2.1, 4, 4, 4, 4, 4, 3],
                    [5, 5, 5, 5, 5, 3, 3],
                    [4, 5, 5, 5, 5, 3.1, 3.1],
                    [3.1, 3, 4, 4, 4, 2, 2],
                    [2, 4, 5, 5, 5, 4, 4],
                ],
            },
        )
