# Construct of a class in Python
# class ClassName

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
    
if(__name__ == '__main__'):
    e1 = Employee (101,"AAA",50000)
    e2 = Employee (102,"BBB",70000)
    print("First Employee:",e1.getEmpId(),",",e1.getEmpName(),",",e1.getEmpSal())
    print("Second Employee:",e2.getEmpId(),",",e2.getEmpName(),",",e2.getEmpSal())
    print("Total Number of Employees:",Employee.getTotalEmployees())