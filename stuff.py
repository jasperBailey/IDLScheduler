import csv

teamNames = []
teamData = []

with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        teamNames.append(row[0])
        weekData = []
        for i in range(7):
            weekData.append(row[7*i+1:7*i+8])
        teamData.append(weekData)

possibleMatches = []
matchupTable = []

for team1 in range(8):
    for team2 in range(team1, 8):
        if team1 == team2:
            continue
        matchupData = []
        matchupTable.append( {
            teamNames[team1],
            teamNames[team2]
        })
        for week in range(7):
            isWeekPossible = False
            for day in range(7):
                if float(teamData[team1][week][day]) + float(teamData[team2][week][day]) == 10:
                    isWeekPossible = True
                    break
            matchupData.append(isWeekPossible)
        possibleMatches.append(matchupData)
    


print(matchupTable)
print(possibleMatches)