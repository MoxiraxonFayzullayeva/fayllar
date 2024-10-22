# 'r' -> 'read' ya'ni fileni o'qish uchun ishlatilinadi
# 'w' -> 'write' ya'ni filega yozish uchun ishlatilinadi
# 'a' -> 'append' ya'ni filega ma'lumot qo'shish uchun ishlatilinadi

# with open('pi.txt', 'r') as f:
# with open('pi.txt') as f: # ning defold holati 'r' -> ya'ni 'read' ga teng

    # yuqoridagi ikkalasi ham bir xil vazifani bajaradi ya'ni o'qish uchun

# agar:

### with open('pi.txt', 'w') as f: qilib ochadigan bo'lsak ehtiyot bolishimiz kerak file ichidagi hamma narsani o'chirib yuboradi
#  telefonlarga qanday sbros berilsa shunga o'xshab qoladi 

# bunaqa narsalar ko'p with open('pi.txt', 'shuyerda ahmmasi chiqadi')


# 'r+' -> fileni o'qish va yozish uchun ochish
# 'a+' -> filega ma'lumot qo'shish va o'qish uchun ochish. (file mavjud bo'lmas ayangi file yaratadi)

# with open('teachers.txt', 'w') as f:
#     # f.write('Assalomu alaykum')
#     f.write('Bu dastur yozilgan') # AVVAL YOZGAN Assalomu alaykum ma'lumotimiz o'chib ketadi 


# ism = "otajon bozorboyev".capitalize()
# yosh = 25

# with open('teachers.txt', 'w') as f:
#     f.write(ism + '\n') # write metodi ichiga bitta argument qabul qilganligi uchun vergul bilan yozilmidi vergul o'rniga + belgisidan fiydalanib ketamiz
# #    # f.write(yosh) # txt filega intejer ma'lumot yozilmidi hammasi str ma'lumot bo'ladi buni hozir natijada ham chiqarishimiz mumkin
#     f.write(str(yosh)) # print ichida str() ga olib ketishimiz optimalroq bo'ladi chunki kiritgan integer ma'lumotimiz bizga dastur davomida kerak bo'lib qolishi mumkin 

# run:
# TypeError: write() argument must be str, not int
# xatolik qaytarmasligi uchun f.write(str(yosh))

#################### with open('teachers.py', 'w') as f:
    # f.write("print(\"Hello world!\")") #####################

# with open('teachers.txt', 'a') as f:
#     f.write('\nsaidkamol')
#     f.write('\nsaidkamol')

# Pickle file yozish:

# Pickle pythonnni yuklab olgan vaqtimizda o'zi avtomaticheski mavjud 
# Pickledan foydalanishimiz biz avval bu modulni import qilib olamiz fileni ochishda esa open() funksiyasiga ikkinchi argument sifatida wb 
# va filega yozish uchun esa le.dump() bilan yozib ketamiz

# wr -> write binary (binary -> ikkilik sanoq tizimi degani) yozish uchun
# le.dump() -> f.write() o'rniga pickle da ishlatilinadi yozish uchun
# rb -> read binary -> o'qish uchun
# f.load() -> f.load() -> o'qish uchun
# boshladik:

import pickle 
student1 = {'ism': 'Alimjon', 'familiya': 'Rahmatullayev', 'yoshi': 26}
student2 = {'ism': 'Rakmatulla', 'familiya': 'Alimjonov', 'yoshi': 24}
student3 = {'ism': 'Saidkamol', 'familiya': 'Qudratov', 'yoshi': 18}

with open('info.dat', 'wb') as f: # format berish uchun tavsiya etilinadi file.dat yoki file.info debketish kerak 
# chunki file.txt formatta ochilsa boshqa shunga o'xshagan fileimiz ham bor bo'lsa xatolik qaytarib biz kutgan natijani chiqarmasa 
# nimaga unday bo'lyatganini tushunmay adashib o'tiraveramiz

# shuning uchun pickle da yozganimizda yoki format bermaymiz yoki -----.dat dib ketamiz
    pickle.dump(student1, f)
    pickle.dump(student2, f)
    pickle.dump(student3, f)

with open('info.dat', 'rb') as f:
    talaba1 = pickle.load(f)
    talaba2 = pickle.load(f)
    talaba3  = pickle.load(f)

# qoida: bunda har bir qatorni alohida alohida qilib o'qib olishimiz kerak shu sababli ham bir qatorga alohida o'zgaruvchi oldik sababi kelgusida ishlatishimiz uchun bu qol kelishi mumkin 



print(talaba1)
print(talaba2)
print(talaba3)
