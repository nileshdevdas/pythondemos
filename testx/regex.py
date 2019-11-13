import re

expression = "^([0-9]{4})+-+([0-9]{4})+-+([0-9]{4})+-+([0-9]{4})+$"
data = "12932-9393-2993-2929"
def check_valid_card():
    if re.match(expression, data):
        return True
    else:
        return False
print(check_valid_card())

essay_on_cookies = """
I love cookies , cookies are made up of milk, sugar and flour, 
cookies are sweet and i like to eat cookies every day , 
cookies for breakfast , cookies for lunch and cookies for dinner, 
cookies make me happy and i think every one should eat cookies
"""
c_expression = "cookies"
print(re.sub(c_expression, "monkeys", essay_on_cookies))

email_finders_data= """
for any information send mail to info@vinsys.com
for complaints and tickets dev.support@vinsys.com
for any other issues itfm.support@vinsys.com 
"""
email_exp = "[a-zA-Z0-9.]+@+[a-zA-Z0-9]+.+[a-zA-Z]+"
print(re.findall(email_exp, email_finders_data))





