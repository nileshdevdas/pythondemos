
a = ['nilesh', 'ramesh', 'satish', 'ahishek', 'prakash']

newusers = sorted(a, reverse=True)
print(newusers)
def sorter(data):
    if data=='username':
        return 0
    else:
        return 1

users = {'username': 'nilesh','password' :'abcded'}
print(sorted(users, key=sorter))