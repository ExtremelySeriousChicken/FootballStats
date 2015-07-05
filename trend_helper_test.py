__author__ = 'Edward'

# Test files for some of the files in the trend_helper.py
# This is because I have found some unwanted behavior in the
# trend_helper python file
def processLeagueInfo(league):
    countryList = list()
    result =  searchData(league, 'country', league[0]['country'])
    league = result['listDict']
    countryList.append(result['countryArray'])
    for y in league:
        print y
    for y in result['countryArray']:
        print "printing countryArray"
        print y

    print countryList

from trend_helper import searchFile, searchData
if __name__ == '__main__':
    #get the data from search file
    leagueArray = searchFile()
    processLeagueInfo(leagueArray)