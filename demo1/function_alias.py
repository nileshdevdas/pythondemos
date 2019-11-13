

def super_function():
    print("this is a super function")


not_so_super = super_function

not_so_super()

super_function = lambda : print("you have been terminated")

super_function()
not_so_super()
