import time

while True:
    choice = input("Do you want to start:\n\tYes or No?")
    if "y" in choice.lower():
        hour = int(input("Enter The hour: "))
        minutes = int(input("Enter The minutes: "))
        secend = int(input("Enter The secend: "))
        jam = hour*60*60 +minutes*60 +secend
        print("start timer:")
        time.sleep(1)
        while jam!=0:
            print(jam)
            jam-=1
            time.sleep(1)
    elif "n" in choice.lower():
        print("Exit")
        break
    else:
        print("Wrong")