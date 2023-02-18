while True: #حلقه بی نهایت
         #چاپ درخواست از کاربر
    print("Choice Your Option:\n\t1:Encrypt\n\t2:Decrypt\n\t3:Exit")
         #قرار دادن انتخاب در متغیر
    ch=input("Your Choice:")
        # تحلیل دخواست
    if ch=="1":
        plan_text = input(" Enter Text:") #وارد کردن متن ساده
        encrypted_text=""
        for c in plan_text:
            x = ord(c)*5+2 #تبدیل متن به کد اسکی و رمز نگاری همزمان
            encrypted_text+=chr(x)#تبدیل کد اسکی به حروم ناخوانا
        print("Encrypted_Text: ",encrypted_text) #چاپ متن رمز نگاری شده
        print("*"*40+"\n")

    elif ch=="2":
        encrypted_text = input(" Encrypted Text:")#وارد کردن متن رمز نگاری شده
        plan_text=""
        for c in encrypted_text:
            x = (ord(c)-2)//5 #تبدیل متن رمز نگاری شده به کد اسکی و تبدیل به متن ساده همزمان
            plan_text+=chr(x)
        print("plan_text: ",plan_text) #چاپ متن ساده
        print("*"*40+"\n")

    elif ch=="3": #پایان حلقه بی نهایت
        print("See you!")
        break

    else:
        print("Wrong!")# وارد کردن درخاست اشتباه
        print("*" * 40 + "\n")