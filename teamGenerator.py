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

# Requires : The table and the fixtures
# Modifies : the table
# Effects  : go through each of the fixtures and then calculate
#            The statistics of the table
def calculatePts(table,fixtures):
    for game in fixtures:
        #go through each game
        game