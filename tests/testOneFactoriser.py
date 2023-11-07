import unittest
from models.onefactoriser import OneFactoriser


class TestOneFactoriser(unittest.TestCase):
    def setUp(self):
        self.onefact = OneFactoriser(8)
        self.onefact.oneFactorisations()

    @unittest.skip
    def testCreateEdges(self):
        print(f"edges: {self.onefact.getEdges()}")

    @unittest.skip
    def testInitialSol(self):
        print(self.onefact.getInitialSol())

    @unittest.skip
    def testGetOneFactors(self):
        print(self.onefact.getOneFactors())

    @unittest.skip
    def testGetOneFactorisations(self):
        print(self.onefact.getOneFactorisations()[0])

    @unittest.skip
    def testGetW1(self):
        for thingy in self.onefact.getW1():
            print(thingy)
        # print(self.onefact.getOneFactorisations()[0])

    # @unittest.skip
    def testGetOneFactorisationsAsLists(self):
        print(self.onefact.getOneFactorisationsAsLists()[0])
