# function can have variable arguments 
# advantage (Becomes a little future proof )
# however needs to be strongly documented 
def function_with_var_args(*micheal):
    print(micheal)

# the * denotes that i will accept a tuple 
# all the parameter will get converted to a tuple 
function_with_var_args(1,2,3,4,54,5,6,6,'x', [1,2,3,4])