from models.pairing import *


class Solution:
    def __init__(self, weeks: int, pairingsPerWeek: int):
        self.weeks = weeks
        self.pairingsPerWeek = pairingsPerWeek
        self.teamsPlayingInWeek = {}
        self.pairings = []
        for i in range(weeks):
            self.teamsPlayingInWeek[i] = set()
            self.pairings.append(set())
        self.score = 0
        self.numPairings = 0
        self.pairingsNeeded = weeks * (weeks + 1) / 2

    def getWeeks(self):
        return self.weeks

    def getPairingsPerWeek(self):
        return self.pairingsPerWeek

    def getTeamsPlayingInWeek(self, week):
        return self.teamsPlayingInWeek[week]

    def addTeamToWeek(self, teamName, week):
        self.teamsPlayingInWeek[week].add(teamName)

    def removeTeamFromWeek(self, teamName, week):
        self.teamsPlayingInWeek[week].remove(teamName)

    def getScore(self):
        return self.score

    def getPairings(self):
        return self.pairings

    def getNumPairings(self):
        return self.numPairings

    def changeScore(self, scoreDelta: int):
        self.score += scoreDelta

    def isValidPairing(self, pairing: Pairing, week) -> bool:
        return pairing.getTeams().isdisjoint(self.getTeamsPlayingInWeek(week))

    def addPairing(self, pairing: Pairing, week) -> None:
        self.addTeamToWeek(pairing.getTeam1Name(), week)
        self.addTeamToWeek(pairing.getTeam2Name(), week)
        self.pairings[week].add(pairing)
        self.numPairings += 1
        self.changeScore(pairing.getWeekScores()[week])

    def removePairing(self, pairing: Pairing, week) -> None:
        self.removeTeamFromWeek(pairing.getTeam1Name(), week)
        self.removeTeamFromWeek(pairing.getTeam2Name(), week)
        self.pairings[week].remove(pairing)
        self.numPairings -= 1
        self.changeScore(-pairing.getWeekScores()[week])

    def isFinished(self):
        return self.getNumPairings() == self.pairingsNeeded
