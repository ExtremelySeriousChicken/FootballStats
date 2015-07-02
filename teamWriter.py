__author__ = 'Edward'
import csv
#this file will write csv file

# Requires : The league
# Modifies : the league
# Effects  : Take the league data and then make it
#            Into an array of strings so that it can be written
#            into the csv file
def stringify(league):

    leagueArray = list()

    infoArray = ["Team Name","Wins","Draws","Loses","Points","Goals For","Goals Conceded"]

    leagueArray.append(infoArray)

    #now iterate through the league
    for team in league:
        newArray = list()
        newArray.append(team.teamName)
        newArray.append(team.win)
        newArray.append(team.draw)
        newArray.append(team.lose)
        newArray.append(team.points)
        newArray.append(team.goalFor)
        newArray.append(team.goalConceded)
        leagueArray.append(newArray)

    return leagueArray

def writeLeague(filename, league):

    printed = stringify(league)

    with open("trying.csv","wb") as fp:
        a = csv.writer(fp,delimiter=',')
        a.writerows(printed)