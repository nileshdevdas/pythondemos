# function with params and return a value


def function_that_returns_value(param_1, param_2):
    return param_1 * param_2


def function_that_returns_value(param_1, param_2):
    print("In the base function")

    def a():
        print("Another funciton")
        print("You need to believ this")
        return 100 * 100
    return a


print(globals())
c1 = function_that_returns_value(1, 2)

# i am sayting c1()// because c1 is a callable (Function)
print(c1())
