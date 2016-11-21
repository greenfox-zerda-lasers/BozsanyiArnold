from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.view.draw(self.model.levels, self.model.people_count, self.model.current_level)
        self.view.functions()
        self.handle_inputs()

    def handle_inputs(self):
        which_funct = input()
        if which_funct not in 'wasdx' or len(which_funct) > 1 or len(which_funct) == 0:
            self.view.error_messeage()
            self.handle_inputs()

        else:
            if which_funct == 'a':
                self.model.add_people()
                self.view.draw(self.model.levels, self.model.people_count, self.model.current_level)
                self.view.functions()
                self.handle_inputs()

            elif which_funct == 'd':
                self.model.rem_people()
                self.view.draw(self.model.levels, self.model.people_count, self.model.current_level)
                self.view.functions()
                self.handle_inputs()

            elif which_funct == 'w' and self.model.levels - 1 == self.model.current_level:
                self.view.draw(self.model.levels, self.model.people_count, self.model.current_level)
                self.view.functions()
                self.view.highest_lv()
                self.handle_inputs()

            elif which_funct == 'w' and self.model.levels != self.model.current_level:
                self.model.move_up()
                self.view.draw(self.model.levels, self.model.people_count, self.model.current_level)
                self.view.functions()
                self.handle_inputs()

            elif which_funct == 's' and self.model.current_level == 0:
                self.view.draw(self.model.levels, self.model.people_count, self.model.current_level)
                self.view.functions()
                self.view.lowest_lv()
                self.handle_inputs()

            elif which_funct == 's' and self.model.current_level != 0:
                self.model.move_down()
                self.view.draw(self.model.levels, self.model.people_count, self.model.current_level)
                self.view.functions()
                self.handle_inputs()

            elif which_funct == 'x':
                self.view.clear_screen()

controller1 = Controller()
