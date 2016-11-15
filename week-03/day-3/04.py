class Students():
    grades = []
    def add_grade(self, grades):
        if grades >=1 and grades <= 5:
            self.grades.append(grades)
        else:
            return 'wrong grade , must be to much or to less!'
    def get_average(self):
        return sum(self.grades) / len(self.grades)

student1 = Students()
student1.add_grade(5)
student1.add_grade(4)
student1.add_grade(3)
print(student1.get_average())
