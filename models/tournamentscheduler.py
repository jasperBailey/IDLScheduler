from models.team import Team


class TournamentScheduler:
    def __init__(self, teamsAvailabilities: list):
        self.teamsAvailabilities = teamsAvailabilities
        self.pairings = None

    def createPairings(self):
        # Returns:
        #
        # list [frozenset, list] - a list where the first element of each entry is
        #   a frozenset containing the name of both teams involved in the pairing
        #   and the second element of each entry is a list of boolean values indicating
        #   whether that matchup can take place on that week

        numTeams = len(self.getTeams())
        numWeeks = numTeams - 1
        # teamData = [list(teamData.keys()), list(teamData.values())]

        pairingsData = []

        # create list of possible matchups and list of matchup availabilities
        # in each time period (week)
        for team1 in range(numTeams):
            for team2 in range(team1, numTeams):
                if team1 == team2:
                    continue

                matchupData = frozenset([teamData[0][team1], teamData[0][team2]])
                # matchupData = [frozenset([teamData[0][team1], teamData[0][team2]]), []]

                # for week in range(numWeeks):
                #     isWeekPossible = False

                #     for day in range(7):
                #         if (
                #             float(teamData[1][team1][week][day])
                #             + float(teamData[1][team2][week][day])
                #             == 10
                #         ):
                #             isWeekPossible = True
                #             break

                #     matchupData[1].append(isWeekPossible)

                pairingsData.append(matchupData)

        # order matchups by number of possible weeks
        pairingsData.sort(key=lambda e: e[1].count(True))
        return pairingsData
