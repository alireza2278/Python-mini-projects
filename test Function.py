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
# پیاده سازی کار داخلی len توسط len2
# def len2(x):
#     i = 0
#     for _ in x:
#         i+=1
#     return i
# a = input("enter: ")
# print(len2(a))
#-----------------------------------------------------------------
#پیاده سازی کار تابع داخلی max یا min
# def max2(*args):
#     m = args[0]
#     for i in args:
#         if i > m:
#             i = m
#     return m
#
# print(max2(1,99,70,100,36))
#--------------------------------------------------------------------
# #پیاده سازی تابع داخلی sum
# def sum2(it):
#     x=0
#     for i in it:
#         x+=i
#     return x
#
# print(sum2([1, 99, 70, 100, 36]))
#---------------------------------------------------------------------
#تابع تشخیص مربع بودن یا نبودن یک عدد
# def aquare():
#     z=int(input("Enter number: "))
#     for i in range(1,z):
#         if i**2 == z:
#             print(f"yes :) {i} * {i} = {z}")
#             break
#     else:
#             print("no!")
# aquare()
#------------------------------------------------------------------
#تابع محاسبه قیمت کالا همراه تخفیف
# def price(price,discount_percent):
#     discount_rate = int(price * discount_percent / 100)
#     new_price = price - discount_rate
#     print("price",price)
#     print("Discounted price",new_price)
#
#
# price1 = float(input("Enter price: "))
# discount_percent = float(input("Enter discount percent: "))
# price(price1,discount_percent)
#-------------------------------------------------------------------
 # مشخص شدن نوع یک کاراکتر
# def func(ch):
#     if 48<=ord(ch)<=57:
#         print("your character is a number!")
#     elif 65<=ord(ch)<=90:
#         print("your character is a capital letter!")
#     elif 97 <= ord(ch) <= 122:
#             print("your character is a small word!")
#     else:
#         print("other!")
#
# c = input("Enter the char: ")
# func(c)
#--------------------------------------------------------------------
#تشخیص تعداد زوج و فرد یک لیست با نوشتن دو تابع lambda
# ls = [1,2,3,4,5,6,7,8,9,10,22,66,31,51,33]
# print("list:",ls)
# fard = len(list(filter(lambda x:x%2!=0,ls)))
# zogh = len(list(filter(lambda x:x%2==0,ls)))
# print(f"tedad zogh: {zogh} \ntedad fard: {fard}")
#--------------------------------------------------------------------
# # مرتب کردن تاپل های داخل لیست بر اساس اعداد
# ls = [("Reza",65),("Ali",93),("Sasan",42)]
# print(ls)
# ls.sort(key=lambda x:x[1])
# print(ls)
#-------------------------------------------------------------------
# #مرتب کردن دیکشنری بر اساس رنگ میوه ها
# ls = [{"name":"apple","weight":50,"color":"red"},
#       {"name":"banana","weight":60,"color":"yellow"},
#       {"name":"orange","weight":20,"color":"orange"},
#       {"name":"coconut","weight":35,"color":"brown"}
#       ]
# print(ls)
# ls.sort(key=lambda x:x["color"])
# print("sorted list:",ls)
#--------------------------------------------------------------------------
#جدا کردن زوج و فرد یک لیست
# ls = [1,2,3,4,5,6,7,8,9,10,22,66,31,51,33]
# print("list:",ls)
# fard =list(filter(lambda x:x%2!=0,ls))
# zogh =list(filter(lambda x:x%2==0,ls))
# print(f" zogh: {zogh} \n fard: {fard}")
#---------------------------------------------------------------------
#تبدیل اعداد به مربع و مکعب
# ls = [1,2,3,4,5,6,7,8,9,10,22,66,31,51,33]
# print("list:",ls)
# moraba =list(map(lambda x:x**2,ls))
# mokhab =list(map(lambda x:x**3,ls))
# print(f"moraba{moraba}\nmokab{mokhab}")
#-------------------------------------------------------------------
#تشخیص حرف اول رشته ک آیا حرف مد نظر ما بوده است با شرط های داخل lambda
# s = "reza"
# starts_with = lambda s: True if s.startswith("a") else False
# print(starts_with(s))
#--------------------------------------------------------------------
#تشخیص عدد بودن یک رشته یا عدم آن
# s = "4.5"
# is_num = lambda s:s.replace(".","",1).isdigit()
# print(is_num(s))
#---------------------------------------------------------------









