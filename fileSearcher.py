__author__ = 'Edward'
import glob, os

# FIXXXMEEEEEEEE
# Requires: Nothing
# Modifies : Nothing
# Effects  : Search for all the .csv file and then it will return
#            a list of the path to the data of different leagues
# Method   : we need to go into different folders in search of the
#            data. One way we can do this is to use recursive.as
#            So if they found a directory, go in and then recursive
# Method 2 : Another way we can do is to ascertain whether there is
#            a specific pattern in the path and then go in and then
#            find the csv files
# ANOTHER PROBLEM: SOME OF THE LEAGUES DOES NOT HAVE A FIXED IE
# ENGLAND 1880S have an extra "round" input
def searchFile():
    csvFiles = list()
    leagueInfo = list()
    for dirname, dirnames, filenames in os.walk('soccer_data/'):
        #for subdirname in dirnames:
            #print(os.path.join(dirname,subdirname))

        for filename in filenames:
            pass
            filePath = os.path.join(dirname,filename)

            if filePath[-3:] == "csv":
                csvFiles.append(filePath)
                newArray = [filePath]

        if '.git' in dirnames:
            dirnames.remove('.git')

    for x in range(len(csvFiles)):

        newArray = csvFiles[x].split("\\")
        #if the csv files is not "teams.csv"
        if newArray[len(newArray) - 1] != "teams.csv":
            league = newArray[1]
            year = newArray[-2]
            leagueName = newArray[-1]
            newNewArray = [league, year, leagueName, csvFiles[x]]
            leagueInfo.append(newNewArray)


    return leagueInfo