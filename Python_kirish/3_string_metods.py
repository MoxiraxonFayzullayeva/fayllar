# =====================================================STRING===============================================================

#  qo'shtirnoq bilan birtirnoq ikkalasi ham matnga tegishli lekin ularning farqi:
# bitritnoq ochilganda mantnning davomida (o) ga shapka kelib (o') bo'lganida qo'shtirnoq o'ziga o'xshaganini qidirib ketadi
# va topishi bilan yopadi, va hatolik beradi
# bunday xolatda birtirnoq oldiga BACKSLASH (\) belgisini qo'yamiz, shunda xatolik bermaydi


# ism = "Umar"
# ism = 'Assalom O\'zbekiston' bunda backslash (\) belgisi tushib qoladi
# print(ism)

# ============================================== stringagi (+) va (,) ==========================================================
# 
# ism = "Moxiraxon" 
# print("Assalom", ism) #vergul ikki so'z ortasiga bo'shliq qo'yib beradi
# print("Assalom"+ ism) #plus ikki so'z o'rtasini qo'shib beradi,bunda orasini ochishimiz uchun pastdagi amalni bajaramiz
# print("Assalom"+ ' ' + ism)

# -----------------------------------------------------f-string--------------------------------------------------------------
# ism = 'Mohiraxon'
# familiya = 'Fayzullayeva'
# sharifi = f'{familiya} {ism}' # sharifi = f'Sizning farzandingizning {ism} {familiya}

# # print(sharifi) f-stringni o'zgaruvchiga o'zlashtirb ham ishlarsa bo'ladi
# print(f'Men {familiya} {ism}man. Yoshim esa {2024-2004}da') # f-stringni print ichida ham ishlatsa bo'ladi, murakkab 
# variantlarini dars davomicda o'rganib chiqamiz

# --------------------------------------------f-stringda matematik amal-------------------------------------------------------

# yosh = 20
# print(f'Men {2024-20}-yilda tavallud topganmaman')

# f-stringda hammasi jingalak qavs ichida ishlatilinadi

# malum bir funksiya uchun ishlatiladigan data type lar boshqa biror funksiya uchun ishlamaydi

# ---------------------------------------------------upper() va lower()-------------------------------------------------
# upper()-hamma harflarni bosh harfga o'zgartirib beradi 
# lower()-hamma harflarni ikichik harfga o'zgartirib beradi
# bular orqasida forsikl ya'ni takrorlanish operatori ishlaydi chunki bitta so'zni qaytadan o'qib chiqadi

# ism = 'Mohira'
# print(ism.upper()) 
# print(ism.lower())
# print(f'{ism.upper()}') # f-stringda jingalak qavs ichida ishlatilinadi, jingalak qavs tashqarisida yozilsa matn deb o'qiydi

# --------------------------------------------------title() va capitalize()-------------------------------------------------

# title() da hamma so'zlarni alohida bosh harf holatiga keltiradi 
# capitalize() da faqatgina gapning boshidagi so'zni bosh harf holatiga keltirib beradi

# ism = 'moxiraxon fayzullayeva abduxalil qizi'
# print(ism.title())
# print(ism.capitalize())

# title() ni bitta tarafi, so'zda kelgan belgilardan keyin kelgan harfni ham katta harf holatiga keltirib qo'yadi 
# qo'shtirnoqda bo'lsa ham bir tirnoqda bo'lsa ham

# ism = 'o\'rmon'
# print(ism.title())
# ism = "o'rmon"
# print(ism.title())


# ----------------------------------------------strip(), lstrip() va rstrip()-----------------------------------------------
# bo'shliqlar bo'yicha chopib beradi
# lstrip() - chap tomondagi bo'shliqni qancha bo'lsa yo'q qilib beradi (o'ng tomon qiziqmas)
# rstrip() - o'ng tomondagi bo'shliqni qancha bo'lsa yo'q qilib beradi(chap tomon qiziqmas)
# strip() - ikkala tomondagi bo'shliqni chopib beradi

# meva = '    qulupnay   '
# print("Men" + meva.lstrip() + "ni yaxshi ko'raman.")
# print("Men" + meva.rstrip() + "ni yaxshi ko'raman.")
# print("Men" + meva.strip() + "ni yaxshi ko'raman.")


# meva = '    qulupnay   '
# print("Men", meva+"ni yaxshi ko'raman.")
# print("Men", meva.lstrip() + "ni yaxshi ko'raman.")
# print("Men", meva.rstrip() + "ni yaxshi ko'raman.")
# print("Men", meva.strip() + "ni yaxshi ko'raman.")

# ================================================string ikkinchi qismi=====================================================
# indeks - dasturchilar indekslarni 0 dan boshlab sanaydi, matematiklar esa 1 dan boshlan o'qiydi

# soz = "as salam"
# print(soz[0]) # bu = a ga 
# # indeks bo'yicha (0) dan boshlab sanaladi
# # lenth - len() uzunligi bo'yicha (1) dan boshlab aniqlab beradi
# print(len(soz))


# ---------------------------------------------------------text------------------------------------------------------------- 

# textda kelgan so'zlarning bor yo'qligini aniqlash uchun print ichida mant yozib (in) va o'zgaruvchi nomini kiritamiz
# bunda boolean ya'ni True yoki False qaytaradi (bitta harf holatiga ham qaraydi, ya'ni matnda katta harf bilan yozilgan 
# so'zni printda kichik hafr bilan bersak False chiqadi)

# text = "Men AVO Bankka ishga kirdim!"
# print("AVO" in text) # boolean - True
# print("aVO" in text) # boolean - False
# print(type("AVO" in text))

# buni teskarisi bor

# print("AVO" not in text)
# print("aVO" not in text)

# =======================================================KESISH==============================================================

# soz = "MICROSOFT Inc"
# print((soz.lower()).title()) #o'zim uchun ko'rdim
# indeks chiqarishda nimaning indeksini chiqarish kerakligi haqida buyruq berib ketish kerak (ya'ni o'zgaruvchini nomini 
# kiritib ketish kerak)
# print(soz[8])

# -----------------------------[start:end:step]-indekslarni [boshlanishi:tugash:qadam] --------------------------------------
# soz = 'foundation'
# print(soz[2:5])
# print(soz[2:5+2])
# print(soz[:5+2]) # boshlanishi erkin holatda tursa (0) indeksdan boshlanadi
# print(soz[2:]) # tugashi erkin holatda tursa oxirgi indeksgacha boradi
# print(soz[-1]) # bunda bizga oxirdan boshlangan indeks kerak bo'lsa(-) da kiritamiz 
# (-0 degan narsani o'zi yoq (son o'qida ham faqatgina 0 bor))

# soz = "MICROSOFT Inc"
# print(soz[::2]) # boshlanishiga va tugashiga xechqanday raqam kiritmasagu faqat qadamni kiritadigan bo'lsak 
# so'zda shuncha sakrab yuradi (yuqorida boshlanish erkin holatda tursa (0) indaksdan boshlab olishi haqida aytib o'tdik)

# soz = "MICROSOFT Inc" # endi teskarisiga qarab o'qishni hohlasak quyidagicha kiritamiz
# print(soz[-1::-1])
# yani qadamlar qatoriga -1 kiritib yozamiz
# agar o'rtadagi indeksdan boshlab teskarichasiga o'qishi hohlasak quyidagicha kiritamiz
# print(soz[-5::-1])

# # agar teskari o'qiganda faqatgina biz hohlagan indeksgacha o'qishi hohlasak quyidagicha kiritamiz
# print(soz[-5:4:-1])
# print(soz[-5:3+1:-1])

# yoki
# print(soz[-5:-9:-1])
# print(soz[-5:3+1:]) qadam kiritilmasa xechnarsa chiqarib beramaydi

# indekslarni [boshlanishi:tugash:qadam] - [start:end:step]

# -----------------------------------------------------replace()-------------------------------------------------------------
# o'zgaruvchi qiymatidagi biror indeksni boshqa bir narsaga o'zgartirish uchun foydalaniladi (faqat string bo'lishi kerak)

# ism = 'otajon'
# ism2 = ism.title()
# print(ism.replace('j', '1'))
# print(ism.replace('o', '0'))
# print(ism2.replace('jon', 'bek'))

# -------------------------------------------------------format()---------------------------------------------------------

# yosh = 20
# ism = "Mening ismim Moxiraxon. Mening yoshim {} da." # jingalak qavs bizga kiritmoqchi bo'lgan o'zgaruvchimizning 
# qayerda kelishini ta'minlaydi.
# print(ism.format(yosh))

# made = "Mercedes Benz"
# model = "X7 Drive"
# price = 300000000000 # biz 0 larda adashib ketmaslik uchun (_) tagchiziqdan foydalanamiz( nuqta(.) yoki verguldan(,)
# foydalanadigan bo'lsak float yoki xatolik beradi)
# price = 300_000_000_000 # pastki chiziqcha run qilganimizda yo'qolib ketadi
# buyurtma = "Men yangi {} sotib oldim. Modeli: {}. Narxi esa ${}." jingalak qavslarga qarab o'zgaruvchilarning qaysi biri qayerdakelishini hohlasak

# print(buyurtma.format(model, made, price)) # printda o'zgaruvchilarni ketmaketlikda joylashtiramiz

# --------------------------------------------------isnumeric(), isdigit()-------------------------------------------------
# ikkalasi deyarli birxil vazifani bajaradi
# stringda hamnmasi sonmi kelganmi yo'qmi shuni tekshirvolishimiz uchun isnumeric() yoki isdigit() qilib tekshirvolamiz
# son = '32345678' # hammasi son bo'lsa True
# son1 = "2345676543l2" # agar ichida harf qatnashgan bo'lsa False
# print(son.isnumeric()) 
# print(son1.isdigit())

# endi yuqoridagi isnumeric() bilan indigit() ni teskarisi bor ular

# _________________________________________________________isalpha()_________________________________________________________ 
# stringda hammasi harfmi shuni tekshirib beradi (agar ichida  probel ya'ni bo'shliq tashlab ketilgan bo'lsa ham False qaytaradi)
# soz = 'Google' # True
# print(soz.isalpha()) 

# gap = "Google kompaniyasi" # False (chunki bo'shliq ham qatnashgan)
# print(gap.isalpha()) 


# ----------------------------------------------------index() va find()-----------------------------------------------------
# ikkalasiham indeksni topib beradi
# index() nechinchi indeksdan boshlanishi
# find() nechinchi indeksda turibdi

# top = "Siz NASA kosmik stansiyasida ishlaysiz"
# print(top.index("NASA"))
# print(top.find("NASA"))

# -----------------------------------------------------------count()--------------------------------------------------------
# sanab beradi print ichida nimani sanashni buyursak shu narsa stringda nechta ekanligini sanab beradi
# bu ko'p ishlatilinadigan medotlardan biri hisoblanadi
# xat = "asd hgfwertyhjbvcasd aswertyhbvcx asdjlkjhgfdsaasd"
# print(xat.count('asd'))


# -------------------------------------------------------casefold()-----------------------------------------------------------
# lower()ni sinonimi
# (casefold() afzalroq lower()dan)

# maktub = "Men ARMIYAGA ketyapman."
# print(maktub.casefold())


# =======================================================Sinf ishi==========================================================

# __________________________________________________________1-2__________________________________________________
# viloyat1 = 'Toshkent'
# shahar1 = 'Toshken'
# mahalla = 'Gulzor'
# kocha = 'T.Haqiqat'
# # asd = " {} viloyat, {} shahar, {} mahallasi, {} ko'chasi."
# # print(asd.format(viloyat1, shahar1, mahalla, kocha))
# print(f'{viloyat1} viloyati, {shahar1} shahar, {mahalla} mahallasi, {kocha} ko\'chasi')

# # qo'shimcha
# # viloyat1 = 'toshkent'
# # shahar1 = 'toshken'
# # mahalla = 'gulzor'
# # kocha = 't.haqiqat'
# # z1 = [viloyat1, shahar1, mahalla, kocha]
# # print(f'{z1[0].capitalize()} viloyati,', f'{z1[1].capitalize()} shahar,', f'{z1[2].capitalize()} mahallasi,', f'{z1[3].title()} ko\'chasi.')
# # print(f'{z1[0].capitalize()} viloyati,','\n' f'{z1[1].capitalize()} shahar,', '\n' f'{z1[2].capitalize()} mahallasi,', '\n' f'{z1[3].title()} ko\'chasi.')


# viloyat2 = 'Sirdaryo'
# shahar2 = 'Baxt'
# mahalla2 = 'Xazina'
# kocha2 = 'Y.Qrilish'
# # asd = " {} viloyat, {} shahar, {} mahallasi, {} ko'chasi."
# # print(asd.format(viloyat2, shahar2, mahalla2, kocha2))
# print(f'{viloyat2} viloyati, {shahar2} shahar, {mahalla2} mahallasi, {kocha2} ko\'chasi')

# # /t
# # \n

# # qo'shimcha
# # viloyat2 = 'sirdaryo'
# # shahar2 = 'baxt'
# # mahalla2 = 'xazina'
# # kocha2 = 'y.qrilish'
# # r1 = [viloyat2, shahar2, mahalla2, kocha2]
# # print(f'{r1[0].capitalize()} viloyati,', f'{r1[1].capitalize()} shahar,', f'{r1[2].capitalize()} mahallasi,', f'{r1[3].title()} ko\'chasi.')
# # print(f'{r1[0].capitalize()} viloyati,','\n' f'{r1[1].capitalize()} shahar,', '\n' f'{r1[2].capitalize()} mahallasi,', '\n' f'{r1[3].title()} ko\'chasi.')


# viloyat3 = 'Qashqadaryo'
# shahar3 = 'Qarshi'
# mahalla3 = 'Olmazor'
# kocha3 = 'A.Tutzor'
# # asd = " {} viloyat, {} shahar, {} mahallasi, {} ko'chasi."
# # print(asd.format(viloyat3, shahar3, mahalla3, kocha3))
# print(f'{viloyat3} viloyati, {shahar3} shahar, {mahalla3} mahallasi, {kocha3} ko\'chasi')


# # qo'shimcha
# # viloyat3 = 'qashqadaryo'
# # shahar3 = 'qarshi'
# # mahalla3 = 'olmazor'
# # kocha3 = 't.tutzor'
# # w1 = [viloyat3, shahar3, mahalla3, kocha3]
# # print(f'{w1[0].capitalize()} viloyati,', f'{w1[1].capitalize()} shahar,', f'{w1[2].capitalize()} mahallasi,', f'{w1[3].title()} ko\'chasi.')
# # print(f'{w1[0].capitalize()} viloyati,','\n' f'{w1[1].capitalize()} shahar,', '\n' f'{w1[2].capitalize()} mahallasi,', '\n' f'{w1[3].title()} ko\'chasi.')


# viloyat4 = 'Xorazm'
# shahar4 =  'Xiva'
# mahalla4 = 'Qorovul'
# kocha4 = 'B.Qaroqchi'
# # asd = " {} viloyat, {} shahar, {} mahallasi, {} ko'chasi."
# # print(asd.format(viloyat4, shahar4, mahalla4, kocha4))
# print(f'{viloyat4} viloyati, {shahar4} shahar, {mahalla4} mahallasi, {kocha4} ko\'chasi')

# # qo'shimcha
# viloyat4 = 'xorazm'
# shahar4 =  'xiva'
# mahalla4 = 'qorovul'
# kocha4 = 'q.qaroqchi'
# q1 = [viloyat4, shahar4, mahalla4, kocha4]
# print(f'{q1[0].capitalize()} viloyati,', f'{q1[1].capitalize()} shahar,', f'{q1[2].capitalize()} mahallasi,', f'{q1[3].title()} ko\'chasi.')
# print(f'{q1[0].capitalize()} viloyati,','\n' f'{q1[1].capitalize()} shahar,', '\n' f'{q1[2].capitalize()} mahallasi,', '\n' f'{q1[3].title()} ko\'chasi.')


# viloyat5 = 'Surxandaryo'
# shahar5 = 'Termiz'
# mahalla5 = 'N.Qwerty'
# kocha5 = 'A.Oripov'
# asd = " {} viloyat, {} shahar,  {} mahallasi, {} ko'chasi."
# print(asd.format(viloyat5, shahar5, mahalla5, kocha5))
# print(f'{viloyat5} viloyati, {shahar5} shahar, {mahalla5} mahallasi, {kocha5} ko\'chasi')


#qo'shimcha
# viloyat5 = 'surxandaryo'
# shahar5 = 'termiz'
# mahalla5 = 'qwerty'
# kocha5 = 'a.oripov'
# v1 = [viloyat5, shahar5, mahalla5, kocha5,]
# print(f'{v1[0].capitalize()} viloyati,', f'{v1[1].capitalize()} shahar,', f'{v1[2].capitalize()} mahallasi,', f'{v1[3].title()} ko\'chasi.')
# print(f'{v1[0].capitalize()} viloyati,','\n' f'{v1[1].capitalize()} shahar,', '\n' f'{v1[2].capitalize()} mahallasi,', '\n' f'{v1[3].title()} ko\'chasi.')

# -------------------------------------------------------------3--------------------------------------------------------------

# viloyat1 = 'toshkent'
# shahar1 = 'toshkent'
# mahalla = 'gulzor mahallasi'
# kocha = 't.haqiqat'
# print(viloyat1.upper(), shahar1.upper(), mahalla.capitalize(), kocha.title())

# viloyat2 = 'sirdaryo'
# shahar2 = 'baxt'
# mahalla2 = 'xazina mahallasi'
# kocha2 = 'y.qrilish'
# print(viloyat2.upper(), shahar2.upper(), mahalla2.capitalize(), kocha2.title())

# viloyat3 = 'qashqadaryo'
# shahar3 = 'qarshi'
# mahalla3 = 'olmazor mahallasi'
# kocha3 = 'a.tutzor'
# print(viloyat3.upper(), shahar3.upper(), mahalla3.capitalize(), kocha3.title())

# viloyat4 = 'xorazm'
# shahar4 =  'xiva'
# mahalla4 = 'qorovul mahallasi'
# kocha4 = 'b.qaroqchi'
# print(viloyat4.upper(), shahar4.upper(), mahalla4.capitalize(), kocha4.title())

# viloyat5 = 'surxandaryo'
# shahar5 = 'termiz'
# mahalla5 = 'qwerty mahallasi'
# kocha5 = 'a.oripov'
# print(viloyat5.upper(), shahar5.upper(), mahalla5.capitalize(), kocha5.title())



# ===============================================uyga vazifa===============================================================

# ____________________________________________________1___________________________________________________________________ 

# dad = 'abduxalil oripov fayzullayevich'
# dadyil = 1971
# dadyosh = 53
# dadlive = ['sirdaryo viloyati', 'baxt shahar']
# print(dad.title(), dadyil, dadyosh, dadlive[0].capitalize(), dadlive[1].capitalize())
# print(f'Dadajonim {dad.title()}. U {dadyil} yilda tavallud topgan. Oktabr oyida {dadyosh} yoshga to\'ladi. {dadlive[0].capitalize()} {dadlive[1].capitalize()}da istiqomat qiladi.')


# mum = 'adolar oripova artikulovna'
# mumyil = 1978 
# mumyosh = 46 
# mumlive = ['sirdaryo viloyati', 'baxt shahar']
# print(mum.title(), mumyil, mumyosh, mumlive[0].capitalize(), mumlive[1].capitalize())
# print(f'Onajonim {mum.title()}. U {mumyil} yilda tavallud topgan. Yanvar oyida {mumyosh} yoshga to\'ladi. {mumlive[0].capitalize()} {mumlive[1].capitalize()}da istiqomat qiladi.')


# bro = 'muhammadali fayzullayev abduxalil', 'o\'g\'li'
# broyil = 2002
# broyosh = 22 
# brolive = ['sirdaryo viloyati', 'baxt shahar']
# print(bro[0].title(), bro[1].capitalize(), broyil, broyosh, brolive[0].capitalize(), brolive[1].capitalize())
# print(f'Akajonim {bro[0].title()} {bro[1].capitalize()}. U {broyil} yilda tavallud topgan. Iyul oyida {broyosh} yoshga to\'ladi. {brolive[0].capitalize()} {brolive[1].capitalize()}da istiqomat qiladi.')


# sis1 = 'xabubullayeva nisoatxon abduxalil qizi'
# sis1yil = 1999
# sis1yosh = 25
# sis1live = ['sirdaryo viloyati', 'xovos tuman']
# print(sis1.title(), sis1yil, sis1yosh, sis1live[0].capitalize(), sis1live[1].capitalize())
# print(f'Opajonim {sis1.title()}. U {sis1yil} yilda tavallud topgan. Sentabr oyida {sis1yosh} yoshga to\'ladi. {sis1live[0].capitalize()} {sis1live[1].capitalize()}ida istiqomat qiladi.')


# sis2 = 'kimyoxon fayzullayeva abduxalil qizi'
# sis2yil = 2007
# sis2yosh = 17
# sis2live = ['sirdaryo viloyati', 'baxt shahar']
# print(sis2.title(), sis2yil, sis2yosh, sis2live[0].capitalize(), sis2live[1].capitalize())
# print(f'Singlim {sis2.title()}. U {sis2yil} yilda tavallud topgan. Dekabr oyida {sis2yosh} yoshga to\'ladi. {sis2live[0].capitalize()} {sis2live[1].capitalize()}da istiqomat qiladi.')

# _________________________________________________2-3__________________________________________________________________


# dad = 'abduxalil ORIpov FAYzullaYEVICH'
# dadyil = 1971
# dadyosh = 53
# dadlive = ['sirdaryo viloyati', 'baxt shahar']
# dadmatn = "Dadajonim {}. U {}-yilda tavallud topgan. Oktabrda {} yoshga to'ladi. {} {}da istiqomat qiladi."
# print(dadmatn.format(dad.lower().title(), dadyil, dadyosh, dadlive[0].capitalize(), dadlive[1].capitalize()))
# print(dadmatn.count('a'), dadmatn.count('b'), dadmatn.count('c'), dadmatn.count('d'), dadmatn.count('e'), dadmatn.count('f') )
# print(f'{dad}{dadlive}{dadmatn}'.count('a'),'\n', f'{dad}{dadlive}{dadmatn}'.count('b'),'\n', f'{dad}{dadlive}{dadmatn}'.count('c'),'\n', f'{dad}{dadlive}{dadmatn}'.count('d'),'\n', f'{dad}{dadlive}{dadmatn}'.count('e'),'\n', f'{dad}{dadlive}{dadmatn}'.count('f'),'\n',)

# mum = 'adolar oripova artikulovna'
# mumyil = 1978 
# mumyosh = 46 
# mumlive = ['sirdaryo viloyati', 'baxt shahar']
# mummatn = "Onajonimjonim {}. U {}-yilda tavallud topgan. Oktabrda {} yoshga to'ladi. {} {}da istiqomat qiladi."
# print(mummatn.format(mum.title(), mumyil, mumyosh, mumlive[0].capitalize(), mumlive[1].capitalize()))
# print(mummatn.count('a'), mummatn.count('b'), mummatn.count('c'), mummatn.count('d'), mummatn.count('e'), mummatn.count('f') )
# print(f'{mum}{mumlive}{mummatn}'.count('a'),'\n', f'{mum}{mumlive}{mummatn}'.count('b'),'\n', f'{mum}{mumlive}{mummatn}'.count('d'),'\n', f'{mum}{mumlive}{mummatn}'.count('e'),'\n', f'{mum}{mumlive}{mummatn}'.count('f'),'\n',)


# bro = ['muhammadali fayzullayev abduxalil', 'o\'g\'li']
# broyil = 2002
# broyosh = 22
# brolive = ['sirdaryo viloyati', 'baxt shahar']
# bromatn = "Akajonim {} {}. U {}-yilda tavallud topgan. Oktabrda {} yoshga to'ladi. {} {}da istiqomat qiladi."
# print(bromatn.format(bro[0].title(), bro[1].capitalize(), broyil, broyosh, brolive[0].capitalize(), brolive[1].capitalize()))
# print(bromatn.count('a'), bromatn.count('b'), bromatn.count('c'), bromatn.count('d'), bromatn.count('e'), bromatn.count('f') )
# print(f'{bro}{brolive}{bromatn}'.count('a'),'\n', f'{bro}{brolive}{bromatn}'.count('b'),'\n', f'{bro}{brolive}{bromatn}'.count('c'),'\n', f'{bro}{brolive}{bromatn}'.count('d'),'\n', f'{bro}{brolive}{bromatn}'.count('e'),'\n', f'{bro}{brolive}{bromatn}'.count('f'))


# sis1 = 'xabubullayeva nisoatxon abduxalil qizi'
# sis1yil = 1999
# sis1yosh = 25
# sis1live = ['sirdaryo viloyati', 'XOVOS tumani']
# sis1matn = "Opajonim {}. U {}-yilda tavallud topgan. Oktabrda {} yoshga to'ladi. {} {}da istiqomat qiladi."
# print(sis1matn.format(sis1.title(), sis1yil, sis1yosh, sis1live[0].capitalize(), sis1live[1].lower().capitalize()))
# print(sis1matn.count('a'), sis1matn.count('b'), sis1matn.count('c'), sis1matn.count('d'), sis1matn.count('e'), sis1matn.count('f') )
# print(f'{sis1}{sis1live}{sis1matn}'.count('a'),'\n', f'{sis1}{sis1live}{sis1matn}'.count('b'),'\n', f'{sis1}{sis1live}{sis1matn}'.count('d'),'\n', f'{sis1}{sis1live}{sis1matn}'.count('e'),'\n', f'{sis1}{sis1live}{sis1matn}'.count('f'))

# sis2 = 'kimyoxon fayzullayeva abduxalil qizi'
# sis2yil = 2007
# sis2yosh = 17
# sis2live = ['sirdaryo viloyati', 'baxt shahar']
# sis2matn = "Singlim {}. U {}-yilda tavallud topgan. Oktabrda {} yoshga to'ladi. {} {}da istiqomat qiladi."
# print(sis2matn.format(sis2.title(), sis2yil, sis2yosh, sis2live[0].capitalize(), sis2live[1].capitalize()))
# print(sis2matn.count('a'), sis2matn.count('b'),sis2matn.count('c'), sis2matn.count('d'), sis2matn.count('e'), sis2matn.count('f') )
# print(f'{sis2}{sis2live}{sis2matn}'.count('a'),'\n', f'{sis2}{sis2live}{sis2matn}'.count('b'),'\n', f'{sis2}{sis2live}{sis2matn}'.count('c'),'\n', f'{sis2}{sis2live}{sis2matn}'.count('d'),'\n', f'{sis2}{sis2live}{sis2matn}'.count('e'),'\n', f'{sis2}{sis2live}{sis2matn}'.count('f'))

# m1 = '"KOENIGSEGG CCXR TREVITA"' 
# rang1 = 'qora'
# narx1 =  48_000_000
# matn1 = 'Men dadajonimga {} nomli {} rangdagi mashinani ${} ga sotib oldim'
# m2 = 'LAMBORGINI VENENO ROADSTER'
# rang2 = 'oq'
# narx2 = 45_000_000 
# matn2 = 'Men onajonimga {} nomli {} rangdagi mashinani ${} ga sotib oldim'
# m3 = 'LYKAN HYPERSPORT' 
# rang3 = 'moviy'
# narx3 = 34_000_000
# matn3 = 'Men opajonimga {} nomli {} rangdagi mashinani ${} ga sotib oldim'
# m4 = 'LIMITED EDITION BUGATTI VEYRON BY MANSORY VIVERE'
# rang4 = 'yashil'
# narx4 = 30_000_000
# matn4 = 'Men singlimga {} nomli {} rangdagi mashinani ${} ga sotib oldim'

# miyyaginam
# 1
# print(matn1.format(m1, rang1, narx1))
# print(matn2.format(m2, rang2, narx2))
# print(matn3.format(m3, rang3, narx3))
# print(matn4.format(m4, rang4, narx4))
# 2
# print(matn1.format(m1, rang1, narx1),'\n',
#       matn2.format(m2, rang2, narx2),'\n',
#       matn3.format(m3, rang3, narx3),'\n',
#       matn4.format(m4, rang4, narx4))
# 3
# print(f'Men dadajonimga {m1} nomli {rang1} rangdagi mashinani ${narx1} ga sotib oldim'.count('a'))
# print(f'Men onajonimga {m2} nomli {rang2} rangdagi mashinani ${narx2} ga sotib oldim'.count('b'))
# print(f'Men onajonimga {m4} nomli {rang4} rangdagi mashinani ${narx4} ga sotib oldim'.count('c'))
# print(f'Men onajonimga {m3} nomli {rang3} rangdagi mashinani ${narx3} ga sotib oldim'.count('d'))
# print(f'Men onajonimga {m4} nomli {rang4} rangdagi mashinani ${narx4} ga sotib oldim'.count('e'))
# print(f'Men onajonimga {m4} nomli {rang4} rangdagi mashinani ${narx4} ga sotib oldim'.count('f'))
# 4
# print(matn1.format(m1, rang1, narx1).count('a'))
# print(matn2.format(m2, rang2, narx2).count('b'))
# print(matn3.format(m3, rang3, narx3).count('c'))
# print(matn4.format(m4, rang4, narx4).count('d'))
# print(matn4.format(m4, rang4, narx4).count('e'))
# print(matn4.format(m4, rang4, narx4).count('f'))
# 5
# print(f'{m1.lower()}{rang1}{matn1}{m2}{rang2}{matn2}{m3}{rang3}{matn3}{m4}{rang4}{matn4}'.count('a'))
# print(f'{m1.lower()}{rang1}{matn1}{m2}{rang2}{matn2}{m3}{rang3}{matn3}{m4}{rang4}{matn4}'.count('b'))
# print(f'{m1.lower()}{rang1}{matn1}{m2}{rang2}{matn2}{m3}{rang3}{matn3}{m4}{rang4}{matn4}'.count('c'))
# print(f'{m1.lower()}{rang1}{matn1}{m2}{rang2}{matn2}{m3}{rang3}{matn3}{m4}{rang4}{matn4}'.count('d'))
# print(f'{m1.lower()}{rang1}{matn1}{m2}{rang2}{matn2}{m3}{rang3}{matn3}{m4}{rang4}{matn4}'.count('e'))
# print(f'{m1.lower()}{rang1}{matn1}{m2}{rang2}{matn2}{m3}{rang3}{matn3}{m4}{rang4}{matn4}'.count('f'))
# print(f'{m1.lower()}{rang1}{matn1}{m2}{rang2}{matn2}{m3}{rang3}{matn3}{m4}{rang4}{matn4}'.count('g'))
# 6
# print(f'{matn1, m1.lower(), rang1, m2.lower(), rang2, matn2, m3.lower(), rang3, matn3, m4.lower(), rang4, matn4}'.count('a'), '\n', 
#       f'{matn1, m1.lower(), rang1, m2.lower(), rang2, matn2, m3.lower(), rang3, matn3, m4.lower(), rang4, matn4}'.count('b'), '\n',
#       f'{matn1, m1.lower(), rang1, m2.lower(), rang2, matn2, m3.lower(), rang3, matn3, m4.lower(), rang4, matn4}'.count('c'),'\n',
#       f'{matn1, m1.lower(), rang1, m2.lower(), rang2, matn2, m3.lower(), rang3, matn3, m4.lower(), rang4, matn4}'.count('d'),'\n',
#       f'{matn1, m1.lower(), rang1, m2.lower(), rang2, matn2, m3.lower(), rang3, matn3, m4.lower(), rang4, matn4}'.count('e'),'\n',
#       f'{matn1, m1.lower(), rang1, m2.lower(), rang2, matn2, m3.lower(), rang3, matn3, m4.lower(), rang4, matn4}'.count('f'),'\n',)





