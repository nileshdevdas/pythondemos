

def param_demo(a, b , c=10):
    print(a)
    print(b)
    print(c)
    return 100

def myfunc( *argv,**kwargs,):
  print(kwargs)
  print(argv)
myfunc(1,2,3 , a=1,b=2,c=1)

print(param_demo(1,2))