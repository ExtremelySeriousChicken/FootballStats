__author__ = 'Edward'

import csv

from classes import *

from dataProcessor import *

from teamGenerator import *

from teamWriter import *

from fileSearcher import *

def makeTable():
    listArray = searchFile()

    for x in listArray:
        country = x[0]
        year = x[1]

        fileName = x[2]
        path = x[3]
        data = process(path)
        league = createTeam(data)
        league = calculatePts(league,data,year)
        writeTo = "results/tableMaker/" + country + "/" + year + "-" + fileName
        writeDir("result/tableMaker/",country)
        writeTableMaker(writeTo,league)

if __name__=="__main__":
    makeTable()

