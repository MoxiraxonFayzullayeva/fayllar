

# Fayllar bilan ishlash


# biz avvalgi darslarimizda yozgan kodlarimizdagi input kiritgan narsalar saqlanib qolmaganligini kuzatganmiz
# endi biz fayllar bilan ishlash jarayonida input kiritgan ma'lumotlarni ham saqlab qolishni 
# (ya'ni terminalda chiqargan natijamizni boshqa faylda saqlab borishni o'rganamiz)


# fayllari bilan ishlashda shunday narsa borki kiritilgan ma'lumot text formatida txt faylda saxratin bo'lib ketaveradi
# ya'ni -> biz kiritgan ma'lumotlar huddi real hayotdagi qayd daftarchaga yozib ketgan narsalarimizdek turadi uni saxranit qilganimizda bizga *.txt formatda saxranit qilib beradi
# (fileni qo'lda ochvolib bo'ldik ichida biz qo'lda kiritgan qiymatlar bor) 
# bir narsani yodimizda saqlashimiz kerak, bu -> filelar ichidagi hamma kiritilgan malumotlar string holatda ya'ni str formatda bo'ladi
# dastur file ichidagi narsalarni matn deb tushunadi (huddi inputga o'xshab)

# 'r' -> 'read' degani kiritilgan fileni o'qi 
# 'w' -> 'write' degani kiritilgan filega yozish, bunda ehtiyot bo'lishimiz kerak chunki eski filemiz ichida kerakli malumotlar bo'lsa 
# 'w' qilib ketishimiz avval yozilingan malumotlarni sbros ya'ni yo'q qilib yuboradi
# file shunday ochilinadi bizda open ichidagi fileimiz mavjud uni qisqaroq qilib f ko'rinishida chaqirvoldik 
# with open('pi.txt') as f: # bunday defolt holatda turishini dastur o'qish uchun ochilinyapti deb tushunadi
# with open('pi.txt', 'r') as f: 
# # # with open('C:\Python\pi.txt', 'r') as f: # copy path qilib ishlatsa ham bo'ladi (\ slash o'rniga backslash qoysa ham ishlayveradi)
#     pi = f.read()
#     print(pi)

# with open() OPTIMAL BVARIANT HISOBLANADI CHUNKI AVTOMAT TARZDA KO'P NARSANI ORQA TOMONDAN AMALGA OSHIRIB BERADI
# bulardan biri file ochilingandan keyin uni yopish amaliyotini ham o'zi amalga oshirib ketadi, 
# agar boshqacha yo'l bilan ochilinganda albatta kodimiz oxirida *.close() metodini qollab ketishimizga to'g'ri keladi


# # faylni ochishni ikkinchi usuli ham bor bu:

# file = open('pi.txt') # as f qilib ketsak ham bo'ladi # ya'ni o'zgaruvchiga o'zlashtirib ochib ketish 
# pi1 =file.read() # biz o'zgaruvchini elon qilishda sonni ishlatishimiz mumkin faqata so'z boshida emas

# print(pi1) 
# file.close() # bu usulda ochilgan file ni close() qilib yopib ketishimiz kerak bo'lmasam fileimizga zarar yetib qolishi mumkin



# with open('pi.txt', 'r') as f: # buni 'r' yozmasdan ham ishlatishimiz mumkin
#     pi = f.read() # text ni chaqirdik o'zgaruvchi berdib o'zlashtirdik, o'qidi
#     pi = pi.replace('\n', '') # biz replace string metodidan bo'lib ishlab turibdi bu degani,
    # demak haqiqatan ham chaqiryatgan filimiz ichidagi hamma narsa stringda turibdi, va biz bo'shliqlar o'rniga ya'ni \n o'rniga xechnarsa qoymaslik uchun
    # qoshib chiqarishi uchun '' dan foydandik
    # pi = float(pi) # keyin chaqirgan fileimiz ichidagi malumotlarni floatga konvertatsiya qildik ichidan faqat bittasigina konvertatsiya qilinishini natijada ko'ramiz
    # print(pi) # natijasi 3.1415926535897953 chiqdi nima uchun fileda turgan malumotimiz o'zgarib qoldi desak:
    # print(type(pi)) # haqiqatan floatga o'tganini berganini tekshirib oldik
    # print(pi) # pi = float(pi) ni kamentariyaga olib tekshiramiz


# Qoida: float type 16 xonali sonlargscha hisoblay oladi. Uyog'iga o'zi ketadi
# Agar bank schotlati bilan ishlayotgan bo'lsak biz decimal kutubxonani chaqirib olish orqali foydalanamiz 

##### from decimal import Decimal

# avvalgi darsda aytib o'tganimiz integerni hotira optimallashuvi -5 dan 257 gacha deb adashgan ekanmiz bu korsatgich -5 dan 256 gacha ekan

# int = -5 to 256 memory optimisation

# a = 256
# b = 258
# d = 258   ###############
# print(id(a), id(b), id(d))


# with open('students.txt', 'r') as f:
#     students = f.readlines() # o'zgaruvchiga nuqta(.) qoysak bo'ldi qanaqa metodlari borligini ozi chiqarib beradi 
#     print(students) # ['Moxiraxon Fayzullayeva\n']
# readlines() list qaytarar ekan natijani chiqarganimizda nechi qator bo'lsa undagi bor narsani chiqarib beradi
# kursorni ham qayerda turganini bilib olishimiz kerak: kursor bir qatorni o'qib bo'ldimi srazi bopshqa qatorni boshidan o'qishni boshlaydi
# yani hozir 1 qatordagi natijani chiqardik kursor esa ikkinchi qator boshida qoldi u yerda ma'lumot xechnarsa yoq  

# file ichidagi ma'lumotlarga metod qo'llab koramiz
# students = [student.rstrip() for student in students]
# print(students)

# ----.rstrip() o'ng tomondagi becklsash \n larni ya'ni bo'shliqlarni chopib berdi
# ----.lstrip() chap tomondagi becklsash \n larni ya'ni bo'shliqlarni chopib berdi
# ----.strip() hamma boshliqni chopadi

# metodlarni ozidan nima qaytarishini bilib olsak masalalarni yechishimiz shunchalik osonlashib boraveradi

# _______________________________________UYGAS VAZIFALAR_____________________________________

# _____________1___________________

# with open('uy_ishi_25_1.txt') as u:
#     vazifa = u.readlines()
#     print(vazifa, '\n')


# vazifa = [ismlar.rstrip() for ismlar in vazifa]
# print(*vazifa)

# _____________2_________________

with open('uy_ishi_25_2.txt') as u:
    












