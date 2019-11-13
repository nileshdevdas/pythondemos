# functions with paramters and + defualt values
# default values always on the right side


def function_with_def_params(param_1, param_2,
                             param3_def=10, param4_def=20):
    print(param_1)
    print(param_2)
    print(param3_def)
    print(param4_def)


function_with_def_params(1, 2)
function_with_def_params(100, 200, 300, 400)
