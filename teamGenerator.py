__author__ = 'Edward'

from classes import *
from dataProcessor import *

#This file aims to get the data of the teams
def createTeam(data):
    newLeague = list()
    duplicate = 0
    id = 0
    print data
    for team in data:
        #go through each
        print team

        index = isExist(newLeague,team.home)

        if(index == -1):
            newLeague.append(teamProfile(id,team.home))
            id += 1
            duplicate = 0
            print id
        else:
            duplicate += 1

        if(duplicate >= 20):
            break

        for x in newLeague:
            print(str(x.id) + ":" + x.teamName)

    return newLeague


# Requires : the data, which is the list
# Modifies : Nothing
# Effects  : It will find the name of the team in the data
def isExist(data, team):
    if(len(data) == 0):
        return -1
    else:
        index = -1
        for x in range(len(data)):
            if(team == data[x].teamName):
                index = x
        return index

# Requires : The league and the name of the team
# Modifies : Nothing
# Effects  : It will iterate through the league and find the team
#            Return the index of the team

def findIndex(league, team):
    for i in range(len(league)):
        if league[i].teamName == team:
            return i

    return -1
# Requires : The table and the fixtures
# Modifies : the table
# Effects  : go through each of the fixtures and then calculate
#            The statistics of the table
def calculatePts(table,fixtures):
    for game in fixtures:
        #go through each game
        homeIndex = findIndex(table, game.home)
        awayIndex = findIndex(table, game.away)

        if((homeIndex == -1) or (awayIndex == -1)):
            print "There is something wrong with calculate pts!"
            exit(1)

        #now check the scores
        #adding the goal
        table[homeIndex].goalFor += game.h
        table[homeIndex].goalConceded += game.a
        table[awayIndex].goalFor += game.a
        table[awayIndex].goalConceded += game.h

        #if the home team wins
        if (game.h > game.a):
            print "home wins!"
            table[homeIndex].win += 1
            table[homeIndex].points += 3
            table[awayIndex].lose += 1
        elif (game.h < game.a):
            print "away wins!"
            table[awayIndex].win += 1
            table[awayIndex].points += 3
            table[homeIndex].lose += 1
        else:
            table[homeIndex].draw += 1
            table[homeIndex].points += 1
            table[awayIndex].draw += 1
            table[awayIndex].points += 1

    for x in table:
        print "Team name | Wins | Draw | Lose | Points | Goal for | Goal Conceded"
        print x.teamName + " | " + str(x.win) + " | " + str(x.draw) + " | " + str(x.lose) + " | " + str(x.points) + " | " + str(x.goalFor) + " | " + str(x.goalConceded)

    return table