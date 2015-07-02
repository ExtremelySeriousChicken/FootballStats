__author__ = 'Edward'
import glob, os

#FIXXXMEEEEEEEE
def searchFile():
    for file in os.listdir("soccer_data/"):
        print(file)
        if file.endswith(".csv"):
            print(file)