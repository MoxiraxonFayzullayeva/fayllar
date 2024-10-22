# _____________________________________LIST_2.0_______________________________________________
meva = ['banan', 'qulupnay', 'kiwi', 'olma', 'anor']
# print(meva[2:3+1])

# _________________________________________sort()__________________________________________

# listda sort() degan narsa bor kiritilgan elementlarni tartiblab beradi
# meva.sort() #buni print ichida yozsa none qaytaradi
# print(meva)

# # sortlash metodini ikki xil usuli bor, bittasi qiymat qabul qiladi bittasi qiymat qabul qilmaydi, farqi ishlash tezligida

# ________________________________________sorted()__________________________________________
# sorted(meva) # print ichida ham yozsa bo'ladi
# print(meva)

# sorted() da faqat bitta o'zgaruvchini kiritib tartiblasa bo'ladi

sabzavot = ['sabzi', 'kartoshka', 'piyoz', 'lavlagi', 'karam']
# print(sorted(sabzavot))

# __________________________________reverse=True________________________________________________
# sortlashda reverse=True degan narsa bor -----.sort(reverse=True) shaklida ishlatilinadi
meva.sort(reverse=True) # bunda tartiblangan elementlarni, teskarisiga qilib qo'yadi
print(*meva)
sabzavot.sort(reverse=True) # bunda tartiblangan elementlarni, teskarisiga qilib qo'yadi
print(*sabzavot)

# sabzavot = ['sabzi', 'Kartoshka', 'Piyoz', 'lavlagi', 'karam']
# sabzavot.reverse() #bunda reverse() faqatgina teskari qilib berdi tartiblamadi
# print(sabzavot)
# agar elementlarda bosh harflilari ham bo'lsa unda unda birinchi bosh harflilarni sortlaydi, keyin kichik harflilarni sortlaydi

# sabzavot.sort()
# print(sabzavot)
# sabzavot.sort(reverse=True)
# print(sabzavot)
# print(sorted(sabzavot, reverse=True)) # True ni o'rniga 0 dan katta son qo'yilsa ham bo'ladi
# print(sorted(sabzavot, reverse=3))
# print(sorted(sabzavot))


# sonlar = [54,2,34,87,67,4,42,32,687,8,90,856,78] # integerlarni ham sortlasa bo'ladi
# sonlar.sort()
# print(sonlar)
# print(sorted(sonlar))

# sonlar = [54,2,34,87,67,4,42,32,687,8,90,856,78] # integerlarni ham sortlasa bo'ladi

# sonlar.sort()
# sonlar.reverse()
# print(sonlar)

# sonlar = [54,2,34,87,67,4,42,32,687,8,90,856,78]
# print(len(sonlar)) # len() uzunlikni aniqlab berishi haqida gaplashgan ediga


# sabzavot = ['sabzi', 'Kartoshka', 'Piyoz', 'lavlagi', 'karam']
# sabzavot.append('go\'sht') # list.append() takes exactly one argument 
# sabzavot.extend(['salat', 'olma', 'xurmo']) # tortburchak qavs elementni listda chiqarib beradi
# print(sabzavot)

# _________________________________________id()________________________________________
# # id bu bizga o'zgaruvchimizning hotiradan qayerdan joy eganlaganligini ko'rsatib beradi
# age = [54,2,34,]
# yosh = age #biz bir o'zgaruvchini boshqa bir o'zgaruvchiga o'zlashtirib qo'ysakda,
# ularning xotiradagi o'rni bir joydan o'rin egallaydi  
# print(id(age))
# print(id(yosh))
# biz bunda ularning boshqa boshqa joydan o'rin egallashini hohlasak 
# o'zlashtirilgan o'zgaruvchiga [:] ni qo'shib qo'yishimiz kerak

# age = [54,2,34,]
# yosh = age[:] #endi ularning o'rni boshqa boshqa joyda 
# print(id(age))
# print(id(yosh))

# listda yana range degan narsa bor
#___________________________________________ range()____________________________________
# range()
# [(start, end, step)]
# my_list = list(range(0,10+1))
# # print(my_list)

# juft_sonlar = list(range(0, 10+1, 2))
# toq_sonlar = list(range(1, 10, 2))
# print(f'{juft_sonlar}\n'
#       f'{toq_sonlar}')

# _______________________________renge()da__max(), min(), sum()_________________________________

# max() dan eng ko'pini tanlab berishda foydalanamiz
# min() dan eng kamini tanlab berishda foydalanamiz
# sum() esa elementlarning yig'indisini hisoblab beradi

# a = list(range(0, 10+1)) 
# print(max(a))
# print(min(a))
# print(sum(a))


# _________________________________________UYGA VAZIFA________________________________________

# ____________________________________________1_________________________________________________

# juft = list(range(100, 1500+1, 2))
# toq = list(range(101, 1500+1, 2))
# print(f'{sum(juft)}\n', f'{sum(toq)}')

# _____________________________________________2_________________________________________________

# komandalar = ['Leicester', 'Tottenham', 'Brighton', 'Man Utd', 'Crystal Palace', 'West Ham', 
# 'Fulham', 'Man City', 'Ipswich', 'Southampton', 'Everton', 'Arsenal', 'Liverpool']
# print(*komandalar)
# komandalar.sort()
# print(*komandalar)
# komandalar.sort(reverse=5)
# print(*komandalar)

# ____________________________________________3___________________________________________________

# ism = ['Abduxalil','Nisoatxon','Adolat','Muhammadali','Umida','Kimyoxon','sitora','nargiza','gulnoza','muyassar,','sevinch','ismigul',]
# yosh = [53,25,46,22,23,17,20,20,19,18,21]
# # print(f'{sorted(ism,)}\n' f'{sorted(yosh)}')
# # for i in ism:
# #     for j in yosh:
# matn = ism+yosh
# sorted(matn)
# _______________________________________________4___________________________________________________


# juftSon = list(range(100, 1000+1, 2))
# print(min(juftSon))
# print(max(juftSon))
# toqSon = list(range(101, 1000+1, 2))
# print(min(toqSon))
# print(max(toqSon))

# _________________________________________________5_____________________________________________________


# juftSon = list(range(100, 1000+1, 2))
# toqSon = list(range(101, 1000+1, 2))
# print(len(juftSon))
# print(len(toqSon)









