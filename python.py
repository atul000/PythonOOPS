# check if employee has achieved his weekly target or not
class Employee:
    name = 'Ben'
    designation = 'sales manager'
    salesMadeThisWeek = 6

    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("target has been achieved")
        else:
            print("target not achieved")


employeeOne = Employee()
employeeOne.hasAchievedTarget()
employeeTwo = Employee()


class Employee:
    numberOfWorkingHours = 40


employeeOne = Employee()
employeeTwo = Employee()
print(employeeOne.numberOfWorkingHours)
employeeOne.name = "john"
employeeOne.name
employeeTwo.name = "atul"
print(employeeTwo.name)


# Self parameter
class Employee:
    def employeeDetails(self):
        self.name = 'Atul'
        print("Name = ", self.name)
        age = 30
        print("Age = ", age)

    def printEmployeeDetails(self):
        print("Printing in anotehr method")
        print("Name: ", self.name)
        print("Age: ", age)


employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()
Employee.employeeDetails(employee)


# METHODS: STATIC & INSTANCE
class Employee:
    def employeeDetails(self):
        self.name = 'atul'

    @staticmethod
    def welcomeMessage():
        print("welcome to the company")


employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()


# INIT METHOD
class Employee:
    def __init__(self, name):
        self.name = name

    def displayEmployeeDetails(self):
        print(self.name)


employee = Employee("atul")
employeeTwo = Employee("alex")

employee.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()


# INIT METHOD
class Rectangle:
    def __init__(self, length, breadth, unit_cost=0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost

    def get_area(self):
        return self.length * self.breadth

    # def calculate_cost(self):
    #     area = self.get_area()
    #     return area * self.unit_cost


# breadth = 120 units, length = 160 units, 1 sq unit cost = Rs 2000
r = Rectangle(160, 120, 2000)
print("Area of Rectangle: %s sq units" % (r.get_area()))
