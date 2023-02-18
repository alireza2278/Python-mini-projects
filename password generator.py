import random
import string
letters = string.ascii_letters
symbols = "~!@#$%^&*()_+=[]{}*/><?"
numbers = "0123456789"

all = letters + symbols + numbers
while True:
    print("Choice an Option:\n\t1: Creat password\n\t2: Exit")
    choice = input("Your Choice: ")
    if choice == "1":
        length = int(input("Enter the length of password: "))
        password = "".join(random.sample(all,length))
        print("*" * 40)
        print(password)
        print("*"*40)
    elif choice == "2":
        print("see you!")
        break
    else:
        print("Wrong!")
