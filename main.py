class StudentsInMLOps :
    def __init__(self):
        self.totalStrength = 0

    def enrollStudents(self, numberOfStudents):
        self.totalStrength += numberOfStudents

    def dropStudents(self, numberOfStudents):
        self.totalStrength -= numberOfStudents

    def getTotalStrength(self):
        return self.totalStrength

    def getClassName(self):
        return self.__class__.__name__            
