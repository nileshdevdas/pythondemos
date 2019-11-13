
"""
Documentation
"""

# comment 
################################################################
a = 10
b = "" 
c = True
e = range(1, 100)
f = [1, 2,3,4]
g = (1,2,3,4)
h = {1,2,3,3,5}
################################################################
if a < 20: 
    print("a is less than 20 ")
elif a > 20:
    print("a is greater than 20")
else: 
    print("A is 20")
################################################################
for e1 in e: 
    pass
    #print(e1)
################################################################
def function_name(file_name):
    file = open(file_name, 'r')
    line = file.readline()
    while line:
        print(line)
        line = file.readline()
################################################################
file_name = input("Enter File Name :-")
function_name(file_name)
################################################################