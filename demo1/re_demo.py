import re;


st = re.match("Ab", "Abhishek does the activity of asian art")
print(st.span())


st1 = re.match("[a-zA-Z]", "Abhishek does the activity of asian art")
print(st1)