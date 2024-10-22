# ________________________________ERRORS___________________________________

# Xatoliklar turi bor PYTHONDA. ular nom berilgan yoki nom berilmagan bo'lishi mumkin ya'ni mantiqiy xatoliklar
# Oldindan ogohlantirib bo'ladigan yoki oldindan ogohlantirib bo'lmaydigan hatoliklar turi bor

# _________________________________SyntaxError_________________________________

# SyntaxError eng ko'p uchraydigan xatolik turi hisoblanib,
# odatda dasturlash tili qoidalariga amal qilmaslik natijasida yuzaga keladigan xatolik turi hisoblanadi

# PYTHON 2-versiyasida avval print bilan () ishlatilinmagan
# print 'Assalomu alaykum' # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

# EOL va EOF

# EOL -> End Of Line (Qatorning oxiridagi xatolik turi)
# masalan:
# print("Assalomu alaykum) # SyntaxError: unterminated string literal (detected at line 22)

# EOF -> End Of Function (Qatorning boshidagi xatolik turi)
# masalan:
# print("Assalomu alaykum" #SyntaxError: '(' was never closed

# ____________________________________________IndentationError______________________________________________
# IndentationError oldindan noo'rin probel tashlanganligi yoki tashlanmaganligi uchun xatolik qaytaradi
# masalan:
#  print("Assalomu alaykum") # IndentationError: unexpected indent


# number = 25
# if number % 2 == 0:
#     print("Juft son")
# else:
# print("Toq son") # IndentationError: expected an indented block after 'else' statement on line 33

# Bu mavzuni o'tishimizdan sabab try_except mavzusini o'rganganimizda xatolik turlarini bilib olgan bo'lsak shunga qarab ishlay olamiz
# nima uchun, qaysi xatolik ustida ishlayatganligimizni tushunib o'tirishimiz uchun kerak bu mavzu

# masalan print yozganimizda u nima vazifani bajarishini bilmimiz, ekranga malumot chiqaryapti lekin aynan qaysi malumotni chiqaryatganligini bilmimiz,
# demak, print terminalda dasturimiz natijasini ko'rsatib beruvchi funksiya ekanligini bilganimizdan so'ng ortiqcha narsalarga chalg'imay printti o'zi bilan cheklanamiz


# number = 25
# if number % 2 == 0:
#  print("Juft son")
# else:
#  print("Toq son") Asslida while if for shunga oxshash funksiyalar uchun chaqirilgan print oldidan bitta probel tashlasak ham yetadi


# number = 25
# if number % 2 == 0:
#   print("Juft son")
# else:
#   print("Toq son") # lekin bitta tapulatsiya tashlash afzal hisoblanadi (Tab) tugmasini bosamaiz. Bu nima uchun kerak deydigan bolsak: sababi kodimiz chiroyli boladi
# yozilgan kodlarimiz tartib bilan chiqib ajratvolishimiz oson bo'ladi, tagma-tag yozilgan kodlarimiz ichida qaysi print qaysi funksiyagan tegishli ekanligini oson topib olamiz

# _____________________________________________RunTimeError_________________________________________

# Dastur bajarish davomida kelib chiqadigan xatolik, dasturning ishlashini to'xtatadi, 

# Bunday xatolikning o'zing bir nechta xatolikturlari ham mavjud bo'lib ular:

# _____________TypeError:
# masalan:

# son = input("Enter the number: ") # input o'zidan string ma'lumot qaytaradi
# print(f"{son}ning kvadrati {son + 2}") # TypeError: can only concatenate str (not "int") to str

# _____________NameError:
# masalan:

# Funksiya yoki operatornimi nomini not'g'ri yozib qo'ysak NameError qaytaradi
# prit("Hello World") # NameError: name 'prit' is not defined. Did you mean: 'print'?

# countries = ['moxiraxon', 'odinaxon', 'muslimaxon']
# for i in countrys:
#     print(i) # NameError: name 'countrys' is not defined. Did you mean: 'countries'?


# _____________ValueError:
# masalan:

# qiymat xatoligi biz kiritgan format chiqarmoqchi bo'lgan formatimizda chiqmaydi
# son = int(input("Son kiriting: ")) 
# print(son) # ValueError: invalid literal for int() with base 10: '5.6'

# son = float(input("Son kiriting: ")) # <- bu ko'rinishdagi formatda ValueError bo'lmaydi
# print(son)  


# ________________IndexError
# masalan:

# qiymatdagi uzunlikka qarab indeksni chaqirganda, biz kiritgan indeks mavjud bo'lmasa xatolik qaytaradi
# mevalar = ['qulupnay', 'banan', 'kiwi', 'ananas']
# print(mevalar[9]) # IndexError: list index out of range


# __________________ZeroDivisionError
# masalan:

# 0 ga bo'lib bo'lmaydigan xatolik turi, matematikada ham dasturlashda ahm har qanday sonni 0 ga bo'lib bo'lmaydi
#  (ko'paytirish mumkin lekin unda ham harqanday sonni 0 ga ko'paytirsa 0 ning o'zi chiqadi)
# a, b = 25, 25
# y = 100/(a-b)
# # # y = 100*(a-b)
# print(y) # ZeroDivisionError: division by zero


# _______________________________________MantiqiyXatoliklar_________________________________________________


# Mantiqiy xatoliklar aksariyati odatda xatolik qaytarmaydi, dastur ishlab turaveradi lekin biz kutgan natijani bermaydi
# ya'ni: 100 qatorlik kodni butunlay yozib bo'ldik va run berdik natija 10 chiqishi kerak, lekin bizga nimadir bo'lib 20 yoki 11qilib natija chiqarildi
# xato 30-qatorda bo'lgan, lekinbiz kod boshidan oxiriga tushib chiqib ham topa olmay qolamiz, mantiqiy xatolikka e'tibor bermasak

# masalan:

# son = float(input("Istalgan son kiriting: "))
# ildiz = son ** 1/2 # bu yerda son ** 1 / 2 bo'lib  bu son ** 1(/2) kiritilgan sonning birinchi darajasini hisoblab olib keyin 2 ga bo'lib qoyyapdi 
# print(f'{son} ning ildizi {ildiz} ga teng') # 6.0 ning ildizi 3.0 ga teng


# radiusi = 5
# pi = 4.423685
# aylana_yuzi = pi * radiusi ** 2
# print(aylana_yuzi)


# countries = ['Japan', 'uzbekistan', 'toshkent', 'ukraina']
# for i in countries:
#     print(i)
#     print("Dastur tugadi.") # kodimiz ishlayveradi lekin biz kutgan natija bermaydi

# # natija:
# Japan
# Dastur tugadi.
# uzbekistan    
# Dastur tugadi.
# toshkent      
# Dastur tugadi.
# ukraina       
# Dastur tugadi.

# countries = ['Japan', 'uzbekistan', 'toshkent', 'ukraina']
# for i in countries:
#     print(i)
# print("Dastur tugadi.")

# # biz kutgan natija
# Japan
# uzbekistan    
# toshkent      
# ukraina       
# Dastur tugadi

# son = 1
# while son < 10:
#     print(son, end=' ')


# ______________________________________________UYGA VAZIFALAR______________________________________________

# _______________________1____________________




























