class Employee:
    # declared in side the class is a class variable
    username = "nilesh"

    # if you wish to create methods
    # that can be accessed with class level accessors
    # the method requires a decorator @classmethod
    @classmethod
    def class_method1(cls):
        print(cls)
        print("This is class Method")

    def __init__(self):
        print("Constrcutor.............")
        self.version = 1
        self.data = "something"
        self.activity_name = "super"

    def __del__(self):
        print("Destructor.............")

    def __str__(self):
        return "This is a Employee....."

# when you wish to extend a class you simply 
#  Manager(Employee)
class Manager(Employee):
    def __init__(self):
        super().__init__()

#emp = Employee()
# print(emp)
mgr = Manager()

#







# a class in Python is  writting 
""" 
class Employee: 
    pass 

python class has  class level and instance level variable 
python class has  classs level and instnace level functions

class Employee: 
    #this is class level variable
    # can be accessed Employee.employeeName
    employeeName

class Employee:
    def __init__(self):
        self.username = "nilesh"
The __init__ is like a constreuctor 
the __init__ method get called implicitly when you 
# create a object from a class however you need to understand
called only when you write one 
The init method takes a paramter self (ideally to be named as
self) not mandatory to be self 
if you wish to create instance level vars the 
you can create the same using self.varname 
The variables that you create using self.varname can be 
accessed only and only when you use .... 
object.varname and not accessible className.varname

there is amethod  __del__ this acts as descrtuctor 
there is method  __str__ this is used as when ever 
you push a ref to stream then the it call the __str__

Note very cleary you can write a clas level method also 
like you can write a object level method 
@classmethod  (as the decorator )
def xxx(cls):
    pass 
the above will act as a class level method and does not 
need you to isntantiate the object to access the method 


Inheritence : 
The inheritence is simplified and works in a simple way 
class Manager(Employee):
    pass 
All the inheritence methods are accessible and would be access
by manager whenever applicable except the class methods 

What ever define in the classess as the class level is not 
inheritable but whatever you define for the object level 
is inheritable 





















""" 








