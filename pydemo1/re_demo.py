import re 

# check only lower case 
print(re.search("^[a-z]+$", "nileshD"))

print(re.search("^[A-Z]+$", "NILESHD"))

print(re.search("^[A-Za-z0-9.]+@+[A-Za-z0-9]+.+[(a-zA-Z)\d{3}]+$", "nilesh.devdas@vinsys.com"))