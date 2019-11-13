
# how to make use of locals and globals


def function_with_local_values():
    a = 10
    b = 20
    c = 30
    global nilesh
    nilesh = "ABCSDJISD"
    print(locals())

function_with_local_values()
print(locals())