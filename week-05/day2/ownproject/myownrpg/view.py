import texts
import os

class View:
    def name(self):
        print(texts.name)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def name_error(self):
        print(texts.name_error)

    def ask_class(self):
        print(texts.ask_class)

    def print_attributes_w(self):
        print(texts.warrior_des)
        print(texts.warrior)

    def print_attributes_m(self):
        print(texts.mage_des)
        print(texts.mage)

    def print_attributes_t(self):
        print(texts.thief_des)
        print(texts.thief)

    def wrong_class(self):
        print(texts.choose_class_wrong_key)

    def choosen_thief(self):
        print(texts.if_thief)

    def choosen_warrior(self):
        print(texts.if_warrior)

    def choosen_mage(self):
        print(texts.if_mage)

    def welcome_msg(self):
        print(texts.welcome_msg)

    def opt_wrong_key(self):
        print(texts.opt_wrong_key)

    def instructions(self):
        pass
