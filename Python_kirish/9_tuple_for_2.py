
# ____________________________________________FOR_______________________________________________

# For - asosan (Iterable: str, list, tuple, set, dictionary)  bilan ishlidi

# ya'ni stringni ichidagi, listni ichidagi, tupleni, setti, dictionaryni ichidagi qiymatlarni aylantirsa ishluradi

# for ichida for ishlatish:

# ism = ['moxira', 'sitora', 'sevinch', 'asal']
# for i in ism: #ismdagi indekslarni o'qib chiqadi
#     for j in i: #ismdagi indekslar i ga o'tib qolgan edi ularni aylantirib chiqadi
#         print(j)
#     print(i.title()) #ichidagi qiymatlar string bo'lsa title() capitalize() ishlatib ketish mumkin

# son = list(range(0,11))
# for i in son:
#     print(f"{i} ning kvadradi {i*i} ga teng")
#     print(f"{i} ning kvadrati {i**2} ga teng")

# optimalroq variantda list ochmasdan turib ham range() ni o'zida sonlarni aylantirsa bo'ladi:

# for son in range(11): # bittadona kiritilgan qiymatning o'zi chegarani bildiradi
#     print(f"{son} ning kvadrati {son**2} ga teng") # xotiradan yutamiz

# for s in range(0, 11): # (start, end, step)ni o'tgan edik
#     print(f"{s} ning kvadrati {s**2} ga teng") # xotiradan yutamiz

# for n in range(0, 11, 2): # kiritilgan step bo'yicha faqat juft solarni kvadratini olib beradi
#     print(f"{n} ning kvadrati {n**2} ga teng") # xotiradan yutamiz

# for o in range(1, 11, 2): # kiritilgan step bo'yicha faqat toq solarni kvadratini olib beradi
#     print(f"{o} ning kvadrati {o**2} ga teng") # xotiradan yutamiz

# numbers = list(range(11))
# sonkv = []
# for i in numbers:
#     sonkv.append(i*i) #bitta qiymatti boshqa o'zgaruvchiga o'zlashtirib beradi
# print(sonkv)  

# cars = []
# for i in range(5): #nechta mashina kiritish
#     cars.append(input(f"{i+1}-mashinani kiriting")) #foydalanuvchi kiritgan narsalar cars o'zgaruvchisiga o'zlashtiriladi
# print(cars)


# cars = []
# for i in range(int(input("Nechta mashina kiritmoqchisiz: "))): # foydalanuvchi nechta mashina kiritishi
#     cars.append(input(f"{i+1}-mashinani kiriting: ")) #foydalanuvchi kiritgan narsalar cars o'zgaruvchisiga o'zlashtiriladi
# print(cars)


# ism = input("Ismingizni kiriting: ")r
# for i in range(int(input("Ismingiz nechi marta chiqsin: "))):
#     print(f"{i+1}. {ism.title()}.")

# foydalanuvchi kiritgan chegaragacha sonlarni o'suvchi tartibda chiqaramiz

# for x in range(int(input("Chegarani kiriting: "))+1):
    # print(x, end=" ")


# ______________________________________SINF ISHI_____________________________________

#___________________________________________1_________________________________________

# person = ('Amir Temur', 'Alisher Navoiy', 'Al-Buxoriy', 'Ibn Sino', 'Imom Muslim')
# for tarix in person:
#     print(f"Allomalar muzeyi (Xiva) - muzey \"Ichan qal'a\" davlat muzey-qo'riqxonasidagi 1765-yilda qurilgan Muhammad Amin inoq madrasasida joylashgan."
#           f"Muzeyda Xorazm Ma'mun akademiyasi tarixi, akademiyada faoliyat yurishgan olimlarning asarlari, ularning ilmiy merosi o'rin olgan."
#           f"Muzeyda O'rta Osiyolik buyuk allomalar masalan: {tarix}ning nodir asarlari o'rin olgan.\n\n")


# __________________________________________2___________________________________________

# country = ('Malayziya', 'BAA', 'Sadudiya Arabistoni', 'Qatar', 'Quvayt')
# for shahar in country:
#     print(f"Islom dunyoda tarqalishi bo'yicha ikkinchi o'rinda turadigan dindir, 1,8 milliardan ortiq kishi Islom dininga e'tiqod qiladi."
#           f"Faqatgina 18% foiz musulmonlar arab davlatlarida yashaydi. Asosiy aholisi Islom diniga e'tiqod qiladigan davlatlar soni 30 dan ortiq bo'lsa ularning biri {shahar}dir.\n\n")


# ( 'BAA', 'Sadudiya Arabistoni', 'Qatar', 'Quvayt')
# country = []
# for shahar in range(5):
#     country.append(input("Mamlakat nomini kiriting: "))
#     print(f"Islom dunyoda tarqalishi bo'yicha ikkinchi o'rinda turadigan dindir, 1,8 milliardan ortiq kishi Islom dininga e'tiqod qiladi."
#           f"Faqatgina 18% foiz musulmonlar arab davlatlarida yashaydi. Asosiy aholisi Islom diniga  e'tiqod qiladigan davlatlar soni 30 dan ortiq bo'lsa ularning biri {country}dir.\n\n")



# __________________________________________3_____________________________________________


# for kub in range(0, 100, 2):
#     print(f"{kub} ning kubi {kub**3} ga teng")

# _____________________________________UYGA VAZIFA__________________________________________

# _________________________________________1_______________________________________________

# country = []
# for i in range(5):
#     country.append(input("Yoqtirgan mamlakatingizni kiriting: "))
# print(country)

# __________________________________________2___________________________________________________


# cars = []
# for c in range(5):
#     cars.append(input("Yoqtirgan mashinangizni kiriting: "))
# print(tuple(cars))

# __________________________________________3_____________________________________________________




# ____________________________________________4_____________________________________________________


# for i in range(int(input("Nechta odam bilan ko'rishdingiz: "))):
#     print(input(f"{i+1}-odam ismini kiriting: ").title())

# ________________________________________________5_________________________________________________

# kishi = ('Teacher A\'zam', 'Teacher Ismail', 'Marifat Jamal')
# for i in kishi:
#   print(f'Hayrli kun hurmatli {i}. Sizni ijodizni hurmat qilaman. Olib chiqayotgan podcastlaringiz juda manfaatli. Omad!') 

























