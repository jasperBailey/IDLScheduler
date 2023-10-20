import unittest
import json
from models.tournamentscheduler import *
from models.pairing import *
from models.solution import *


class TestScheduler(unittest.TestCase):
    def setUp(self):
        with open("data6.json") as f:
            self.data = json.load(f)
        self.numTeams = len(self.data["teamAvailabilities"])
        self.scheduler = TournamentScheduler(self.data["teamAvailabilities"])

    # @unittest.skip
    def testBruteForce(self):
        self.scheduler.createPairings()
        [result, score] = self.scheduler.getScheduleBF()
        self.assertEqual(score, 146.0)

    @unittest.skip
    def testOldBruteForce(self):
        self.scheduler.createPairings()
        result = self.scheduler.getScheduleBFOld()
        score = self.scheduler.evaluateSolution(result)
        self.assertEqual(score, 146.0)

    def testGetPairings(self):
        self.assertEqual(
            len(self.scheduler.getPairings()), (self.numTeams / 2) * (self.numTeams - 1)
        )

    def testGetTeams(self):
        self.assertEqual(
            self.scheduler.getTeamsAvailabilities(), self.data["teamAvailabilities"]
        )
