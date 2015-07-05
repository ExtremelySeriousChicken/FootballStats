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
#s
from trend_helper import searchFile, processLeagueInfo
from trend_helper2_v1 import convert, country, league, season
if __name__=='__main__':
    leagueArray = searchFile()


    result = processLeagueInfo(leagueArray)
    cleanResult = convert(result)
