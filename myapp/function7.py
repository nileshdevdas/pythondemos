
# variable + named both can be passed at the same time 
def function_with_both_types_args(*micheal, **maddonaa):
    print(micheal)
    print(maddonaa)

function_with_both_types_args({1,2,3,4,6}, {'a': 'nilesh'}, b=10)