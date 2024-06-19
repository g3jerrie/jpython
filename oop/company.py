# Construct of a class in Python
# class ClassName

# Entity class

class Employee:

    # Class variable: Has only one occurance for the entire life of the program irrespectiveof the number of instance created for it.
    # Variable created without using 'self'.
    noOfEmployees = 0

    # Initializers
    def __init__(self,empId,empName,empSal): #self is pointer representing the current class
        # Initialize to create objects empno, ename, esal
        self.eno = empId
        self.ename = empName
        self.esal = empSal
        Employee.noOfEmployees = Employee.noOfEmployees + 1

    # Knowing responsibilities of an object
    def getEmpId(self):
        return self.eno
    def getEmpName(self):
        return self.ename
    def getEmpSal(self):
        return self.esal
    
    # Doing responsobilities
    def setEmpname(self,name):
        self.ename = name
    def setEmpSal(self,sal):
        self.esal = sal

    # Defining a static method
    @staticmethod # initializing wih a decorator method and not declaring as 'self' just like static variable
    def getTotalEmployees():
        return Employee.noOfEmployees
    
# Action class

class Company:

    def __init__(self,name):
        self.companyName = name
        self.EmployeeList = [] # Blank List

    # Action methods on the employees

    def getCompanyName(self):
        return self.companyName
    
    def createEmployee(self,name,sal):
        # Autonegerate EmpId like EMP1, EMP2, etc by adding 1 to the current value of Employee.noOfEmployees
        empcnt = Employee.getTotalEmployees() + 1
        empId = "EMP" + str(empcnt)
        e = Employee(empId,name,sal) # creating Employee object to create new employee
        self.EmployeeList.append(e) # add the newly created Employee to the empploye list in the company

    def displayAllEmployees(self):
        cnt = 1
        for e in self.EmployeeList:
            print("Employee",cnt,"#",e.getEmpId(),"|",e.getEmpName(),"|",e.getEmpSal())
            cnt = cnt + 1
    
if(__name__ == '__main__'):
    c1 = Company("Alphabet")
    print("The company is:",c1.getCompanyName())
    c1.createEmployee("AAA",50000)
    c1.createEmployee("BBB",70000)
    c1.createEmployee("CCC",90000)
    c1.createEmployee("DDD",30000)
    c1.displayAllEmployees()

    c2 = Company("Google")
    print("The company is:",c2.getCompanyName())
    c2.createEmployee("ZZZ",40000)
    c2.createEmployee("YYY",60000)
    c2.createEmployee("XXX",80000)
    c2.createEmployee("WWW",20000)
    c2.displayAllEmployees()