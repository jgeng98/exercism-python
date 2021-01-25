class Garden:

    default_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    
    def __init__(self, diagram, students=default_names):
        self.students = sorted(students)
        self.diagram = diagram.split("\n")

    def plants(self, name):
        plants = []
        for row in self.diagram:
            index = self.students.index(name)*2
            for num in range(index, index+2):
                if row[num] == 'C':
                    plants.append("Clover")
                elif row[num] == 'G':
                    plants.append("Grass")
                elif row[num] == 'R':
                    plants.append("Radishes")
                elif row[num] == 'V':
                    plants.append("Violets")
        
        return plants
