# _________________________________INPUT___________________________

# input() o'zgaruvchiga ochilib qiymat berilmasa printda ma'lumot kiritilishini kutadi

# ism = input() # input defold holati string ma'lumot qaytaradi
# print(ism)

# ism = input("ismingizni kiriting: ") # kiritish yoki kiritmaslik majburiy emas
# print(ism)

# agar son kiritilsa string ma'lumot bo'lib qoladi, yuqorida input() string malumot qaytarishini aytib o'ttik
 
# son kiritilganda son qaytarilishi uchun input oldidan integer qoyib yozamiz
# ism = int(input("Son kiriting: ")) 
# print(ism)

# ism = input("ismingizni kiriting: ")
# print(type(ism))
# print(ism.capitalize())
# print(ism.title())
# print(ism.lower())
# print(ism.upper())

# _______________________________________\n____\t________________________
# printda \n va\t degan narsa bor bu 

# \n back slash (n)
# printda indekslar orasida \n ko'rinishida ochilsa o'zidan keyingi indeksni pastma pastga tushirib beradi

# \t back  sslash (t)
# printda indekslar orasida \t ko'rinishida ochilsa o'zidan keyingi indeksni orasini 4 ta (Tab) qilib beradi yani orasiga 4 ta probel qoyib beradi

# print("Assalomu\talaylkum")
# print("Assalomu\nalaylkum")
# __________________________________________end=____________________________
# pastma past ochilgan printda qavs yopilishidan oldin \n funksiyasi ishlab turgan boladi
# uni o'chirish qavsdan oldin print(....., end=" ")(qo'shtirnoqli yoki birtirnoqli ikkalasi ham bo'ladi)
# ochilsa shunda pastdagi print tepadagi print oldiga o'tadi(agar qo'shtirnoqlar orasiga probel qoyilmagan bo'lsa bir qatorda yopishib qoladi) 
# print("Mohiraxon", end=" ")
# print("Mohiraxon", end='')
# print("Mohiraxon", end=" ")
# print("Mohiraxon") #oxiriga qo'yilmasa bo'ladi chunki undan keyin boshqa printyoq


# __________________________________________and|or_________________________________________


# and = *|& #ma'lumotlar binariga o'tqazilganda ularning ko'paytmasi 0 ga teng kelib qolsa olinmaydi, ma'lumot qabul qilmaydi
# or = /|+ #ma'lumotlar binaryga o'tlkzilganda ularning yigindisi 1 ga teng kelib qolsa olinadi, ma'lumot qabul qilinadi
# and-da agar hamma ma'lumot binarida 1 bo'lib bittasi 0 bolib qolsa false qaytaradi
# or-da agar hamma ma'lumot binarida 0 ga teng bo'lib bittasi 1 ga teng bolib qolsa true qaytaradi
# bular kiritilganlarni binariga o'tkazib beradi

# print('a' in 'asdsaqwer' and 'g' in 'qawertyuik' and 'p' in 'gfdsazxcvbnm' ) #False
# print('a' in 'asdsaqwer' or 'g' in 'qawertyuik' or 'p' in 'gfdsazxcvbnm' ) #True

# in = ichida bormi 
# not in = ichida yo'qmi

# and = *|&
# or = /|+

# 00000000110 # 6
# 00000000111 # 7
# 00000000110 # 6
# 00000000111 
# >> << - shift 

# 00000000110 #6
# # 7 >> 2 # oldinga ikta surib beradi
# 00000011000 #6
# # 7 << 2 #orqaga ikta surib beradi
# 00000000110 #6


#___________________________________integers - int_____________________________________

# a = 20
# b = 50
# c = a+b
# print(c)

# kv = 2**3
# print(kv)

# Float - float
# pi = 3.1415926535
# radius = int(input("Aylana radiusini kiriting: ")) # agar int yozilib ketilmasa input stringda chiqib xatolik qaytaradi
# diametri = 2*radius
# print(f"Aylanana uzunligi {pi*diametri} ga teng.")

# aholi = 38_000_000 # bankoviy schotlarda raqamlarni 3 tadan qilib ajratadi adashib ketmaslik uchun, dasturda biz tagchiziqdan foydalanamiz
# print(aholi)

# _________________________________KONSTANTA________________________________________

# pi = 3.1415926535
# konstanta - bu o'zgarmas qiymat pi = konstanta qiymat ekan

# o'zgaruvchilarni elon qilishni boshqacha usuliham bor 
# a,b,s,d = 1,2,3,4 # nechta o'zgaruvchi bo'lsa shuncha qiymat kiritishimiz kerak bir qatorda

# ism = "zubayr"
# yosh = 25
# info = ism.capitalize() + " " + str(yosh)+" "+"yoshda."
# info2 = ism.capitalize(),str(yosh),"yoshda."
# print(info) 
# print(info2) 
# print(type(info))
# print(type(info2))

# typecasting tipini o'zgartirib beradi ya'ni integerni stringga stringdan integerga integerdan floatga floatdan integerda stringga 
# qisqasi - Typecasting - bu data typeni o’zgartirib qabul qildirish

# ___________________________________boolean__________________________________________

# boolean - bool

# print(10 > 9) #true
# print(10 < 9) #false
# print(10 == 9) #false
# print(10 != 9) #true
# print(10 >= 9) #true
# print(10 >= 9) #true
# # print(10 >> 9) #true
# # print(10 << 9) #true

# _____________________________________SINF ISHI__________________________________

# ___________________________________________1_______________________________________


# Mening ismim Moxiraxon. Yoshim 20 da. Sirdaryo viloyatidanman.
# a = input("O'zingiz haqingizda ma'lumot kiriting: ")
# print(len(a))

# a1 = input("O'zingiz haqingizda ma'lumot kiriting: ")
# a2 = len(input("O'zingiz haqingizda ma'lumot kiriting: "))
# print(type(a1), type(a2)) 


# __________________________________________2______________________________________

# Foundation
# matn = input("Ma'lumot: ")
# matn = Foundation
# print(matn[:].lower(),'\n', matn[4::-1].lower(),'\n', matn[-1:3+1:-1])

# _____________________________________________3______________________________________

# soz = ('kompyuter', 'sichqoncha', 'ruchka', 'telefon')
# soz2 = soz[0]
# soz3 = soz[-1]
# print(soz2, soz3)
# print(soz[0].replace(soz2, soz3), soz[-1].replace(soz3, soz2))

# qwertyu
# soz = ['kompyuter', 'sichqoncha', 'ruchka', 'telefon']
# soz[0] = 'telefon'
# soz[-1] = 'kompyuter'
# print(*soz)



# ____________________________________UYGA VAZIFA________________________________________

# _________________________________________1__________________________________________

# pi = 3.1415926535
# radius = int(input("Radiusni kiriting: "))
# print(f'Foydalanuvchi kiritgan radius asosida aniqlangan aylana maydoni {pi*radius} ga teng.')


# _______________________________________2__________________________________________________


# son = int(input("Son kiriting: "))
# print(f"""
# {son} x 1 = {son*1}
# {son} x 2 = {son*2}
# {son} x 3 = {son*3}
# {son} x 4 = {son*4}
# {son} x 5 = {son*5}
# {son} x 6 = {son*6}
# {son} x 7 = {son*7}
# {son} x 8 = {son*8}
# {son} x 9 = {son*9}
# {son} x 10 = {son*10}
# """)


# _______________________________________3___________________________________



# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# print(f'Foydalanuvchining kiritgan ma\'lumotlariga ko\'ra u {2024-yil} yoshdaligi aniqlandi.')


