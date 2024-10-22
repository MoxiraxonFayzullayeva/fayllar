
# _____________________________DICTIONARY  -  dict_________________________________________

# dict = {} (bo'sh dict ochilishi)
# dictionaryda bilamiz -> so'z - tarjimasi bo'ladi huddi shunday ichidagi elementlar

# so'z - tarjima -> key (kalit) - value (qiymat) ko'rinishida bo'ladi

# ikki xil elon qilinishi bor:

# ozgaruvchi = dict() # dasturlarni ichida bunday holatda e'lon qilinadi
# ozgaruvchi = {} # dastur boshi shunday e'lon qilib ketilinadi

# qiymatlarni ajratvolishda eng osoni dictionany

# masala:

# car = {'nomi': "mercedes",
#         'modeli': 'X7',
#         "color": "oq"}
# print(car)
# dict tartiblangan lekin indekslanmagan bo'ladi
# print(car[0])
# tartiblangan:
# print(car['modeli']) #key kiritsak bizga value sini chiqarib beradi

# print(f'Men kecha yangi {car["nomi"].upper()} sotib oldim.\n'\
#         f'Modeli: {car["modeli"]}. Rangi esa {car["color"]}.')

# endi car dagi qiymatti o'zgartiramiz(update qilamiz) yoki qoshamiz

# # agar o'zgaruvchidagi bor kalitti o'zgartirsak
# car['color'] = 'pushti' # bu ham bir metodlardan biri
# print(car) # telefonimizdagi ilovani yangilash qilganimizda uning versiyasi qanday yangilansa 
# # bunda ham biz oxirgi yangilagannarsamiz qoladi eskisi o'chirilib o'rniga yangisi ya'ni yangi versiyasi qoladi

# # agar o'zgaruvchida yo'q kalit kiritsak: yangi qo'shmoqchi bo'lsak
# car['engine'] = True
# print(car)

# # yana bir narsa ko'ramiz

# # agar dictiomary ni ichidagi elementlarni uzunligini sanasak:

# print(len(car)) # bunda 'color' degan kalitti bitta deb hisoblaydi sababini boya aytib o'ttik
# (ya'ni eskisi o'chib ketadi o'rnini yangisi oladi)

# _________________________________del___________________________________________________________


# car = {'nomi': "mercedes",
#         'modeli': 'X7',
#         "color": "oq"}
# print(car)

# car['color'] = 'pushti' 
# car['engine'] = True
# print(car)

# del car #ochilgan o'zgaruvchini butunlay yo'q qilib yuboradi
# del car['engine'] #bunda esa kiritilgan key ni o'zini gina chopib beradi
# print(car) #none qaytaradi


# __________________________________get()__________________________________________________________


# car = {'nomi': "mercedes",
#         'modeli': 'X7',
#         "color": "oq"}

# car['engine'] = True
# print(car)

# get(xatolikni yutib ketadi)
# new_car = car.get('narx', 'bunday key mavjud emas')
# # yuqorida key berdik agar key mavjud bo'lmasa chiqarmaydi 
# print(new_car)

# new_car = car.get('color', 'bunday key mavjud emas') # agar mavjud bo'lsa keyni valuesini chiqarib beradi
# print(new_car)

# print(car.get('engine'))

# _________________________________________________________________________________________________________





















