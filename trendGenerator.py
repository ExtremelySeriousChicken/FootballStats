__author__ = 'Edward'

# Documentation on the file:
# This file will take in the data from the csvs files created from
# tableMaker.py and then it will try to generate files of the
# trend. The csv files should reflect the trend for different
# leagues for different countries for different years and leagues
#
# The source file format: result/tableMaker/{country}/
# {seasonStart}-{seasonEnd}-{leagueNumber}-{leagueName}
#
# Method of assessment:
# 1. This is a bit tricky. There are two ways in which
#    we can assess trend: through the division name
#    (ie premier league, championship) or trend through
#    different league number (eg 1 2 ...). This is beacause
#    in england, the top league changes when premierleague was introduced
#
# 2. For the first method, let us just use the league name. The
#    next tricky part is how to collect the data.
#
# 3, The trend that we want to gather:
#    a. ranking
#    b. points
#    c. wins
#    d. loss
#    e. goal scored
#    f. goals conceded

import os

# Requires: the listDictionary, the keyword that we are finding
#
#
def searchData(listDict, keyword, data):
    print "searching for " + data
    countryArray = {'country': data,
                    'league': list()}
    length = len(listDict)
    x = 0
    while x < length:
        print str(x) + " " + str(len(listDict))
        if(listDict[x][keyword] == data):

            countryArray['league'].append({
                'league' : listDict[x]['leagueDict'],
                'leagueNum' : listDict[x]['leagueNum'],
                'source': listDict[x]['source']
            })
            del listDict[x]
            x = 0
            length = len(listDict)
        x+=1

    return {'listDict': listDict, 'countryArray': countryArray}





# Requires : The list of league data processed from searchFile
# Modifies : the data passed from the argument
# Effects  : group the data; The resulting data should be as follow
#            [{
#                country: [{
#                             name: [(ie Portugal etc)
#                             leagueName: [{
#                                           name:
#                                           number:
#                                           data :[{
#                                                       season:
#                                                       source:
#                                                  }]
#                                          }]
#                         }]
#           }]
def processLeagueInfo(league):
    countryList = list()
    for x in league:
        country = x['country']
        result =  searchData(league, 'country', country)
        league = result['listDict']
        countryList.append(result['countryArray'])
        for y in league:
            print y
        for y in result['countryArray']:
            print "printing countryArray"
            print y

    print countryList


# Requires : Nothing
# Modifies : Nothing
# Effects  : Will search through the results/tableMaker/ folder
#            for the data. Then process the resulting data
def searchFile():
    csvFiles = list()
    leagueInfo = list()
    for dirname, dirnames, filenames in os.walk('results/tableMaker/'):
        #for subdirname in dirnames:
            #print(os.path.join(dirname,subdirname))

        for filename in filenames:
            pass
            filePath = os.path.join(dirname,filename)

            if filePath[-3:] == "csv":
                csvFiles.append(filePath)

        if '.git' in dirnames:
            dirnames.remove('.git')

    leagueOverallArray = list()
    for x in csvFiles:
        newArray = x.split("/")

        newArray = newArray[2].split("\\")
        leagueArray = newArray[1].split("-")
        leagueDict = {
            'country'    : newArray[0].split("-")[1],
            'season'     : leagueArray[0] + "-" + leagueArray[1],
            'leagueNum'  : leagueArray[2],
            'leagueDict' : leagueArray[3][:-4],
            'source'     : x
        }
        leagueOverallArray.append(leagueDict)

    #here we are going to group them based on
    #country: Then the
    leagueOverallArray = processLeagueInfo(leagueOverallArray)



    #return leagueOverallArray


    #return leagueInfo

if __name__=='__main__':
    searchFile()

