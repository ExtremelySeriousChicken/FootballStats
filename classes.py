__author__ = 'Edward'

class game(object):
    def __init__(self, home, away, homeScore, awayScore):
        self.home = home
        self.away = away
        self.h = homeScore
        self.a = awayScore

class teamProfile(object):
    def __init__(self, id, team):
        self.id = id
        self.teamName = team
        self.win = 0
        self.draw = 0
        self.lose = 0
        self.points = 0
        self.goalFor = 0
        self.goalConceded = 0
