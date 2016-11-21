# Create an elevator controller class
# It should take an user input by listening to user input
# List of commands:
#
#  - Move elevator up
#  - Move elevator down
#  - Add people
#  - Remove people
#
#  Features to implement:
#   - Always draw the state of the elevator as depicted in "art.txt"
#   - [ x ] is the elevator. X means it has at least 1 person inside
#   - Moving floors should take time
#   - don't move beyond limits
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects
from viewer import Viewer
from model import Model
import os

class Controller:
    def __init__(self):
        self.model = Model()
        self.viewer = Viewer()
        self.viewer.draw(self.model.levels, self.model.people_count, self.model.position)
        self.viewer.functions()
        self.check_function()

    def check_function(self):
        exit = ''
        while exit != 'x':
            self.ask_motion()
            self.viewer.draw(self.model.levels, self.model.people_count, self.model.position)
            self.viewer.functions()
    def move(self):
        try:
            moveput = int(input('Which level would you like to go???'))
        except ValueError:
            print('Please insert only number.')
        if moveput > 0 and moveput < self.model.levels:
            self.model.level = moveput
        self.model.position = self.model.levels

    def ask_motion(self):
        motion = input().lower()
        if motion in 'arx':
            if motion == 'a':
                self.model.add_people()
            elif motion == 'r':
                self.model.remove_people()
            else:
                self.exit = 'x'
        elif isinstance(int(motion), int):
            self.move()





controller = Controller()
