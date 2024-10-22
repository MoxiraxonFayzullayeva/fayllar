# _________________________________SHART OPERATORLAR_______________________________

# shart operatorlar 6 ta:
# 1. ARIFMETIK OPERATORLAR
# 2. BELGILASH OPERATORLARI
# 3. TAQQOSLASH OPERATORLARI
# 4. MANTIQIY OPERATORLAR
# 5. IDENTIFIKATSIYA OPERATORLARI
# 6. A'ZOLIK OPERATORLARI


# ___________________1_____________ARIFMETIK OPERATORLAR________________________________


#  + PILUS; 
# - MINUS; 
# / BO'LISH(FLOATDA CHIQARADI); 
# // BO'LISH(INTEGERDA CHIQARADI); 
# * KO'PAYTIRISH:
# ** DARAJAGA OSHIRISH; 
# % FOIZDA BO'LISH.

# a = 50
# p = 51
# b = 4
# d = a % b
# o = p % b
# print(d, '\n', o) # 2 (% foizga bo'lganda qoldiq nechi chiqsa ushani ushab beradi)

# son = 10 # son bu o'zgaruvchi hisoblanadi
# print(son % 2 ) # shunaqa narsa borki ya'ni print ichida ham arifmetikoperatorlarni amalga oshirish mumkin

# son = 10
# print(son / 2) # float da chiqarib beradi
# print(son // 2) #integerda chiqarib beradi

# _____________________2_______________BELGILASH OPERATORLARI________________________

# =  (x=5) teng belgisi bo'lib shu narsa ushbu narsaga teng degan ma'noda  keladi
# += (x+=3) bu x = x+3 ning qisqartirib yozilgan ko'rinishi, har ikkisiham to'g'ri bo'ladi
# -= (x-=3) bu x = x-3 ning qisqartmasi, ikkalasi ham to'g'ri
# *= (x*=3) bu x = x*3 ning qisqartmasi, ikkalasi ham to'g'ri
# /= (x/=3) bu x = x/3 ning qisqartmasi, ikkalasi ham to'g'ri(floatda chiqadi)
# //= (x//=5) bu x = x // 5 ning qisqartmasi, ikkalasi ham to'g'ri
# %= (x%=3) bu x = x % 3 ning qisqartmasi, ikkalasi ham to'g'ri
# **= x**=3) bu x = x ** 3 ning qisqartmasi, ikkalasi ham to'g'ri
# masalan:

# son = 5
# son *= 3
# print(son)
# _______________________3___________TAQQOSLASH OPERATORLARI_________________________________________

#  == tengmi degani
#  != teng emasmi degani
#  >  katta
#  <  kichik
#  >= katta yoki teng bo'lsin
#  <= kichik yoki teng bo'lsin 

 
# ________________________4________MANTIQIY OPERATORLAR_____________________________________________

# and  - & va *
# or   - | va +
# not - yoq degani

# _________________________5____________________IDENTIFIKATSIYA OPERATORLARI________________________


# is - ==  (tengmi) degani (yana is ni o'zi ham alohida vazifasi bor)
# == - qiymatlari bilan aniqlab beradi
# is - adresi bilan aniqlab beradi
# is not -!= (-)

# x = ['banan', 'olma', 'lemon', 'qulupnay']
# y = ['banan', 'olma', 'lemon', 'qulupnay']
# z = x

# # print(x is y) # adresi bilan aniqlaganda ikkalasi har xil shuning uchun False qaytadi
# # print(x == y) # qiymatlari bilan aniqlaganda ikkalasi ham bir xil shuning uchun True qaytadi

# # hamma o'zgaruvchilarni hotirada saqlanayotganda alohida adresi bor uni ID bilan aniqlaymiz

# print(id(x)) # 2189142479488 adresda
# print(id(y)) # 2614933484992 adresda

# ____________________________________________A'ZOLIK OPERATORLARI____________________________________

# in - ichida bormi degani
# not in - ichida yo'qmi degani

# print('abs' in 'absasdfghjkiuytrewaxcabsgfdwqwerthjnbvcsa') # ichida bor bo'lsa True qaytadi
# print('abs' in 'iuytjhasdfghjkiuytrewaxcgfdwqwerthjnbvcsa') # ichida yo'q bo'lsa False qaytadi
# print('abs' not in 'absasdfghjkiuytrewaxcabsgfdwqwerthjnbvcsa') # ichida bor bo'lsa False qaytadi
# print('abs' not in 'lkjasdfghjkiuytrewaxcgfdwqwerthjnbvcsa') # ichida yo'q bo'lsa True qaytadi


# qiziqarli narsa ko'ramiz

# print((5+5)*10/5) # float da 20 
# print((55+10-20/2)) # float da 55
# print((5+5)*(10//5))# integer da 20 
# print((55+10-20//2)) # integer da 55

# __________________________________________UYGA VAZIFA_____________________________________________


# 1. Matnni in orqali Tekshirish:__________________________________________________________________
# text o'zgaruvchisida matn bor. Agar matnda a harfi bo'lsa, True, aks holda False natijani chiqarish.
# text = "Agar matnda a harfi bo'lsa, True, aks holda False natijani chiqarish."
# print('a' in text, 'a' not in text)

# 2. Raqqamni Toq yoki Juftligini Aniqlash:_______________________________________________________
# # number o'zgaruvchisi bor. Agar raqam toq bo'lsa, True, aks holda False natijani chiqarish.
# number = int(input(">>> "))
# print(number % 2 == 0)
# print(number % 2 != 0)

# 3. Matnni Ko'paytirish:_________________________________________________________________________
# text o'zgaruvchisini 3 marta ko'paytirish va natijani chiqarish.
# text = 'Matn uzunligini hisoblash va natijani chiqarish.' 
# print(text*3 )


# 4. Matnning Uzunligini Hisoblash:_______________________________________________________________
# text o'zgaruvchisi bor. Matn uzunligini hisoblash va natijani chiqarish.
# text = 'Matn uzunligini hisoblash va natijani chiqarish.'
# print(len(text))

# 5. Raqamni Qisqartirish:_________________________________________________________________________
# number o'zgaruvchisini 5 ga qisqartirish va natijani chiqarish.
# number = int(input(">>> "))
# print(number // 5)

# 6. Matnda Harf Sonini Hisoblash:_________________________________________________________________
# text o'zgaruvchisi bor. Matndagi e harflarining sonini hisoblash va natijani chiqarish.
# text = 'Matndagi e harflarining sonini hisoblash va natijani chiqarish.'
# print(text.count('e'))














