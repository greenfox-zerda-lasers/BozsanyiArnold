from model import Model
from viewer import Viewer
import os


class Controller:
    playername =  ''
    playagain_question = ''
    def __init__(self):
        self.model = Model()
        self.viewer = Viewer()
        self.ask_name()
        self.welcome()
        os.system('cls' if os.name == 'nt' else 'clear')
        self.game_it()
    def ask_name(self):
        playername = input(self.viewer.askingname)
    def welcome(self):
        print(self.viewer.welcome.format(self.playername))
    def rules(self):
        print(self.viewer.rules)
    def game_it(self):
        print('This is your 1st try good luck.')
        while self.model.count_tries < 10:
            try :
                firstnum = int(input(self.viewer.tries1))
            except ValueError:
                print(self.viewer.onlynumpls)
                self.game_it()
            if firstnum == self.model.actual_number:
                print(self.viewer.victory)
                self.playagain()
            elif firstnum > self.model.actual_number:
                print(self.viewer.mine_is_smaller)
                self.model.count_tries += 1
            elif firstnum < self.model.actual_number:
                print(self.viewer.mine_is_bigger)
                self.model.count_tries += 1
        if self.model.count_tries == 10:
            print(self.viewer.lost)
            self.playagain()

    def playagain(self):
        print(self.viewer.playagain)
        playagain_question = input()
        if self.playagain_question != 'a':
            self.model.count_tries = 0
            self.game_it()
        else:
            self.model.count_tries = 11


controller1 = Controller()
