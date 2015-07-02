__author__ = 'Edward'
import csv
from classes import *

def readFile(filename):
    data = list()
    with open("1-premierleague.csv", 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in reader:
            data.append(row)

    del data[0]

    return data

def makeGame(data):
    gameList = list()

    for x in data:
        datum = x[3].split("-")
        datum[0] = int(datum[0])
        datum[1] = int(datum[1])
        newGame = game(x[1],x[2],datum[0],datum[1])

        gameList.append(newGame)


    return gameList

def process(filename):
    data = readFile(filename)

    gameList  = makeGame(data)

    #now we are going to process the winners

    for x in gameList:
         print (x.home + "," + x.away + "," + str(x.h) + "," + str(x.a))
        # print x.away
        # print x.h
        # print x.a

    return gameList
