import unittest
from models.onefactoriser import OneFactoriser


class TestOneFactoriser(unittest.TestCase):
    def setUp(self):
        self.onefact = OneFactoriser(8)

    @unittest.skip
    def testCreateEdges(self):
        print(self.onefact.getEdges())

    @unittest.skip
    def testInitialSol(self):
        print(self.onefact.getInitialSol())

    def testGetOneFactors(self):
        print(self.onefact.getOneFactors())
