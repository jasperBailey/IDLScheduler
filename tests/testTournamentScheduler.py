import unittest
import json
from models.tournamentscheduler import *


class TestScheduler(unittest.TestCase):
    def setUp(self):
        with open("data/datainv.json") as f:
            self.data = json.load(f)
        self.numTeams = len(self.data["teamAvailabilities"])
        self.scheduler = TournamentScheduler(self.data["teamAvailabilities"])

    @unittest.skip
    def testBruteForce(self):
        self.scheduler.createPairings()
        [result, score] = self.scheduler.getScheduleBF(
            curSolution=self.scheduler.emptySolution()
        )
        print(result)
        self.assertEqual(score, 400)

    def testGetTeams(self):
        self.assertEqual(
            self.scheduler.getTeamsAvailabilities(), self.data["teamAvailabilities"]
        )
