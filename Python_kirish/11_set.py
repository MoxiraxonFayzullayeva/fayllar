# ____________________SET_________________________________________

# elon qilinishi -> {} (ya'ni jingalak qavs) yoki set()

# son = {} #agar biz setti qiymat bermasdan ochsak dictionary qaytaradi
# print(type(son)) 

# # set ni qiymat bermasdan ham ochsak bo'ladi:

# son = set() #ko'rinishida kiritishimiz kerak boladi
# print(type(son))


# sabari setga ham dixtionary ga ham {} jingalak qavs ochilinadi

# set indeksanmagan boladi har safar harxil joydan chiqadi
# set takrorlangan qiymatlarni chopib beradi faqat qiymatlari ham data typelari ham birxil bolishi kerak
# kamchiligi indekslanmagan ikta dublicatelarni qabul qilmaydi
# lekin bu tuple valistga qaraganda tezroq ishlaydi

# konvertatsiya qilishda

# lst = ['abduxalil', 'adolat', 'adolat', 10, 10, 40, 'qwerty', 'qwerty', 'moxira']
# print(lst)
# lst = set(lst)
# print(lst)
# lst = list(lst)
# print(lst)


# nima uchun konvertatsiya qilishda listdan goydalanamiz deydigan bo'lsak chunki listningimkoniyatlari kengroq
#  shuning uchun setti listga konvertatsiya qilib yana qayta setga o'tqizamiz
# tupleni listga konvertatsiya qilib yana tuplega qaytaramiz va h.k

# _____________________________________METODLARI________________________________________________

# setga element qo'shish ya'ni -> EDIT

# ism = {'komila', 'kivi', 'mart'}
# ism.add('olma') # bitta malumot qabul qiladi
# ism.update('anor') # listdagi _____.extand() setdagi _______.update() ekan
# agar update()ni ichiga listda elementlarni kiritib ketsak unda hammasini to'gri qo'shib beradi
# ism.update(['anor', 'xurmo', 'son', 'behi', 25]) # str, int, bool, float hammasini qabul qiladi
# print(ism)

# __________________________discard()/remove()____________________________________________________

# farqi:
# biz kiritgan mallumot set ichida bo'lmasa remove() xatolik qaytaradi
# biz kiritgan mallumot set ichida bo'lsa discard() xatolikni yutvoradi


# ism.discard(25)
# ism.remove('limon') # biz kiritgan mallumot set ichida bo'lmasa remove() xatolik qaytaradi
# ism.remove('anor')
# print(ism)

# ________________________________pop()_____________________________________________________________

# set da ham pop() bor

# # _______________________________union()_________________________________________________________________
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = a | b
# print(c)
# c = a.union(b) # a bilan b ni birlashtirib beradi
# print(c)

# ______________________________intersection()______________________________________________

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a & b) # & - bu belgi ampersand
# print(a.intersection(b))

# bunda a da ham b da ham bor elementlarni o'zlashtirib beradi qolganlarini olmidi

# __________________________________difference()__________________________________________________

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
#
# print(a - b) # bunda birinchi kiritilgan o'zgaruvchininggina farqli jihatini oberadi
# print(b.difference(a)) # bundaxam shunday



# # ^ = symmetric_difference
# #bunda ikkala o'zgaruvchida ham bor farqli jihatlarini olib beradi 

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a ^ b)
# print(a.symmetric_difference(b))

# __________________________________________________________________________________________________

# my = ['ona', 'ota', [15, 56, [15, 'opa', 'uka'], ['aka']], 2, 5, 8, 'akam']
# # print(my[-1])

# for i in my[2][2]:
#     # print(type(i))
#     if i == my[2][2][-1]:
#         print(i.upper())
#     elif i == my[2][2][1]:
#         print(i.title())
#     else:
#         print(i)


# _________________________________________UY ISHI_____________________________________________________

# ___________________________1_________________________________________________________________

# davlat = {'xitoy', 'yaponiya', 'singapur'}
# davlat.add('malayziya')
# davlat.update(['afrika', 'arabiston', 'aqsh', 'rossiya'])
# print(davlat)
# _____________________________2_______________________________________________

# davlat.remove('yaponiya')
# davlat.discard('xitoy')
# davlat.remove('singapur')
# # davlat.remove('singapur')
# print(davlat)


# _________________________________3_____________________________________________


# maxsulotlar = {"go'sht", 'guruch', 'olma', 'pamidor', 'piyoz', 'kartoshka'}
# o_maxsulotlar = {'guruch', 'mosh', 'pamidor', 'lavlagi', 'kartoshka'} 
# o = maxsulotlar - o_maxsulotlar, o_maxsulotlar.difference(maxsulotlar)
# a = maxsulotlar & o_maxsulotlar 
# b = o_maxsulotlar ^ maxsulotlar
# c = a | b
# print(o,'\n', *a,'\n', *b,'\n', *c,'\n')

# __________________________________4_____________________________________________

# guruh = [['kimyoxon', [17, 2007,]], ['nisoatxon', [25, 1999]], ['moxiraxon', [20, 2004]], ['mavluda', [16, 2008]]]

# for i in guruh[0]:
#     if i == guruh[0][0]:
#         print(f'Singlimning ismi {i.title()}')

