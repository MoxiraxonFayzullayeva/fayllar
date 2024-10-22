# _________________________LAMBDA / MAP / FILTER _______________________________________

# LAMBDA

# lambda => nomsiz funksiya

# lambda argument: ifoda #ko'rinishida yoziladi (argument => o'zgaruvchi), (ifoda => qiymat)
# misol:

# lambda a, b: a + b # ikki nuqtagacha bo'lgan jarayondagi a va b larni o'zgaruvchilar deb olsak,
# ikki nuqtadan so'nggi jarayonda a va b o'zgaruvchilar nimani amalga oshirishi haqida kiritamiz 
# qo'shish bo'lsa qoshish, ko'paytirish bo'lsa ko'paytirish va hakozo

# daraja = lambda x, y: x**y
# print(daraja(2, 3)) # return lambdani ichiga kirib ketganligi sababli,
# huddi def funksiyadagi qiymat qaytaruvchi returnga o'xshab natijani printga chiqaramiz 

# print(daraja(x = int(input("A: ")), y = int(input("B: "))))


# def daraja(n): # n ham qiymat qabul qiladi
#     return lambda x: x**n # x ham qiymat qabul qiladi
# # n uchun berilgan qiymatlar
# kvadrat = daraja(2)
# kub = daraja(3) 
# # x uchun berilgan qiymatlar
# print(kvadrat(2))
# print(kub(2))


# print(True+True*True) # Truening defold holati 1 ga teng bo'lsa matematik amallarda avval ko'paytirish
#  keyin qoshish bajariladi
# print(1+1*1) # Natija ikkalasida ham bir xil 2 chiqadi


# map() filter() #doim qavs bilan yoziladi
# map() #hammaga teng taqsimlab beradi
# filter() # qaysidir shartdan o'thanlarnigina oladi

# from math import sqrt #ildizlarnigina chiqarib beradi
# numbers = list(range(11))
# ildizlar = list(map(sqrt, numbers)) #map ichidagi qiymatarni tahlil qilamiz: 
# matematik kutubxonadan chaqirgan ildiz (sqrt) finksiyamiz bo'yicha
# # number ichidagi rangedan foydalanib chaqirgan 10 ta sonlarimizni ildizlarini map orqali natijasini chiqardik
# print(ildizlar)


# a, b = map(int, input('Son: ').split()) #foydalanuvchi kiritgan ma'lumotni map()dan foydalanib
# # bir xil taqsimlab berib intejer tipiga kanvertatsiya qilib printdagi matematik amalni bajardik
# # split() bizga foydalanuvchi A va B o'zgaruvchilar uchun kiritgan ma'lumotlar oraligidagi
#  bo'shliqni chopib berish uchun ishlatilindi
# print(a + b)

# o'zbekcha litcode ROBOCONTEST da birinchi masala map orqali o'zgaruvchilarga beriladigan qiymatli
# amaliyotlar bajarilsagina qabul qiladi
# masalan:
# a, b = map(int, input('Son: ').split()) 
# print(a + b)

# a = int(input("A: "))
# b = int(input("B: "))
# print(a + b)


# number = list(range(11))
# def daraja(n): #darajaga kiritilgan qiymat number dan olingan
#     return n*n
#     # return n*2
# print(list(map(daraja, number)))

# number = list(range(11))
# kv = list(map(lambda a: a*a, number)) 
# print(kv)
# kv1 = list(map(lambda a: a*a, range(11)))
# print(kv1)
#lambdada forga o'xshab sikl aylanadi a -> 
# -> number o'zgaruvchisidagi har bir element ichiga kirib chiqadi

# # lambda orqali qilgan ishimizni for da ko'rib ketamiz
# __________ -1
# number = list(range(11))
# kvadratlar = []
# for i in number:
#     kvadratlar.append(i*i)
#     # kvadratlar.append(i**2)
# print(kvadratlar)

# _____________ -2
# for i in range(11):
#     print(i*i, end=" ")

# bir = [1, 2, 3]
# ikki = [1, 2, 3]
# uch = list(map(lambda i, o: i+o, bir, ikki, )) # ikki o'zgaruvchidagi elementlarni bir xil indeksi bilan hisoblab chiqarib beradi
# print(uch)


# bir = [1, 2, 3]
# ikki = [1, 2, 3]
# qoshimcha = [1, 2, 3, 4]
# uch = list(map(lambda i, o, u: i+o+u, bir, ikki, qoshimcha)) # agar o'zgaruvchilarning biri ichida 1 da indeks ko'p bolsa unda shu indeksni olmaydi(chopadi)
# print(uch) 

# names = ['odinaxon', 'alimjon', 'madina', 'saidaxon']
# print(list(map(lambda i: i.upper(), names))) # lambdada string metodlarini ham amalga oshirsa bo'ladi


# # def funksiyasi ichida filter chaqirish
# import random as r
# sonlar = r.sample(range(100), 10) # random orqali 100 gacha bolgan sonlarni faqat 10 tasini aniqlab berdi
# def juft(x): 
#     return x % 2 == 0 # tanlangan 10 ta son ichida juft sonlarnigina ekranga chiqarib beradi
# juft_sonlar = list(filter(juft, sonlar)) # def funksiyasidagi juft(x) uchun qiymat random orqali tanlab olingan 10 ta raqamdan berildi
# # va ichida qoldigi 0 gateng bo'lganlarni tanlab  juft_sonlar o'zgaruvchisiga o'zlashtirildi
# print(sonlar)
# print(juft_sonlar)



# names = ['ali', 'odinaxon', 'alimjon', 'madina', 'saidaxon']
# print(list(filter(lambda x: x.startswith('ali'), names))) # startswith() ichida qanday shart berilsa shu shartga javob berganlarnigina chiqarib beradi
# # list 1 ta argumant qabul qiladi -> filterbi bitta argument sifatida qaraydi 
# filter ichida shart -> lambda, lambdaga berilgan x uchun qiymat namesdan olinadi 
# print(list(filter(lambda x: len(x) > 6, names


# misol:

# import random as r
# print(list(filter(lambda x: x % 2 == 0, r.sample(range(100), k = 15))))
# 1 dan 100 aylangan sonlar ichida  15 tasini tanlab ichidan faqatgina qoldiqsiz bo'linganlarnigina chiqarib berdi


# Recursive function 

# def teskari(son):
#     if son == 0:
#         return
#     print(son, end=' ')
#     teskari(son - 1)

# def togri(son):
#     if son == 0:
#         return
#     togri(son + 1)
#     print(son, end=' ')

# teskari(5)
# print()
# togri(5)


# ____________________________________UYGA VAZIFA_________________________________________
# __________________1________________

# lmda = lambda x: x * 10
# print(lmda(3))

# __________________2________________


# yigindi = lambda x, y: x + y
# print(yigindi(2, 3))


# ________________3 / 4 / 5________________

# import random as r
# print(list(map(lambda a: a, r.sample(range(100), 10))))
# # print(lambda a: a, r.sample(range(100), 10))


# print(list(map(lambda x: x ** 2, r.sample(range(100), 20))))



# print(list(filter(lambda x: x % 2 == 0, r.sample(range(100), k = 20))))




















