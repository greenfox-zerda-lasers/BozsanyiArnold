# Create an "elevator" class
# The class should track the following things:
#  - elevator position
#  - elevator direction
#  - people in the elevator
#  - add people
#  - remove people
#
# Please remeber that negative amount of people would be troubling

class Model:
    levels = 11
    position = 0
    people_count = 0
    level = 0
    def add_people(self):
        self.people_count += 1
    def remove_people(self):
        if self.people_count > 0:
            self.people_count -=1
