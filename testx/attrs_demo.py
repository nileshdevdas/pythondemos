import attr

@attr.s
class Employee:
    username = attr.ib(default=100)


print(Employee().username)

print(Employee().__getattribute__("username"))