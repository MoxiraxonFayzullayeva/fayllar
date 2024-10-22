# _______________________Dict ichida for orqali aylantirib o'tish_______________________________________


# phones = {
#     'Alimjon': "iphone 16",
#     "Rahmatilla": "iphone 16 pro max",
#     "Moxira": "redmi",
#     "islom": "samsung" 
# }

# for i in phones: # for i in phones.keys() -> ikkalasi bitta narsa 
#     print(i) # keylar bilan aylantirib beradi


# for i in phones.values():
#     print(i) # values bilan aylantirib beradi


# for key, value in phones.items():
#     print(key, value) # items -> qiymatti o'z holicha olib chiqadi shuning uchun ikta o'zgaruvchi ochilinadi


# phones = {
#     'iphone 15': 800,
#     'iphone 14': 600,
#     'galaxy 24': 1_500,
#     'redmi': 400,
#     'iphone 13': 650
# }

# # telefonlar = ['iphone 15', 'iphone 14', 'redmi']

# # for i in phones:
# #     if i in telefonlar:
# #         print(f'{i} $ {phones[i]}.')


# for i in sorted(phones.values()):
#     print(i)

# for i in sorted(phones.keys()):
#     print(i)

# for i in sorted(phones.items()):
#     print(i)


# cellphones = {
#     'Otajon': 'iphone 15',
#     'Otabek': 'iphone 14',
#     'Sardor': 'iphone 11',
#     'Orif': 'redMi',
#     'lola': 'iphone 15',
#     'sakina': 'iphone 14',
#     'sitora': 'iphone 11',
#     'moxira': 'samsung 24'
# }


# print("Foydalanuvchilarning telefonlari: ")
# for i in cellphones.values():
#     print(i)

# for i in set(cellphones.values()):
#     print(i)


# copy() -> birorta bo'sh dict.ga nusxalab beradi
# del() 
# clear()
# popitem()

# car1 = {
#     'made': 'bmw',
#     'model':'x7',
#     'year': 2023
# }
# car2 = {
#     'made': 'mercedes',
#     'model':'220',
#     'year': 2024
# }
# car3 = {
#     'made': 'ferrari',
#     'model': 'la ferrari',
#     'year': 2025
# }

# cars = [car1, car2, car3]

# # for i in cars[2].values():
# #     print(i, end=' ')


# print(cars[2].values())

# ______________________________________SINF ISHI__________________________________


#_____________________________________________sinf ishi 1_______________________________________________

# family = {'otam': 'abduxalil',
#         'onam': 'adolat',
#         'akam': 'muhammadali',
#         'opam': 'nisoatxon',
#         'singlim': 'kimyoxon'
# }
# for i in family.values():
#     print(f'Assalomu alaykum hurmatli {i.title()} men sizni Mustaqillik bayrami munosabati bilan tabriklamoqchiman.')

#_______________________________________________sinf ishi 2_____________________________________________

# favourite = {'ismigul': 'BMW', 'odina': 'Mercedes', 'sevinch': 'malibu', 'kumush': 'gentra', 'muyassar': 'nexia'}
# cars = ['ismigul', 'kumush', 'odina']
# for i in favourite:
#     if i in cars:
#         print(f'{i.title()}ning yaxshi ko\'rgan mashinasi {favourite[i].upper()}.')


# _____________________________________________ sinf ishi 3______________________________________________

# sinfishi = {
#     'boolean()': ['to\'g\'ri yoki Noto\'g\'riga', 'ha yoki yo\'q', '1 yoki 0 ga javob beradi'],
#     'int()': ['integer bizga butun sonlarni qaytaradi'],
#     'float()': ['float esa bizga o\'nlik son ko\'rinishida chiqarib beradi'],
#     'str()': ['matnlarga javobberadi'],
#     'if elif else': ['taqqoslash va tekshirish operatori hisoblanadi', 'if va else birmarta celif esa istagan marta ishlatilinadi'],
#     'list()': ['list elementlar uchun xotiradan qo\'shimcha joy ochib boradi'],
#     'tuple()': ['tuple ichidagi elementlarni o\'zgartirib bo\'lmaydi'],
#     'set()': ['indekslanmagan bo\'ladi va dublikatlarni qabul qilmaydi'],
#     'dict()': ['indekslanmagan ammo tartiblangan bo\'ladi', 'keyga murojaat qilish orqali uning valuesini chiqara olamiz'],
# }

# for kalit, qiymat in sinfishi.items():
#     print(f"\n{kalit}:", end=' ')
#     for i in qiymat:
#         if i == qiymat[-1]:
#             print(f'{i.capitalize()}', end='.')
#         else:
#             print(f'{i.capitalize()}', end=". ")
#             pass


#_______________________________________________sinf ishi 4______________________________________________

# cars = {
#     'nomi': 'bwm',
#     'modeli': 'dm-1',
#     'engine': 'automatic',
#     'color': 'pushti',
#     'narx': 20_000
# }
# user = cars.get(input("So'rang: "), 'Bunday ma\'lumot mavjud emas!' )
# print(user)












