# monkey patches


def validate_user(username, password):
    print(username)
    print(password)

def monkey_function(uname, passwd):
    print("You are patched ")
    print("you are fooled by a monkey")


validate_user("nilesh", "nilesh")

validate_user = monkey_function

validate_user("nilesh", "nilesh")

