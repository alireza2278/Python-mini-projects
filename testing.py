users = {"ali":"858522","soheil":"984695","zahra":"365214"}
black_list = {"soheil"}

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        if args[0] in black_list:
            print("this user is blacklist!!!")
        else:
            func(*args,**kwargs)

    return wrapper_decorator

@decorator
def print_pass(username):
    print(username,":",users[username])
@decorator
def chenge_pass(username,new_pass):
    users[username] = new_pass
    print(username,":",new_pass)
    print(users)


print_pass("soheil")
chenge_pass("ali","6565")
