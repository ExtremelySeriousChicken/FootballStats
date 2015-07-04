__author__ = 'Edward'
import csv
from classes import *

def readFile(filename):
    data = list()
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in reader:
            data.append(row)

    #now find the data
    infoArray = data[0]
    for x in range(len(infoArray)):
        infoArray[x] = str(infoArray[x]).lower()
        infoArray[x] = infoArray[x].replace(" ", "")

    del data[0]

    dateIndex = -1
    for x in range(len(infoArray)):
        if infoArray[x] == "date":
            dateIndex = x

    if dateIndex == 1:
        if dateIndex > 1:
            print "there is something wrong with date Index!"
            exit(1)
        for x in range(len(data)):
            del data[x][0]

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

    return gameList
