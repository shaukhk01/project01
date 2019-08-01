class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks= marks
    def disp(self):
        print(self.name)
        print(self.marks)
    def grade(self):
        if self.marks > 60:
            print('First')
        elif self.marks > 50:
            print('second')
        elif self.marks > 40:
            print('pass')
        else:
            print('fail')
n =int(input('Enter a number of student'))
for x in range(n):
    name = input('Enter a name.')
    marks= int(input('Enter a marks'))
    s = student(name,marks)
    s.disp()
    s.grade()
    

