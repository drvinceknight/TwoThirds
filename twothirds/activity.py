"""A class for an overall activity"""
from twothirds import Data, TwoThirdsGame

class Activity:
    def __init__(self, filename):
        self.raw_data = Data(filename)
        self.raw_data.read()
        self.data = self.raw_data.out()
        self.games = [TwoThirdsGame(d) for d in self.data]

    def analyse(self):
        self.two_thirds = [game.two_thirds_of_the_average() for game in
                           self.games]
        self.winners = [game.find_winner()[0] for game in self.games]
        self.winning_guesses = [game.find_winner()[1] for game in self.games]

    def __repr__(self):
        string = ''
        for i, game in enumerate(self.games):
            string += """=====================
Game {}
---------------------
2/3rds of the average: {:.2f}
Winning guess: {}
Winner(s): {}
""".format(i, self.two_thirds[i], self.winning_guesses[i],
                    self.winners[i])
        return string

