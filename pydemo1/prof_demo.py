import cProfile

def do_something():
    abc()
def abc():
    xyz()
def xyz():
    pass
def hello():
    print("xxxx")
    a = range(1, 1000)
    for i in a:
        do_something()
cProfile.run('hello()')
