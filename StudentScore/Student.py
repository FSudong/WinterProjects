class Student:


    def __init__(self,name, testScore, workScore):
        self.name = name
        self.testScore = float(testScore)
        self.workScore = float(workScore)
        self.finalScore = float(testScore)*0.3 + float(workScore)*0.7

    def setLevel(self, level):
        self.level = level



class Class:
    studentList = []
    def __init__(self,list):
        if len(list) == 0:
            self.studentList = []
        self.studentList = list

    def addStudent(self, student):
        self.studentList.append(student)

    def calAverScore(self):
        self.maxScore = 0.0
        scoreSum = 0.0
        for s in self.studentList:
            scoreSum += s.finalScore
            if s.finalScore > self.maxScore:
                self.maxScore = s.finalScore
        self.averScore = scoreSum / len(self.studentList)

    def calStudentLevel(self):
        for s in self.studentList:
            Proportion = s.finalScore / self.maxScore
            if Proportion > 0.9:
                s.setLevel("A")
            elif Proportion > 0.8:
                s.setLevel("B")
            elif Proportion > 0.6:
                s.setLevel("C")
            else:
                s.setLevel("D")
    def printAllStudent(self):
        for s in self.studentList:
            print("{}--> test {}  work {}  final {}  level {}".format(s.name,s.testScore,s.workScore,s.finalScore, s.level))

if __name__ == '__main__':
    s1 = Student("aa","100","70")
    s2 = Student("BB","90","80")
    s3 = Student("CC","70","100")
    s4 = Student("dd","50","80")
    s5 = Student("EE","50","50")

    group = Class([])
    group.addStudent(s1)
    group.addStudent(s2)
    group.addStudent(s3)
    group.addStudent(s4)
    group.addStudent(s5)

    group.calAverScore()
    group.calStudentLevel()
    group.printAllStudent()

