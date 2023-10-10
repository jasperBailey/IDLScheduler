import json

f = open("data.json")
data = json.load(f)
print(data)


newData = {}
for team in data.keys():
    teamData = json.loads(data[team])
    weekSeparatedData = []
    for week in range(len(teamData) // 7):
        weekSeparatedData.append(teamData[week * 7 : (week * 7) + 7])
    newData[team] = weekSeparatedData

print(newData)

f.close()
