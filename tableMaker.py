__author__ = 'Edward'

import csv

from classes import *

from dataProcessor import *

from teamGenerator import *


data = process("a")

league = createTeam(data)

league = calculatePts(league, data)