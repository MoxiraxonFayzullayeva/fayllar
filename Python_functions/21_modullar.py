

# import modul as m    # as degani dek degani bunarsani vazifasi faylga asdan keyin boshqa nom berib murojaat qilsa bo'ladi
# # uzunroq modullaarni chaqirganda shunday as ishlatib qisqartirib ketamiz
# from modul import daraja_hisoblovchi as dh #qisqartirib

# # from degani -> moduldan import qilgin bitta narsani ya'ni daraja_hisoblovchinigina import qilib bergin degani


# import modul as m
# print(m.daraja_hisoblovchi(2, 3))

# from modul import daraja_hisoblov, info_cars #bu yerda hozir faqatgina ikta funksiyani chaqirdik
# agar import o'zini ishlatganimizda, fayldagi hamma funksiyalarlarnichaqirib qo'ygan bo'larmiz va ishlatsek ishlatmasek 
# funksiyalar orqa tomonda kelib turadi, joy egallab

# from modul import * # Bunday yozish tafsiya etilinmaydi, sababi bu hamma funksiyalarni shu yerga chaqirib qoy degani
# agar biz dastur davomida bir o'zgaruvchi (masalan daraja => degan o'zgaruvchi) ochib ketsak biz bilmaymiz chaqirgan funksiyamiz ichida ham shunday
# o'zgaruvchi bor bo'lishi mumkin, va xatolik bo'lishi yoki biz kutmagan natijalar chiqib ketishi mumkin


# from modul import daraja_hisoblovchi as dh, info_cars as ic
# ishlatilgan kutubxonalarni o'chirib qoyish yoki komentariyaga olib ketishimiz kerak yoki chaqiryatgan funksiyalarimizni o'zi bilan cheklanishimiz kerak
# sababi bitta o'zgaruvchiga berilgan qiymatti oladigan bo'lsak uni orqasida qanchadan qancha kod bo'lib ketadi bu xotiradan katta joy oladi, 
# dasturimizni qotirib qoyishi mumkin


# kutubxona yasash (chaqirish)

# import math #pythonda yaratilgan kutubxona matematik amallar bor bu yerda 

# a = 4
# # print(math.sqrt(a)) #kutubxonada ishlatilish usuli [sqrt degani ildiz chiqarib beradi]
# # print(4 ** 0.5) #qo'lda kiritilgan kod varianti

# # print(math.pow(a, 2)) # pow() da o'zgaruvchidagi sonning nechinchi darajasini bermoqchi bo'lsak shu daraga oshirib chiqarib beruvchi amal, 
# # (bu yerda faqatgina o'zgaruvchi emas balki qiymat berib ketsak ham ishlayveradi) print(math.pow(4, 2))

# # qo'lda kirgizib dasturlashni o'zini tilida kod korinishida ishlidigan bo'lsak qiymay bir xil lekin datatype boshqa boshqa bo'ladi

# a = 4
# print(math.pow(a, 2)) # float qaytaradi
# print(math.pow(4, 2)) # integer qaytaradi


# from math import pi # bu yerda hizir faqat pi ni chaqirib ishlatdik 
# print(pi) # pi=konstanta qiymat ya'ni o'zgaruvchi qiymat



# print(int(math.log2(8))) # kutubxonadan foydalanganimizda float qaytarmasligi uchun intdan kerakli joyda foydalanishimiz kerak ekan 
# print(math.log10(100))


# random -> kompyuter tromonidan tanlabberiladigan narsa(masalan 1 dan 100 gacha bo'lgan sonlar ichida tasodifiy bitta 
# yoki birnechta sonni tanlab olishimiz uchun ishlaydi)


# import random as r
# number = r.randint(0, 100) # random biz kiritgan qiymatlarimizgacha ishlaydi
# r.randint -> integer type dagi ma'lumotlar bilan yanlaymiz shu kabi bir qancha metodlari ham bor randomni
# print(number)


# range(0, 10) # range biz kiritgan qiymatgachagina oladi biz kiritgan qiymatni olmaydi
# # rangeda nima uchun +1 degan narsa bor deydigan bo'lsak - chunki chegara o'zgaruvchidan olinadigan qiymatga bog'liq bo'lsa 
# uni o'zgartirib qo'yishga bizni haqqimiz yo'q
# # (masalan)
# n=10
# range(0, n+1) #qilib ishlata olamiz algoritmik masala yechyatganimizda kelasida shuusuldan foydalanib (ya'ni-> +1) qilib ketamaiz


# import random as r

# # names = ['bunyod', 'alimjon', 'rahmatulla', 'moxiraxon', 'otajon']
# # name = r.choice(names) # ichidan bittasini tanlab oladi
# # print(name)

# a  = list(range(0, 51, 5))

# print(a) 
# print(r.choice(a)) #qisqasi choise ro'yxatlarga ishlaydi ekan



# # shuffle 

# x = list(range(11)) # tartib bilan ketgan narsani -> shuffle - aralashtirib beradi
# print(x)
# r.shuffle(x) 
# print(x)




# from random import sample # bizga random bo'yicha 1 donadan ko'proq qiymat kerak buni chaqirish uchun sampledan foydalanamiuz

# x = list(range(0, 100))
# y = sample(x, k=10) # k => 0 dan 100 gacha bo'lgan sonlar ichida nechta ihtiyoriy son hohlasak shunchasini tanlab beradi
# print(y)
# print(sorted(y))
# print(sorted(y, reverse=True))

# _____________________________UYGA VAZIFALAR______________________________________


    











