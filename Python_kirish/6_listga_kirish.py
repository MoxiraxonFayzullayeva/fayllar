# ________________________________NON PRIMITIVE__________________________________
# 1. List - list
# 2. Tupple - tuple
# 3. Set - set
# 4. Diktionsry -diktionary


# ___________________________________LIST_________________________________________

# list() - bu inglizchadan olingan bo'lib ro'yxat degani
# list() - o'zgaruvchida [] to'rtburchak qavs orqali ichiladi
# list() ichiga str float bool int ni hammasini qabul qiladi
# listni ikki xil elon qilinish ko'rinishi bor
# a =[]
# a = list()

# a = ['moxiraxon', 12.0, True, False, 15]
# print(type(a))

# mevalar = ['lemon', 'olma', 'qulupnay', 'banan']
# qiymatlar = [10_000, 15_000] 
# ismlar = []

# print(mevalar)
# print(qiymatlar)
# print(ismlar)

# list() indekslangan bo'ladi(indekslanganda len() berilsa 1 dan boshlab sanaydi)
# print(len(mevalar))

# ko'ramiz string medotlarini qollasa ham boladi
# print(f'Menga {mevalar[3].upper()} yoqadi')

# integer bo'lsa qiymatlarni qo'shsak bizga yig'indisini chiqarib beradi
# print(qiymatlar[0] + qiymatlar[1])

# kurs = ['odina', 'moxira', 'ismigul']
# print(len(kurs)) #listda turibdi
# print(kurs[0]) #kursning 0-indeksi odina
# print(type(kurs[0])) #string
# print(len(kurs[0])) #faqatgina 0-indeksning uzunligini hisoblab berdi
# print(len(kurs)) #listning ichidagi indeksni aniqlab berdi
# kurs[0] = 25_000 #kursing 0-indeksi fotimani 25_000 ga o'zgartiraman
# print(kurs) # endi kurs ning 0-indeksi fotimaga emas balki 25_000 ga o'zgardi
# print(kurs[0]) #kurning 0- indeksi 25_000
# print(kurs) #integer 

# _________________________________LIST METODLARI________________________________


# _____________________________________APPEND______________________________________


# append() - o'zida STRING malumot qaytaradi
# insert() - vazifasi da binchi indeks kiritiladi keyin shu indeksda 
# nima joylashishini hohlasak shuni kiritamiz
# sinf = []
# sinf.append('moxira')
# sinf.append('raxmatilla'.title())
# sinf.append(input("Ma'limot kiriting: ").title()) #agar biz userdan olmoqchi bo'lsak
# sinf.insert(0, 'alimjon'.title()) 
# # print(sinf)

# ___________________________________ELEMENTLARNI O'CHIRISH_____________________________


# # del() - delete o'zgaruvchining inderksi boyicha ham o'zgaruvchining o'zini ham o'chirib beradi kiritilsa
# del() ga qayta murojaat qilinganda xatolik qaytaradi (none)
# del(sinf[0]) # yuqorida kiritilgan 0-indeksdagi 'Alimjon' ni chopadi
# print(sinf)
# del(sinf) #yuqoridagi o'zgaruvchini butunlay chopadi xatolik qaytaradi chunki unday narsa umuman yoq deb qabul qiladi
# print(sinf)
 
# sinf.remove('Alimjon') 
# print(sinf)
# sinf.pop() #agar qiymat kiritilmasa oxirgi indeks bo'yicha chopadi
# sinf.pop(0) #berilgan index raqamidagi qiymatni chopadi
# print(sinf)

# son = sinf.pop() # bu yerda hozir pop boyicha chopilgan 'Rahmatilla' songa teng
# print(son) # run berilganda 'Rahmatilla ' sonda saqlanib  
# print(sinf)

# ________________________________________del() vs clear()_____________________________________ 

# del() o'chirish uchun qayta murojaat qilganda xotirada qolmaydi xechnarsa
# clear() tozalash uchun ishlatilinadi
# clear() - tozalash uchun ishlatilinadi, qayta murojaat qilganda pustoy list qaytaradi

# sinf.clear() # [] list() ni o'zi qaytadi
# print(sinf)


# _________________________________________[start:end:step]__________________________

# indekslardagi kesish listga ham o'tadi

# ism = ['shoxrux', 'moxiraxon', 'alimjon', 'abbos', 'ilhom']
# print(f"{ism[1:-1:2]}")


# _______________________________________UYGA VAZIFA___________________________________

# ___________________________________________1___________________________________________


# ismlar = ['sitora', 'nargiza', 'gulnoza', 'muyassar,', 'sevinch', 'ismigul']
# print(f'{ismlar[0].title()} va {ismlar[1].title()} bilan 32-maktanda birga o\'qiganmiz. {ismlar[2].title()} esa 7-maktabdagi sinfdoshim.', 
#       ismlar[3].title(), ismlar[4].title(), 'kursdoshlarim.', ismlar[-1].capitalize(), 'esa dugonam.')


# # ___________________________________________2_____________________________________________


# son = [12, 34, 654, 962, 268, 258, 987, 1038, 85, 2, 1, int(input('Son kiriting: '))]
# print(son[0]*son[-2], son[1]**son[-3], son[4]-son[5]+son[3], son[-5]/son[-3], son[-4]**3, son[6]//son[-4], son[2]%4, '\n',
#       f"""
# {son[-1]} x 1 = {son[-1]*1}
# {son[-1]} x 2 = {son[-1]*2}
# {son[-1]} x 3 = {son[-1]*3}
# {son[-1]} x 4 = {son[-1]*4}
# {son[-1]} x 5 = {son[-1]*5}
# {son[-1]} x 6 = {son[-1]*6}
# {son[-1]} x 7 = {son[-1]*7}
# {son[-1]} x 8 = {son[-1]*8}
# {son[-1]} x 9 = {son[-1]*9}
# {son[-1]} x 10 = {son[-1]*10}
# """)

 # ___________________________________________3________________________________________________

# tarix = ['Amir Temur', 'Alisher Navoiy', 'Al-Buxoriy', 'Ibn Sino', 'Imom Muslim', 'aslida juda ko\'p']
# amir_temur = tarix.pop(0)
# kop = tarix.pop()
# alisher_navoiy = tarix.pop(0)
# ibn_sino = tarix.pop(1)
# al_buxoriy = tarix.pop(0)
# imom_muslim = tarix.pop()
# print(amir_temur+" - Temurlilar uyg'onish davri yaratuvchisi, ilm-fan, me'morchilik, san'at va adabiyot homiysi. Shabon oyining yigirma beshida, hijriy yetti yuz o'ttiz oltinchi yilda tavallud topgan.")
# print(alisher_navoiy, "ijodining yuksak cho'qqisi \"Xamsa\" asaridir,")
# print(ibn_sino, "o'rta osiyolik Fors qomusiy olimi, tabib va faylasuf. Olimning falsafaga oid eng yirik va muhim asari \"Kitob ash-shifo\"dir.")
# print(al_buxoriy+"ning - asl ismi Abu Abdulloh Muhammad ibn Ismoil ibn Ibrohim al Buxoriy.")
# print(imom_muslim+"ning - asl ismi Abu Al-Husayn Muslim ibn Al-Hajjaj.")
# print(f"Men hurmat qiluvchi tarixiy shaxslar {kop}.")

# hozir = ['Hasanxon Yaxyo Abdulmajid', 'Nuriddin Xoliqnazarov', 'Abdulloh Domla', 'ustozlarim']
# hasanxon_yaxyo_abdulmajid = hozir.pop(0)
# ustozlarim = hozir.pop()
# nuriddin_xoliqnazarov = hozir.pop(0)
# abdulloh_domla = hozir.pop()
# print(f"{hasanxon_yaxyo_abdulmajid} 1981-yil 12-yanvarda Andijon shahrida tavallud topgan. Hozirda {2024-1981} yoshda.")
# print(nuriddin_xoliqnazarov, "1968-yilda Asaka shahrida tug'ilgan Toshkentning bosh imom-xatibi, O'zbekistonning bosh muftiysi va O'zbekiston musulmonlari idorasi raisi.")
# print(abdulloh_domla, "Qirg'izistolik men judaham ma'vizalarini yaxshi ko'rib eshitivchi domla." )
# print(f'Albatta menga bilim bergan {ustozlarim}ning barchasini ham yaxshi ko\'raman hurmat qilaman.')




























