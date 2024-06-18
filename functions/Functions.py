# Functions: Funtions are used to compartmentalize a specific task or
# action on an aspect of business i.e. deals with separation of concerns.
# Delcared as - def functionName(arg1,arg2,...):
#                      # body of function
#                      # return statement
# to call a function - retValue = functionName(arg1,arg2,...)

# Program to impliment an employee insert and display operation with inmemory employee Database
# EmpDB: list
# Records of employees as tuples (empno,ename,sal)

def insertRecords(empDB,rec):
    empDB.append(rec)
    return "1"

def dispplayAlEmployees(empDB):
    if (empDB==[]):
        print("No employee records found.")
    cnt = 1
    for rec in empDB:
        print("Employee",cnt,"#",rec[0],rec[1],rec[2])
        cnt = cnt + 1

def getEmpDetails(empDB):
    print("Provide Employee Details:")
    empno = int(input("Empno:"))
    ename = input("Ename:")
    sal = int(input("Salary:"))
    rec = (empno,ename,sal)
    no = insertRecords(empDB,rec)
    print(no,"records inserted...")

def viewMenu(empDB):
    cont = "y"
    while(cont == "y"):
        print("1: Insert a record\n2: Display all records\n0: To Exit")
        res = int(input("Your choise: "))
        if(res==1):
            getEmpDetails(empDB)
        elif(res==2):
            dispplayAlEmployees(empDB)
        elif(res==0):
            cont = "n"
        else:
            print("Invalid Choice...")

# Initialize Employee Database
empDB = []
viewMenu(empDB)
