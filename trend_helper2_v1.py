__author__ = 'Edward'

# This file will group the data based on the league name
# In version 2, it will group the data based on the league
# number. This file will calculate:
#     a. The trend of the points between the season
#     b. The rank position of the teams throughout the seasons
#     c. The trend of the win of a team throughout the season
#     d. The trend of the loss of a team throughout the season
#     e. The trend of the goal scored
#     f. The trend of the goal conceded

# Requires: The league data.
# Modifies: The league data
# Effects : This file will conver the data from
#     [{
#         country: {country: , league: (array data)
#     }]
#     To
#     [{
#         country: [{
#             name:
#             league: [{
#                         name:
#                         seasons: [{name: , source: }]
#                     }]
#         }]
#         league :
#         data   : [{season: , source: }]
#     }]
#
# We do this through making numerous classes

# The first class is country. This file stores the name and a league
# object
class country(object):
    def __init__(self,name):
        self.countryName = name
        self.leagues = list()

# The second is league
class league(object):
    def __init__(self,name):
        self.leagueName = name
        self.seasons = list()

#the last one is season
class season(object):
    def __init__(self,season,source):
        self.season = season
        self.source = source

def convert(league):
    countryList = list()
    for x in league:
         newCountry = country(x['country'])
         newCountry.leagues = makeLeague(x['league'])
         countryList.append(newCountry)

    for x in countryList:
        print "country name: " + x.countryName
        for y in x.leagues:
            print "league name: " + y.leagueName
            for z in y.seasons:
                print z

    return countryList

# Requires : The country
# Modifies : The league
# Effects  : going through each data and employ the division strategy
#            To classify data by calling searchSeason
def makeLeague(countryData):
    leagueList = list()
    while len(countryData) != 0:
        newLeague = league(countryData[0]['league'])
        result = searchSeason(countryData, newLeague.leagueName)
        countryData = result['countryData']
        newLeague.seasons = result['league']
        leagueList.append(newLeague)

    return leagueList

# Requires : The country data
# Modifies : the country Data
#
def searchSeason(leagueData, leagueName):
    x = 0
    seasonList = list()
    dictLength = len(leagueData)
    while x < dictLength:
        if leagueData[x]['league'] == leagueName:
            print "found: " + leagueData[x]['league'] + " and " + leagueName

            seasonList.append({'season' : leagueData[x]['season'],
                               'source' : leagueData[x]['source']})
            del leagueData[x]
            x = 0
            dictLength = len(leagueData)
        else:
            x+= 1
    return {'countryData': leagueData, 'league': seasonList}

