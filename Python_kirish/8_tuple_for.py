
# _________________________________________________TUPLE___________________________________________

# tuple o'zgaruvchida () qavs bilan ochiladi (biz listda [] qavsdan foydalangan edik)
# my_tpl = (12, True, 'matn', 5.9) # tuple ham hammasini qabul qiladi
# print(my_tpl[:2])

# list tez ishlaydimi tuple tez ishlaydimi deydigan bo'lsak albatta tuple tez ishlaydi deymiz
# 1. sababi list ochilganda xotiradan qo'shimcha joy olib ketaveradi/tupleda esa unaqa emas
# 2. listni o'zgartirsa bo'ladi (xotiradagi joyida turgan holatida)
# 3. tupleni asli qiymatini o'zgartirib bo'lmaydi (o'zgartirilsa ham yangi xotiradan joy egallab o'zgartiriladi)

# misollarda ko'rib chiqamiz

# my_list = [1, 2, 3, 4]
# my_list[0] = 25 
# print(my_list)
# my_tpl = (18, True, 'matn', 5.7)
# print(my_tpl[:2])
# my_tpl[0] = 25 #xatolik qaytaradi
# print(my_tpl)

# o'zgartirsa bo'lish holati

# mytpl = (18, True, 'matn', 5.9)
# # print(mytpl)
# # print(id(mytpl))
# mytpl = list(mytpl)
# mytpl.append('moxiraxon')
# mytpl.extend(['alimjon', 'rahmatilla'])  #hammasini id() si xarxil bo'ladi(tuple asli o'zgarmadi)
# # print(mytpl)
# # print(id(mytpl))
# mytpl = tuple(mytpl)
# print(mytpl)
# print(id(mytpl))

# tuple dagi elementlarni listga kirgissa bo'ladi

# lst = [1,2,3,4,5]
# print(id(lst))
# tpl = (6,7,8,9)
# lst.append(tpl)
# print(lst)
# print(id(lst))

# tuple ni tuple ichiga qo'shsa bo'ladi lekin yangi xotiradan joy egallaydi

# tpl1 = (1,2,3)
# tpl2 = (4,5,6)
# print(id(tpl1))
# print(id(tpl2))
# # tpl2 = tpl1 + tpl2 # lekin biz o'tgan edik ____ = ___ + ___ emas balki ___+=___ tez ishlashini
# tpl1 += tpl2 # baribir boshqa boshqa xotiraga o'tqazib qo'yadi
# print(tpl1)
# print(id(tpl1)) #barbir asl tuple ga tasir qilgani yo'q

# moshinalar = ('ferrari', 'lamborghini', 'bmw', 'mercedes', 'supra', 'tesla')
# (otajon, moxiraxon, *rahmatilla, alimjon) = moshinalar 
# # tuple ni boshqa bir o'zgaruvchiga o'zlashtirish
# print(f'Moxiraxon {moxiraxon}')
# print(f'Otajon {otajon}')
# print(f'Rahmatilla {rahmatilla}')
# print(f'Alimjon {alimjon}')

# moshinalardagi elementlar soni o'garuvchilardan ko'p bo'lganligi uchun bitta elementga * belgisini qo'yib qo'ysak
# ortiqcha elementlar * qo'yilgan o'zgaruvchiga o'zlashtirilib yuboriladi

# ______________________________________________FOR________________________________________________

# Takrorlanish operatorlari - sikllar - loops deyiladi
# 1. for:
# 2. while:

# ishlashi (forga berilgan o'zgaruvchi list ichidagi har bir elementga kirib o'ziga o'lashtirib chiqadi)
# lst = ['moxira', 'alimjon', 'munisa', 'rahmatilla']
# for ism in lst:
#     print(f"Assalomu alaykum hurmatli {ism.title()}\n"
#           f"Sizni kirib kelayotgan muborak Ramazon oyi bilan tabriklayman.\n"
#           f"Hurmat bilan Oripovlar oilasi!\n\n")


# ____________________________________________UYGA VAZIFA____________________________________________

# _________________________________________________1____________________________________________________


# mehmonlar = ('moxira', 'alimjon', 'munisa', 'rahmatilla', 'Abduxalil', 'Nisoatxon', 'Adolat', 'Muhammadali', 'Umida', 'Kimyoxon')
# for taklifnoma in mehmonlar:
#     print(f"""      Assalomu alaykum hurmatli {taklifnoma.title()}
#           Sizni aziz farzandlarimiz"
#         Odinaxon & O'tkirjonlarning
#     nikoh to'ylari munosabati bilan 2024-yil
#     7- sentabr soat 9.00 da yoziladigan "Qizlar
#     bazmi" dasturxonimizga lutfan taklif etamiz.
#           Hurmat bilan Oripovlar oilasi!
#              Manzil: Baxt shahar
#              "Turon" to'yxonasi\n\n""")


# _________________________________________________2_________________________________________________

# moshinaSaloni = ('malibu', 'gentra', 'BYD', 'KIA', 'ferrari', 'lamborghini', 'bmw', 'mercedes', 'supra', 'tesla')
# (muyassar, madina, odina, *ismigul, nasiba, nargiza, sitora) = moshinaSaloni
# print(f'Muyassarga {muyassar} olib berdim.\n'
#       f'Madinaga {madina} olib berdim.\n'
#       f'Odinaga {odina} olib berdim.\n'
#       f'Ismigulga {ismigul} olib berdim.\n'
#       f'Nasibaga {nasiba} olib berdim.\n'
#       f'Nargizaga {nargiza} olib berdim.\n'
#       f'Sitoraga {sitora} olib berdim.')

# __________________________________________________3________________________________________________

# tpl0 = ('malibu', 'gentra', 'BYD', 'KIA')
# tpl1 = ('bmw', 'mercedes', 'supra', 'tesla')
# tpl2 = ('moxira', 'alimjon', 'munisa', 'rahmatilla')
# tpl4 = tpl0+tpl2+tpl2

# for element in tpl4:
#     print(element)

# __________________________________________________4__________________________________________________

# comand =  ('Leicester', 'Tottenham', 'Brighton', 'Man Utd', 'Crystal Palace', 'West Ham', 
# 'Fulham', 'Man City', 'Ipswich', 'Southampton', 'Everton', 'Arsenal', 'Liverpool')
# comand = list(comand)
# del(comand[0])
# comand.pop(3)
# comand[5: 7+1].clear()
# comand = tuple(comand)
# print(comand)

# Buni xotiradan kam joy egallidigan variantiham bormidi?
















