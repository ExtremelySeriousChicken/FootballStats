__author__ = 'Edward'


#This file is to test my assumption that if a team wins the
#Half time, it will have high chance of winning the game
#The way I am going to make this is:
# 1. The program will iterate through the data and for every league
#    I will calculate:
#        a. The probability of HT wins P(HT)
#        b. The probability of winning both the HT and the FT P(FT ^ HT)
#        c. The probability of winning FT given HT P(FT | HT)
#        d. The probability of FT wins P(FT)
#        e. The probability of winning HT give HT P(HT | FT)
#
# 2. The program will then store the data inside a csv file
#    The data in the csv file:
#        a. The name of the country
#        b. The league
#        c. The year
#        d. P(HT)
#        e. P(FT ^ HT)
#        f. P(FT | HT)
#
# 3.  From these data, we can test multiple hypothesis
# NOTE: THE MATHEMATICS FOR THIS FILE AS OF 4/7/2015 is wrong!
from classes import *

from dataProcessor import *
from fileSearcher import searchFile
from teamWriter import writeDir, writer

# Requires : the game object and the gameDictionary
# Modifies : the game object
# Effects  : This function will get the game object and determine
#            if the HT home wins etc
def processOneGameHypoOne(gameObj, gameDict):
    #first check if the home wins the half time
    if(gameDict['HT'][0] > gameDict['HT'][1]):
        gameObj.HomeHT += 1

    if(gameDict['FT'][0] > gameDict['FT'][1]):
        gameObj.HomeFT += 1

    if((gameDict['HT'][0] > gameDict['HT'][1]) and
           (gameDict['FT'][0] > gameDict['FT'][1])):
        gameObj.HomeHTFT += 1

    if(gameDict['HT'][0] < gameDict['HT'][1]):
        gameObj.AwayHT += 1

    if(gameDict['FT'][0] < gameDict['FT'][1]):
        gameObj.AwayFT += 1

    if((gameDict['HT'][0] < gameDict['HT'][1]) and
           (gameDict['FT'][0] < gameDict['FT'][1])):
        gameObj.AwayHTFT += 1

    return gameObj

# Requires : The data of one league
# Modifies : The data
# Effects  : It will iterate through the league and then it will
#            get the hone team, the away team and then the
#            scores. This function primarily try to satisfy
#            the first task
def processOneLeagueHypoOne(league):
    game = hypoOne()
    for x in league:
        #if there is no HT: exit
        if(x[4] == '' or x[4]=='-'):
            return{'pHT': 0.0,
                'pHTFT': 0.0,
                'pFT': 0.0,
                'pFTgivenHT': 0.0,
                'pHTgivenFT': 0.0}
        game.games += 1
        dataFT = x[3].split("-")
        dataFT = [int(dataFT[0]), int(dataFT[1])]
        HT = x[4].split("-")
        HT =[int(HT[0]), int(HT[1])]

        gameDict = {'home': x[1],
                    'away': x[2],
                    'FT': dataFT,
                    'HT': HT}

        #print gameDict

        game = processOneGameHypoOne(game, gameDict)

    pHT = float(game.HomeHT + game.AwayHT) / game.games
    pHTFT = float(game.HomeHTFT + game.AwayHTFT) / game.games
    pFT = float(game.HomeFT + game.AwayFT) / game.games
    pFTgivenHT = pHTFT / pHT
    pHTgivenFT = pHTFT / pFT

    return {'pHT': pHT,
            'pHTFT': pHTFT,
            'pFT': pFT,
            'pFTgivenHT': pFTgivenHT,
            'pHTgivenFT': pHTgivenFT}

def arrayIfy(dictArray):
    resultArray = list()
    baseArray = ['country','year','league','pHT','pFT','pHTFT','pHT given pFT','pFT given HT']
    resultArray.append(baseArray)
    for x in dictArray:
        newArray = [
            x['league data'][0],
            x['league data'][1],
            x['league data'][2][:-4],
            str(x['process one']['pHT']),
            str(x['process one']['pFT']),
            str(x['process one']['pHTFT']),
            str(x['process one']['pHTgivenFT']),
            str(x['process one']['pFTgivenHT'])
        ]

        resultArray.append(newArray)

    return resultArray

def dataProcess():
    #first search for the files
    files = searchFile()

    dictArray = list()

    writeThis = list()

    for x in files:
        league = readFile(x[3])
        processOne = processOneLeagueHypoOne(league)
        oneInfo = {'league data': x, 'process one': processOne}
        dictArray.append(oneInfo)
    returnThis = dictArray
    dictArray = arrayIfy(dictArray)
    writer("./results/gameProbabilities/gameProbabilities.csv", dictArray)
    return returnThis

if __name__=='__main__':
    dictArray = dataProcess()
    for x in dictArray:
        print x

    pHTgivenFT = 0.0
    length = 0
    pHTgFTless = 0
    for x in dictArray:
        if float(x['process one']['pHTgivenFT']) != 0.0:
            pHTgivenFT += float(x['process one']['pHTgivenFT'])
            length += 1
            if float(x['process one']['pHTgivenFT']) < 0.5:
                pHTgFTless += 1

    print pHTgivenFT
    print length
    print pHTgFTless
    print pHTgivenFT / length