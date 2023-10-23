from models.pairing import *


class Solution:
    def __init__(self, weeks: int, pairingsPerWeek: int):
        self.numWeeks = weeks
        self.pairingsPerWeek = pairingsPerWeek
        self.teamsPlayingInWeek = []
        for i in range(weeks):
            self.teamsPlayingInWeek.append([])
        self.score = 0
        self.numPairings = 0
        self.pairingsNeeded = weeks * (weeks + 1) // 2

    def getNumWeeks(self):
        return self.numWeeks

    def getPairingsPerWeek(self):
        return self.pairingsPerWeek

    def getTeamsPlayingInWeek(self, week):
        return self.teamsPlayingInWeek[week]

    def addTeamToWeek(self, teamName, week):
        self.teamsPlayingInWeek[week].append(teamName)

    def removeTeamFromWeek(self, teamName, week):
        self.teamsPlayingInWeek[week].remove(teamName)

    def getScore(self):
        return self.score

    def getNumPairings(self):
        return self.numPairings

    def changeScore(self, scoreDelta: int):
        self.score += scoreDelta

    def isValidPairing(self, pairing: Pairing, week) -> bool:
        return pairing.getTeams().isdisjoint(self.getTeamsPlayingInWeek(week))

    def addPairing(self, pairing: Pairing, week) -> None:
        self.addTeamToWeek(pairing.getTeam1Name(), week)
        self.addTeamToWeek(pairing.getTeam2Name(), week)
        self.numPairings += 1
        self.changeScore(pairing.getWeekScores()[week])

    def removePairing(self, pairing: Pairing, week) -> None:
        self.removeTeamFromWeek(pairing.getTeam1Name(), week)
        self.removeTeamFromWeek(pairing.getTeam2Name(), week)
        self.numPairings -= 1
        self.changeScore(-pairing.getWeekScores()[week])

    def isFinished(self):
        return self.getNumPairings() == self.pairingsNeeded
