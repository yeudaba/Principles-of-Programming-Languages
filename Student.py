
class Student:
    def __init__(self,Name,last_name):
        self.name = Name
        self.Last_Name = last_name
        self.Grades = []

    def __add__(self,Number):
        self.Grades.append(Number)
        return self

    def __str__(self):
        return f'{self.name} {self.Last_Name} {self.Grades}'

    def __eq__(self,c):
        if self.Last_Name==c.Last_Name:
            if self.name==c.Name:
                return True
            else:
                return False
        else:
            return False


    def Average(self):
        return sum(x for x in self.Grades)/len(self.Grades)

    def sumStudents(self):
        return len(self.Grades)

    def SetName(self,Name1):
        self.Name = Name1
        return self

    def GetName(self):
        return self.Name

    def SetLastName(self,LastName1):
        self.LastName = LastName1

    def GetLastName(self):
        return self.LastName


