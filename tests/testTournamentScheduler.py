import unittest
from models.tournamentscheduler import *


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.sampleTournament = TournamentScheduler()

    def testGetTeams(self):
        self.assertEqual(self.sampleTournament.getTeams(), [])
