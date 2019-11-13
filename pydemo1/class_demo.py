

class Employee:
    def __init__(self):
        self.username = "nilesh"
        print("initialized....")

    @classmethod
    def demo_method(cls):
        print(cls)
        print("this is classmethod")


class Manager(Employee):
    def __init__(self):
        super().__init__()
        print("initialized....")


Employee.demo_method()

e = Employee()
print(e.username)
#m = Manager()
