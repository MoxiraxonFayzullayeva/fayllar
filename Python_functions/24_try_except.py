# ____________________________________________TRY EXCEPT________________________________________________

# ta'rif:

# avvalgi darslarda xatoliklar korib chiqqan edik, pythonda nom berilgan xatoliklarga yo'l qoyganimizda dastur ishlab turishini 
# ta'minlovchi operatorlar hisoblanadi

# ishlab turgan xatolik chiqishi mumkin bo'lgan kodni try ga yozamiz agar xatolik chiqsa nima ishlasin degan kodni exceptga yozamiz 
# (huddi if, elif, else ga o'xshab ishlaydi) eng qizig'i try_except ichida if, elig, elseni ham ishlatsa bo'ladi

# ko'ramiz:

# age =input('Yoshingizni kiriting: ')
# age = int(age)
# print(f"Siz {2024-age}-yilda tug'ilgansiz")

# yuqoridagi input string malumot qaytaradi, huddi shuni try exceptga yozib xatolik qaytarganini to'g'irlaymiz



# age =input('Yoshingizni kiriting: ')
# try: # biz operatorlarni to'liq yozmagunimizcha xatolik qaytarib turovradi,
# # masalan kodlarni to'gri kiritsak ham try ni yozib except bilan tugatmasak bizga xatolik qaytaradi
#     age = int(age)
#     print(f"Siz {2024-age}-yilda tug'ilgansiz")
# except:
#     print("Siz butun son kiritmadizngiz.") # try shartga kirsa bo'ldi except ishlamaydi

# try except else ko'rib chiqamiz

# age =input('Yoshingizni kiriting: ')
# try:
#     age = int(age)
# except:
#     print("Siz butun son kiritmadizngiz.")
# else:
#     print(f"Siz {2024-age}-yilda tug'ilgansiz") # else try ga padderjka qiladi

# agar biz kiritgan qiymat integerga konvertatsiya bo'lsa else ham ishlaydi degani (ya'ni try ga kirdimi else ga ham ishlaydi, else ga ham kiradi degani)
# exceptga kirdimi demak ishlamaydi chunki try ga kirgan xatolik qaytargan demak else ga ham kirmaydi degani


# ma'lum turdagi xatoliklarni ishlash uchun qanaqa qilinadi? (masalan manga manashu xatoliklar qaytsagina shunda ishlasin degan narsa bo'ladi)

# MA"LUMOT TURIDAGI XATOLIKLAR
# # ValueError:
# age =input('Yoshingizni kiriting: ')
# try:
#     age = int(age)
# except ValueError: #faqat manashu xatolik turiga ishlaydi
#     print("Siz butun son kiritmadizngiz. Yoki siz butun son kiritganingizda xato ravishda kiritdingiz.")
# else:
#     print(f"Siz {2024-age}-yilda tavallud topgansiz, topdimmi🤗")


# ZeroDevisionError

# a, b = 5, 10
# try:
#     b/(a-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi.")

# IndexError:

# fruit = ['apple', 'orange', 'banana', 'lemon']
# try:
#     print(fruit[5]) # indekslar bilar murojaat qilganimizda 0 dan boshlab sanaydi, bunda bizni savatimizda 6 ta meva bo'lishi kerak
# # chunki 5 indeksni so'raganimizda bizga 6-mevamizni yani oxirgi mevamiznichiqarib berardi
# except IndexError:
#     print(f"Ro'yxatda {len(fruit)} ta meva bor. Xatolik: index bo'yicha listga kirishga imkon bo'lmaydi.")
# # uzunligi bo'yicha esa savatimizda nechta meva bo'lsa shuncha mevani chiqarib beradi

# KeyError:

# user = {
#     'username': 'otajonbozorboyer',
#     'status': 'CEO',
#     'gmail': 'otajonbozorboyev@gmail.com',
#     'phone': '+998912345678'
# }
# try:
#     print(f"Foydalanuvchi: {user['tel']}") # hozir biz user o'zgaruvchisini ichida yo'q kalitni so'raganimiz uchun bizga except qaytaradi
#     print(f"Foydalanuvchi: {user['status']}") # hozir biz user o'zgaruvchisini ichida bor kalitni so'raganimiz uchun bizga shu kalit qiymatini ekranga chiqarib beradi
# except KeyError:
#     print("Bunday kalit mavjud emas") 

# FileNotFoundError
# file = 'imtihon.txt'
# try:
#     f = open(file)
# except FileNotFoundError:
#     print(f"Fayl {file} mavjud emas.") # bizni papkamizdagi barcha filelar python file bo'lganligi uchun ya'ni text korinishidagi imtihon degan fileimiz yo'qligi uchun shartdan o'tmay exceptga kiradi 

# Hozirgi ko'rganlarimizda bittxatoni ushlab ko'rib ketyapmiz, endi birnechta xatolikni ushlab ko'rib ketamiz

# a = input("Butun son kiriting: ")
# try:
#     a = int(a)
#     b = 20/a
# except ValueError:
# # except ValueError or ZeroDivisionError:
# # except [ValueError, ZeroDivisionError]:
#     print("Butun son kiritmadingiz.")
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi.")
# else:
#     print(f"B {b}")
#     print(f"A: {a}") # try ga kirsa else ham ishlaydi

# print(b) # try da printni try tagigan yozsa ham natija chiqaveradi (mantiqan if ga o'xshatishimiz sal notog'ri bo'ladi)
# # try ichida ochilgan o'zgaruvchi globalnimi localniymi degan savolga qo'rqmasdan globalni deb javob berib ketsak bo'ladi


# Xatolarni oldini olish


# yosh =input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
#     print(f"Siz {2024-yosh} yilsiz...")
# except:
#     print("Butun son kiritmadingiz")


# while True:
#     yosh =input("Yoshingizni kiriting: ")
#     if yosh.isdigit(): # isdigit() degani raqammi/sonmi degani
#         yosh = int(yosh)
#         break
# print(f"Siz {2024-yosh} yilsiz...")

# while True:
#     number = input("Butun son kiriting: ")
#     try:
#         number = int(number)
#         print(f"Siz {2024-number} yilsiz...")
#         break
#     except ValueError:
#         print("Butun son kiritmadingiz. Iltimos butun son kiriting!")

# _____________________________UY VAZIFALARI_______________________________________________________


# ______________1_____________


# 1-usul
# while True:
#     harf = input("Harf kiriting: ")
#     try:
#         if harf == int(harf):
#             continue
#     except:
#         print(harf.upper())
#         break
# #    else:
# #       print("Siz harf kiritmadingiz. Iltimos harf kiriting!")

# 2-usul
# while True:
#     harf = input("Harf kiriting: ")
#     try:
#         if harf == int(harf):
#             print("Siz harf kiritmadingiz. Iltimos harf kiriting!")
#             continue
#     except:
#         print(harf.upper())
#         break

# ________________2______________

# 1-usul

# while True:
#     son = input("Son kiriting: ")
#     try:
#         son = int(son)
#         print(son)
#         break
#     except:
#         print("Son kiritmadingiz. Iltimos son kiriting!")

# 2-usul

# while True:
#     try:
#         son = int(input("Son kiriting: "))
#         print(son)
#         break
#     except:
#         print("Son kiritmadingiz. Iltimos son kiriting!")







