# ___________________________________________Variables (o'zgaruvchilar)______________________________________________________

# O'zgaruvchilarninomlashda quyidagi qoidalarga amal qilish kerak:

# 1. O'zgaruvchi nomi harf/_ bilan boshlanishi mumkin;
# 2. O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas! HATOLIK beradi, lekin orasida qatnashishi mumkin;
# 3. o'zgaruvchi nomi faqat lotin alifbosi harflarida (A - z), raqamlar/sonlar va _ qatnashishi mumkin;
# 4. O'zgaruvchilarni e'lon qilayotganda orasida probel tashab yozish HATOLIK beradi;
# 5. O'zgaruvchi nomida bosh va kichik harflar turlicha talqin qilinadi ya'ni harxil o'zgaruvchi sifatida qaraladi(ISM, ism, Ism, iSm,iSM, isM)

# Qo'shimcha qoida sinfatida:

# 1. O'zgaruvchilar nomini kichik harflar bilan yozishimish kerak;
# 2. O'zgaruvchilar nomida 2 ta so'z bo'lsa _ bilan ajratib yozing (ism_familiya = "Otajon Bozorboyev");
# 3. O'zgaruvchilar nomida 2 ta va undan ortiq so'z qatnashgan bo'lsa "tuyaQilib" ya'ni (camelCase) qilib yozish mumkin - (joriyYil = 2024)
# 4. O'zgaruvchilar nomida 2 ta va undan ortiq so'z qatnashgan bo'lsa birinchi harfini katta harf bilan ya'ni (PaskalCase) ko'rinishida yozish mumkin - (MyVariableName = 'Moxiraxon') 
# 5. O'zgaruvchilar nomida 2 ta va undan ortiq so'z qatnashgan bo'lsa "Ilon qilib" ya'ni (Snake Case) usulida yozish mumkin -mening_tavallud_topgam_yilim = 2004
# 6. O'zgaruvchilarga o'zingiz tushunadigan qilib nom bering (y=20 emas. d="Korea" emas, yosh=20, davlat="Korea")
# 7. O'xgaruvchilarga nom berishda Pythonda ishlatiladigan maxsus keywordlardan (KALIT SO'ZLAR) foydalanish HATOLIK beradi (for, if,)


#____________________________________O'zgaruvchilar turlari (DATA TYPES)_____________________________________________________

# Pythonda o'zgaruvchilar (data type turlari) PRIMITIVE VA NON PRIMITIVE ga bo'linadi:

#_______________________________________________PRIMITIVE____________________________________________________________________

# string - "Matn" qisqartmasi python kodlarda (str) yoziladi (faqat matnlarga javob beradi)
# integers - BUTUN SONLAR qisqartmasi python kodlarda (int) yoziladi: 10, 4, 9, 5
# float - O'NLIK SONLAR python kodlarda (float) yoziladi: 10.2, 10.0, 5.8, 9.0
# boolean - TRUE/FALSE qaytaradi ya'ni to'g'ri yoki noto'g'ri, ha yoki yo'q, + yoki -

# ________________________________NON PRIMITIVE__________________________________
# 1. List - list
# 2. Tupple - tuple
# 3. Set - set
# 4. Diktionsry -diktionary



# ___________________________________________primitive data type____________________________________________________________
# Namuna:

# print(type(7)) #int
# print(type(5.3)) #float
# print(type(5-2)) #int
# print(type(5/2)) #float
# print(type(5//2)) #int
# print(type('5')) #str
# print(type('b')) #str
# print(type(5-5==0)) #bool
# print(type(1234567987654454567)) #int


# d = 'Uzbekistan' deb ketish kerak emas chunki bundan tashqari yana ko'plab o'zgaruvchi kelishi mumkin
# keyin yuqoridagi d ni nima uchun ochganimiz esimizdan chiqib qolishi mumkin shuning uchun pastdagi dek o'zgaruvchi ochiladi
# davlat = 'Uzbekistan'

# ________________________________________________integerni (int)____________________________________________________________
# ikki xil e'lon qilish usuli bor

# a = 15 odatda bundan ko'proq foydalaniladi
# a = int(25) bundan type berib ketishda asosan dasturlarni ichida foydalaniladi


# qo'shimcha ma'lumot:
# tresh sonlar degan narsa bor lekin ular pythonda mavjud emas

# a = int() bo'lganida bu - # 0 ga teng bo'ladi
# -5848765432345678765434567 bo'lmaydi

# a = int()
# print(a)

# python javadan sekin ishlidi, kompyuter tepadan pastga o'ngdan chapga qarab o'qiydi

# a = str()
# a = ''
# print(a)

# a = float()
# a = 0.0
# print(a)

# a = 5*5+1.0
# print(a) #qiymatti o'zlashtiradi
# print(type(a))

# a = not True # booleanda falsega teng bo'ladi
# a = not False # booleanda truega teng  bo'ladi
# a = True 
# a = False
# print(a)

# a = bool() # bunda xechnarsa berilmaganligi uchun False qaytaradi
# print(a)

# True ning defold holati = 1 ga 
# False ning defold holati = 0 ga

# string ichida yana bir ajoyib narsasi bor:

# matn = "Men yangi 💻 sotib oldim!"
# print(matn)

# ya'ni  (str) emojilarni ham qabul qiladi ularni ham matn deb o'qiydi (lekin giflarni joylashtirib yurish kerak emas)

#________________________________________________UYGA VAZIFALAR______________________________________________________________

# ______________________________________________________1___________________________________________________________________

# qulupnay = '🍓'
# olma = '🍎'
# banan = '🍌'
# quloqchin = '🎧'
# kampyuter = '💻'
# barg = '🍁'
# televizor = '📺'
# yakkashoh = '🦄'
# ot = '🐎'
# telefon = '☎'
# flamingo = '🦩'
# print(qulupnay, olma, banan, quloqchin, kampyuter, barg, televizor, yakkashoh, ot, telefon, flamingo)

# ______________________________________________________2____________________________________________________________________

# arab
# صفر = '٠'
# وَاحِد = '١'
# اِثْنَان = '٢'
# ثَلَاثَة = '٣'
# أَرْبَعَة = '٤'
# خَمْسَة = '٥'
# سِتَّة = '٦'
# سَبْعَة = '٧'
# ثَمَانِيَة = '٨'
# تِسْعَة = '٩'

# yapon
# rei = '零'
# ichi = '一'
# ni = '二'
# san = '三'
# yon = '四'
# go = '五'
# roku = '六'
# nana = '七'
# hachi = '八'
# kyu = '九'

# print(rei,ichi, ni, san, yon, go, roku, nana, hachi, kyu)

# ______________________________________________________3________________________________________________________________

# qoraqalpogiston = 'Қарақалпақстан'
# toshkent = 'Ташкент'
# sirdaryo ='Сирдарё'
# navoiy = 'Навоий'
# jizzax = 'Жиззах'
# xorazm = 'Хоразм'
# buxoro = 'Бухоро'
# surxandaryo = 'Сурхандарё'
# namangan = 'Наманган'
# andijon = 'Андижон'
# qashqadaryo = 'Қашкадарё'
# samarqand = 'Самарқанд'
# fargona = 'Фарғона'
# print(qoraqalpogiston, toshkent, sirdaryo, navoiy, jizzax, xorazm, buxoro, surxandaryo, namangan, andijon, qashqadaryo, samarqand, fargona)

# фарғона = 'Fargona'
# самарқанд = 'Samarqand'
# қашкадарё = 'Qashqadaryo'
# андижон = 'Andijon'
# наманган = 'Namangan'
# сурхандарё = 'Surxandaryo'
# хоразм = 'Xorazm' 
# жиззах = 'Jizzax'
# навоий = 'Navoiy'
# сирдарё = 'Sirdaryo'
# ташкент = 'Toshkent'
# қарақалпақстан = 'Qoraqalpog\'iston'
# бухоро = 'Buxoro'
# print(бухоро)

