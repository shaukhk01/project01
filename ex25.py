class student:
    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name
    def setmarks(self,marks):
        self.marks = marks
    def getmarks(self):
        return self.marks
n = int(input('Enter a no of student'))
for x in range(n):
    name = input('Enter a name.')
    marks= int(input('Enter a marks.'))
    s = student()
    s.setname(name)
    s.setmarks(marks)
    print(s.getname())
    print(s.getmarks())

