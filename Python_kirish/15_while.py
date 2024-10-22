# _______________________TAKRORLANISH OPERATORLARI _2________________________________

# takrorlanish operatorlari ikta bolib ular: for/while edi
# for ni o'tib bo'lgan edik
# for da bir o'zgaruvchini to oxirgi indeksiga bormagunicha to'xtamaydi
# for ichida o'zgaruvchi ochishga majburmiz

#_________________________________while_______________________________________________

# while - esa mantiqiy hatolikka yo'l qo'yilsa cheksiz ketib qoladi yoki 
# umuman ishlamay qolishimumkin
# while - ichida o'zgaruvchi ochishga majbur emasmiz faqat shart berib ishlatsak bo'ladi
# shartdan o'tsagina yoki o'tmasagina shunda ishlab ketishi mumkin

# number = 1
# while number <=10:
#     print(number, end=" ") #agar dastur 10 dan katta bo'lib qolsa dastur tugaydi
#     # hozir o'zgaruvchi while ichidagi shartdan kichik bo'lganligi sababli dastur davom etib ketadi
#     #faqat cheksiz! Chunki biz o'zgaruvchini o'sib boruvchi qilmadik uni to'xtatish uchun CTRL+C tugmasini bosamiz
#     # agar hozir biz:
#     number += 1 # qilib o'zgaruvchini o'sib boruvchi qilib qo'ysak,
#     #dastur while ichidagi shartdan o'tguncha ishlaydi keyin esa to'xtaydi
# print('Dastur tugadi')


# question = "Ixtiyoriy son kiriting:\n"
# question += "To'xtash uchun 'exit' deb yozing. "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(question).lower()
#     if qiymat != 'exit':
#         print(float(qiymat) ** 3)
#     print('Dastur tugadi!')


# qiymat = ''
# a = True
# while a:
#     qiymat = input("Ixtiyoriy son kiriting: ")
#     if qiymat.lower() == 'exit':
#         a = False
#     else:
#         print(float(qiymat ** 3)) #nima uchunn int ishlatib bo'lmayapti


# print("Istalgan sonning kvadratini chiqaruvchi dastur!")
# while True:
#     number = input("Son kiriting: ")
#     if number.lower() == 'exit':
#         print("Dastur tugadi!")
#         break
#     else:
#         print(int(number) ** 2)


# son = int(input('~ '))
# while son != 10+1: # 11
#     print(son)
#     son += 1
# nums = list(range(1, 11+1))
# for i in nums:
#     if i == 5:
#         break
#     print(f'{i} ning kubi {i ** 3} ga teng.')

# nums = list(range(1, 11+1))
# for i in nums:
#     if i == 5 or i == 8 or i == 9:
#         continue
#     print(f'{i} ning kubi {i ** 3} ga teng.')


# matn = input('Kiriting: ')
# soz = ''
# lst = ['a', 'e', 'i', 'o', 'u']
# for i in matn:
#     if i in lst:
#         soz += '$'
#     else:
#         soz += i
# print(soz) #tushunmadim



# son = 1
# juft = []
# toq = []
# while son <=101:
#     if son % 2 == 0:
#         juft.append(son)
#     else:
#         toq.append(son)
#     son += 1
# print(f'Juft sonlar {juft}')
# print(f'Toq sonlar {toq}')


# _________________________SINF ISH / UY ISHI_________________________________________

# __________________________1_________________________________________________________


# film = ''
# sign = True
# while sign:
#     film = input("Film kiriting: ")
#     if film == 'exit' or film == 'stop':
#         print("Dastur tugadi!")
#         sign = False

# ____________________________2 / 3_________________________________________________________


# bilet ={
#     'bola': 0,
#     'yosh': 25_000,
#     'orta': 65_0000
# }
# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.lower() == 'exit' or yosh.lower() == 'stop':
#         print("Tugadi")
#         break
#     elif int(yosh) >= 7 and int(yosh) <= 18:
#         print(bilet['yosh'])
#     elif int(yosh) > 18 and int(yosh) < 65:
#         print(bilet['orta'])
#     else:
#         print(bilet['bola'])

























