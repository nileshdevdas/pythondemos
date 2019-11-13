# these key value you are passing named args 

def function_with_named_dict_vargs(**kwargs):
    print(kwargs)


function_with_named_dict_vargs(a=10, b=20, c=30, d=40)