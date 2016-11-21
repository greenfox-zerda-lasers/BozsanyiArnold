from view import View
from model import Model

class Game:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.ask_name()
        self.ask_class()

    def ask_name(self):
        self.view.name()
        self.model.playername = input().lower()
        if len(self.model.playername) == 0:
            self.view.name_error()
            self.ask_name()

    def ask_class(self):
        self.view.ask_class()
        self.view.print_attributes_w()
        self.view.print_attributes_m()
        self.view.print_attributes_t()
        self.model.playerclass = input().lower()

        if self.model.playerclass not in 'wtm' or len(self.model.playerclass) != 1:
            self.view.wrong_key()
            self.model.playerclass = input().lower()

        elif self.model.playerclass == 'w':
            self.model.strength += 7
            self.model.inteligence += 3
            self.model.luck += 5
            self.model.speed += 5
            self.view.clear_screen()
            self.view.choosen_warrior()

        elif self.model.playerclass == 'm':
            self.model.strength += 3
            self.model.inteligence += 7
            self.model.luck += 5
            self.model.speed += 5
            self.view.clear_screen()
            self.view.choosen_mage()

        elif self.model.playerclass == 't':
            self.model.strength += 5
            self.model.inteligence += 3
            self.model.luck += 5
            self.model.speed += 7
            self.view.clear_screen()
            self.view.choosen_thief()

        def play_in_z5(self):
            pass
        def in_armory(self):
            pass
        def in_vendor(self):
            pass
        def in_castle(self):
            pass




game1 = Game()
