from collections import defaultdict

class School:
    def __init__(self):
        self.school = defaultdict(list)

    def add_student(self, name, grade):
        self.school[grade].append(name)
        self.school[grade].sort()

    def roster(self):
        roster = []
        for grade in sorted(self.school.keys()):
            roster.extend(self.school.get(grade))
        return roster

    def grade(self, grade_number):
        return self.school[grade_number]
