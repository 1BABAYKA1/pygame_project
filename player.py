class Player():

    def __init__(self, side, name):
        self.side = side
        self.points = 0
        self.name = name

    @property
    def score(self):
        return self.points

    @score.setter
    def score(self, val):
        self.points += val