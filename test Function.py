#شمارش تعداد تکرار یک عدد
#راه اول ریاضی
# def repead(number, digit):
#     cont = 0
#     while number>0:
#         if number % 10 == digit: #هر بار عددی باقیماندش به ده محاصبه شود رقم اخر ان باقی میماند
#             cont+=1
#         number//=10
#     return cont
#
# x = int(input("enter x : "))
# y = int(input("enter y : "))
# print(y,"repead",repead(x,y),"times")

#راه دوم استفاده از رشته
# def repead(number, digit):
#     return str(number).count(str(digit)) #متد .count برای شمارش رشته های برابر اولی در دومی
#
# x = int(input("enter x : "))
# y = int(input("enter y : "))
# print(y,"repead",repead(x,y),"times")
# #----------------------------------------------------------
# def fact(n):#تابع پیدا کردن فاکتوریل یک عدد
#     f = 1
#     for i in range(1,n+1):
#         f*=i
#     return f
# def sumFact(x): #تابع جمع زدن فاکتوریل یک عدد با فاکتوریل عدد های قبل آن
#     y = 0
#     for i in range(1,x+1):
#         y+=fact(i)
#     return y
# z = int(input("enter number: "))
# x = sumFact(z)
# print("sun",x)
#--------------------------------------------------------------
# def Max(): # تابع پیدا کردن بزرگ ترین عدد دریافتی
#     x = int(input("enter a: "))
#     y = int(input("enter b: "))
#     z = int(input("enter c: "))
#     print("max:", max(x ,y, z))
# Max()
#----------------------------------------------------------------