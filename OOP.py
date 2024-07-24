"""
class students:
    def __init__(self,fname,lname,grade,group):
        self.fname = fname
        self.lname = lname
        self.grade = grade
        self.group = group

s1 = students("Junaid","Mk","A+","Computer Science")
s2 = students("alivin","leung","A+","Medical")
s3 = students("Ahsan","Khan","A","Computer Science")
s4 = students("jamshed","lahori","c","commerce")

print(s2.lname)

"""


class Employee:

    increment = 1.5
    No_of_employee = 0
    Senior = "Mr."
    def __init__(self,fullname,Status,salary):
        self.fullname = fullname
        self.status = Status
        self.Salary = salary
        Employee.No_of_employee += 1

    def increase(self):
        self.Salary = int(self.Salary * Employee.increment) 
    
    def senior(self):
        self.fullname = Employee.Senior + self.fullname

    def __repr__(self):
        return "Employee({},{},{})".format(self.fullname,self.status,self.Salary,self)
        pass
    @classmethod
    def change_in_increment(cls,amount):
        cls.increment = amount
    @classmethod
    def from_str(cls,emp_string):
        fullname , status , Salary = emp_string.split("-")
        return cls(fullname,status,Salary)

class programmar(Employee):
    def __init__(self, fullname, Status, salary , prolang , experince):
        super().__init__(fullname, Status, salary)
        self.prolang = prolang
        self.experince = experince

Junaid = Employee("Junaid MK", "Fullstack Developer" , 12000)
Ahsan = Employee("Ahsan Khan", "Backend Developer" , 10000)
Waris = Employee("Waris Mangi", "frontend Developer" , 9000)
Haris = Employee.from_str("HarisSoomro-Backend-10000")
Junsteel = programmar("Junsteel Legend" , "Fullstack" , 45000 , "Python , Html , Css , javaScrip , Swift , SwiftUi" , "Beginner")

# print(Employee.No_of_employee)

# print(Junaid.Salary)
# Junaid.increase()
# print(Junaid.Salary)

# print(Junaid.__dict__)

# print(Waris.fullname)
# Waris.senior()
# print(Waris.fullname)

# print(Junaid.Salary)
# Employee.change_in_increment(2)
# Junaid.increase()
# print(Junaid.Salary)

# print(Haris.fullname)
# print(Haris.Salary)
# print(Haris.status)

# print(Junsteel.experince)
# print(Junsteel.status)
# print(Junsteel.prolang)
# print(Junsteel.fullname)

#print(Junaid)