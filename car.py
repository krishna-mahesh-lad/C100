class Team(object):
    def __init__(self, name, age, gender, level, grade = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grade = {}
    
    def setg(self, course, grade):
        self.grade[course] = grade
    
    def getg(self, course):
        return self.grade[course]

    def getcgpa(self):
        return sum(self.grade.values())/len(self.grade)
        

#define some students
Winter = Team('Winter', 13, 'Female', 1, {'Math': 3})
print(Winter.getcgpa())