import attr


@attr.s
class Employee:
    username = attr.ib(default="nilesh")
    password = attr.ib(default="")


print(Employee().__getattribute__("username"))
