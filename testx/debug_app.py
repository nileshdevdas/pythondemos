
users = ['user1', 'user2']


def user_app():
    for u in users:
        myuser = u
        print(myuser)


def user_print():
    user_app()
    print("done and fine")


def user_demo():
    user_print()


user_demo()
