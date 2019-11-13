

try: 
    10/0
except ArithmeticError as e:
    print(e.args)
finally:
    print("Completed")