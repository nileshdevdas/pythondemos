class Employee:
    version = 1.0
    @classmethod
    def copyright(cls):
        print("Copyright Nilesh Class Level Method")

    def calculate_salary(self):
        print("Calculate Salary of Employee...")

    def __init__(self):
        print("constructor")

    def __del__(self):
        print("descructor")

    def __str__(self):
        #"String representation of the object "
        return "Employee"


class Manager(Employee):
    def calculate_salary(self):
        super().calculate_salary()
        print("Calculating Salary of Manager")


class Supervisor(Manager):
    pass


class President(Manager):
    pass

emp = Manager()
emp.calculate_salary()

emp1 = Employee()
emp1.calculate_salary()
