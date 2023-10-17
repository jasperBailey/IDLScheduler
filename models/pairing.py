class Pairing:
    def __init__(
        self, team1Name: str, team1Avail: list, team2Name: str, team2Avail: list
    ) -> None:
        self.team1Name = team1Name
        self.team1Avail = team1Avail
        self.team2Name = team2Name
        self.team2Avail = team2Avail

        if len(team1Avail) != len(team2Avail):
            raise ValueError(
                "cannot create pairing where teams have different availability profiles"
            )

        self._numWeeks = len(team1Avail)
        [self.weekScores, self.bestDays] = self.calcWeekScores()

    def getTeam1Name(self):
        return self.team1Name

    def getTeam1Avail(self):
        return self.team1Avail

    def getTeam2Name(self):
        return self.team2Name

    def getTeam2Avail(self):
        return self.team2Avail

    def getWeekScores(self):
        return self.weekScores

    def getBestDays(self):
        return self.bestDays

    def calcBestDays(self) -> list:
        result = [frozenset([self.team1Name, self.team2Name]), []]
        for week in range(self._numWeeks):
            bestDayValue = 0
            bestDay = 0

            for day in range(7):
                dayValue = float(self.team1Avail[week][day]) + float(
                    self.team2Avail[week][day]
                )
                if dayValue > bestDayValue:
                    bestDayValue = dayValue
                    bestDay = day

            result[1].append([bestDayValue, bestDay])

        return result
