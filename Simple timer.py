import time
from os import system,name
while True:
    choice = input("want your choice:\n  (Yes or No?)")
    if "y" in choice.lower():
        hour = int(input("Enter hour: "))
        minutes = int(input("minutes hour: "))
        secend = int(input("Enter secend: "))
        total = hour * 60 * 60 + minutes * 60 + secend
        print("Timer Starting Now...")
        time.sleep(1)
        while total !=0 :
            print(total)
            total-=1
            time.sleep(1)
            if name=="nt":
                system("cls")
            else:
                system("clear")
        print("Timer ended :)")
    elif "n" in choice.lower():
        print("Exit")
        break
    else:
        print("choice Wrong!")