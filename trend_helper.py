__author__ = 'Edward'
import os

def searchData(listDict, keyword, data):
    countryArray = {'country': data,
                    'league': list()}
    length = len(listDict)
    x = 0
    while x < length:
        if(listDict[x][keyword] == data):
            countryArray['league'].append({
                'league'    : listDict[x]['leagueDict'],
                'leagueNum' : listDict[x]['leagueNum'],
                'season'    : listDict[x]['season'],
                'source'    : listDict[x]['source']
            })
            del listDict[x]
            x = 0
            length = len(listDict)
        else:
            x+=1

    return {'listDict': listDict, 'countryArray': countryArray}





# Requires : The list of league data processed from searchFile
# Modifies : the data passed from the argument
# Effects  : group the data; The resulting data should be as follow
#            [{
#                country: [{
#                             leagueNum:
#                             league:
#                             source:
#
#                         }]
#            }]
def processLeagueInfo(league):
    countryList = list()
    for x in league:
        country = x['country']
        result =  searchData(league, 'country', country)
        league = result['listDict']
        countryList.append(result['countryArray'])

    return countryList


# Requires : Nothing
# Modifies : Nothing
# Effects  : Will search through the results/tableMaker/ folder
#            for the data. Return the data
def searchFile():
    csvFiles = list()
    leagueInfo = list()
    for dirname, dirnames, filenames in os.walk('results/tableMaker/'):

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

    return leagueOverallArray