import unittest
import json
from models.pairing import *
from models.solution import *


class TestSolution(unittest.TestCase):
    def setUp(self):
        with open("data/data.json") as f:
            data = json.load(f)
        keys = list(data["teamAvailabilities"].keys())
        team1 = keys[0]
        team2 = keys[1]
        team1Avail = data["teamAvailabilities"][team1]
        team2Avail = data["teamAvailabilities"][team2]
        self.pairing = Pairing.fromTeamAvailabilities(
            team1, team2, team1Avail, team2Avail
        )
        numTeams = len(keys)
        self.solution = Solution(numTeams - 1, numTeams // 2)

    def testAddScore(self):
        self.assertEqual(0, self.solution.getScore())
        self.solution.changeScore(2)
        self.assertEqual(2, self.solution.getScore())

    def testRemoveScore(self):
        self.assertEqual(0, self.solution.getScore())
        self.solution.changeScore(-2)
        self.assertEqual(-2, self.solution.getScore())

    def testAddPairing(self):
        self.assertEqual(0, self.solution.getNumPairings())
        self.solution.addPairing(self.pairing, 0)
        self.assertEqual(1, self.solution.getNumPairings())

    def testRemovePairing(self):
        self.solution.addPairing(self.pairing, 0)
        self.assertEqual(1, self.solution.getNumPairings())
        self.solution.removePairing(self.pairing, 0)
        self.assertEqual(0, self.solution.getNumPairings())

    def testTeamsPlayingInWeek(self):
        self.assertEqual([], self.solution.getTeamsPlayingInWeek(0))
        self.solution.addPairing(self.pairing, 0)
        self.assertEqual(["SEMMEL", "HIGHPIE"], self.solution.getTeamsPlayingInWeek(0))
        self.solution.removePairing(self.pairing, 0)
        self.assertEqual([], self.solution.getTeamsPlayingInWeek(0))
