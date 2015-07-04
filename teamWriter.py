__author__ = 'Edward'
import csv
import os
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

def writeDir(resultDir, league):
    if not os.path.exists(resultDir + league):
        os.makedirs(resultDir + league)

def writer(filename, data):
    with open(filename,"wb") as fp:
        a = csv.writer(fp,delimiter=',')
        a.writerows(data)

def writeTableMaker(filename, league):
    printed = stringify(league)
    writer(filename, printed)

