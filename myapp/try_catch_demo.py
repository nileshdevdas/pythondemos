

a = 1
b = 0

try:
    open("d:/invisiblefile.txt", 'r')
    a/b
except ArithmeticError as e:
    print("Some Error Occured")
    print(e)
except FileNotFoundError as e:
    print("Error")
finally:
    print("You cleanup you sins here....")
