# ___________________________________________________DEF______________________________________


# FUNKSIYALAR - FUNCTIONS


# def funksiyasida bir marta kodlarni yozvolamiz va dastur davomida coddi chaqirib chiqamiz kerakli joyda
# funksiya eng ko'p qollaniladigan vosita

# e'lon qilinishi:
# def deb ochilib o'zgaruvchilarganom berilganidek nom beriladi kichik harflarda, va oxirida () qo'yiladi, ikki nuqta qo'yiladi
# qavs ichida xozircha xechnarsa yozmimiz

# def salom():  # qiymat qabulqilmaydigan
#     print("Assalomu alaykum.")

# kod yozdik endi buni chaqiramiz:

# salom() #agar komenteriyaga olib qoysak dastur o'qiydi lekin toxtatib qoyadi ekranga chiqarmaydi
# istagancha chaqirish mumkin
# salom()
# salom()
# salom()

# funksiya chaqirganimizda, argument kiritmasak, lekin chaqirganimizda argument bersak xatolik qaytaradi

# def salom():
#     print("Assalomu alaykum.")
# salom("Moxiraxon.") #xatolik chaqiradi

# agar fuknsiyada qavs ichiga argument berib o'tsak, chaqirganimizda qavs ichiga biror narsa yozsak chiqarib beradi


# qiymat qabul qiladigan:

# def salom(ism): #bunda int() yoki str() malumot bersak qabul qilaberadi 
#     print(f"Assalomu alaykum. {ism}")
# salom("moxiraxon.")
# salom(22)



# def salom(ism: str): # str() malumotni argument oldidan ikki nuqta qoyib chaqirganimizda string kalitlarini chiqarib beriladi 
#     print(f"Assalomu alaykum. {ism.capitalize()}") # agar string metodini berib lekin kodni chaqirganimizda integer malumot kiritsak xatolik qaytaradi

# salom("moxiraxon.".capitalize()) # kodni chaqirganimizda ham string metodini qollab ketsak boladi
# salom("moxiraxon.")
# # salom(22)

# agar argument berilib lekin kodni chaqirilganda qiymat kiritmasak xatolik qaytaradi
# def salom(ism):
#     print("Assalomu alaykum.")
# salom() #xatolik chaqiradi

# _DOC_ qo'shish

# def salom(ism): 
#     """Salom beruvchi function""" #dastur buni o'qiydi lekin ekranga chiqarmaydi kamentariyadek, (komentga obqoysayam bo'ladi, lekin doc str chiqmay qoladi)
#     print(f"Assalomu alaykum. {ism}")
# print(salom.__doc__)
# salom("moxiraxon.")
# # agar buni chiqarishni hohjlasak


# # bir nechta argument berish uchun:
# def ism_familiya(ism, familiya):
#     print(f"Assalomu alaykum {ism} {familiya}")

# ism_familiya('moxiraxon', 'fayzullayeva') 


# bundayam huddi tepada ko'rib chiqqan amallarimizni metodlarimizni qo'llasak bo'ladi

# def ism_familiya(ism:str, familiya:str):
#     print(f"Assalomu alaykum {ism.capitalize()} {familiya.capitalize()}")
# ism_familiya('moxiraxon', 'fayzullayeva') 


# def ism_familiya(ism:int, familiya:str):
#     print(f"Assalomu alaykum {ism.capitalize()} {familiya.capitalize()}") #string metod xatolik qaytaradi
# ism_familiya(20, 'fayzullayeva') 


# def ism_familiya(ism:int, familiya:str):
#     print(f"Assalomu alaykum {ism} {familiya}") #string metod qollanilmaganligi uchun xatolik qaytarmaydi 
# ism_familiya(20, 'fayzullayeva') 

# def  yosh_hisobla(ism: str, tyil): #str ni qoyish ixtiyoriy
#     print(f"{ism.capitalize()}ning yoshi: {2024-tyil} da.")

# yosh_hisobla('Moxiraxon', 2004) #standart qiymat berishi ham mumkin 
# yosh_hisobla(input("Ismingizni kiriting: "),
#             int(input("Yoshingizni kiriting: "))) # userdan ma'lumot kiritishni so'rash ham mumkin


# __________________________________standart qiymat___________________________________________________

# def ismi_yoshi(ism = 'moxiraxon', tyil = 2004): #standart qiymat berilgan
#     print(f"{ism.capitalize()}ning yoshi: {2024 - tyil} da.")

# # standart qiymat berilgan bo'lsa ham kodni chaqirganda boshqa qiymat berilsa shu berilgan qiymat ekranga chiqadi 
# ismi_yoshi('odinaxon', 2005)
# ismi_yoshi() #buni pustoy qoldirsa standart qiymat chiqadi
# ismi_yoshi(tyil = 2000) # standart ism olinadi yil o'zgaradi
# ismi_yoshi(ism='sarvinoz') # standart yosh olinadi ism o'zgaradi



# ______________________________________UYGA VAZIFA______________________________________________________


# ___________________1______________________________

# def ism_yosh(ism, yosh):
#     """Tugilgan yilingizni chiqaruvchi funksiya!"""
#     print(f"{ism.title()} - siz {2024-yosh}-yilda dunyoga kelgansiz.")
# print(ism_yosh.__doc__)
# ism_yosh(input("Ismingiz: "), int(input("Yoshingiz: ")))

# ___________________2______________________________


# def son(son: int):
#     print(f'{son} ning kvadrati {son ** 2} ga, kubi esa {son ** 3} ga teng.')
# son(int(input("Son kiriting: ")))


# ___________________3_________________________________


# def son(son):
#     if son % 2 == 0:
#         print(f"{son} - juft son.")
#     else:
#         print(f"{son} - toq son")
# son(int(input("Son kiriting: ")))

# _____________________4__________________________________

# def son(a, b):
#     print(a ** b)
# son(int(input("A uchun qiymat kiriting: ")), int(input("B uchun qiymat kiriting: ")))

# _______________________5____________________________________

# def son(a, b):
#     print(str(max(a, b)))
# son(int(input("A uchun qiymat kiriting: ")), int(input("B uchun qiymat kiriting: ")))


# _______________________6___________________________________


# def son(son):
#     for i in range(2, 10+1):
#         if son % i == 0:
#             print(i)
# #         else:
# #             continue
# son(int(input("Son kiriting: ")))        


















