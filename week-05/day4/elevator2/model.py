class Model:
    levels = 11
    people_count = 0
    current_level = 0

    def add_people(self):
        self.people_count += 1

    def rem_people(self):
        if self.people_count > 0:
            self.people_count -= 1

    def move_up(self):
        if self.current_level < self.levels - 1:
            self.current_level += 1

    def move_down(self):
        if self.current_level > 0:
            self.current_level -= 1
