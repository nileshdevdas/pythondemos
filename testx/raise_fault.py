

def abc():
    raise Exception("this is very bad")


try:
    abc()
except Exception as e:
    print(e)
finally:
    print("this willl printx")
