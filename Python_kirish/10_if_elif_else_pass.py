# _____________________IF__ELIF____ELSE_____PASS_______________________________________


# Taqqoslash uchun dasturlashda operatorlar mavjud 
# Tekshirish operatorlari

# if:
# elif - else + if
# else:

# ishlatilishi:
# son = int(input("Ixtiyoriy son kiriting: "))
# if son >= 5: #shu shartdan o'tsa
#     print(son) #son chiqsin
# else: #agar shartdan o'tmas
#     print(f'{son} 5 dan kichkina') # berilgan ma'lumot chiqsin

# a, b =  24, 25
# if a > b:
#     print('A > B')
# else:
#     print('A < B')
# print('a > b') if a > b else print('a < b') # bir qatorli ko'rinishi

# cars = ['maLibu', 'cobalt', 'gentra', 'tahoe'] 
# for i in cars:
#     if i == 'tahoe':
#         print(i.upper())
#     else:
#         print(i.title())



# cars = ['MaLibu', 'CoBalt', 'gentra', 'Tahoe'] # agar shriftlar harxil bo'lsa
# for i in cars:
#     if i.lower() == 'tahoe': # shartda lower() metodini qo'llashimiz kerak bo'ladi
#         print(i.upper())
#     else:
#         print(i.title())


# ismlar = ['moxira', 'Alimjon', 'RahmaTULLA', 'Islombek']
# for ism in ismlar:
#     if ism.lower() == 'moxira' and ism.lower() == 'islombek':  
#         print(ism.upper())
#     else:
#         print(ism.capitalize())

# bu yerda and ishlatganimiz, lekin ism ismlar ichida aylanganida 'moxira'ga qarab 1
#  'islombek'ka qarab esa 0 chiqadi chunki ('moxira'=='moxira' va 'moxira'=='islombek') bo'lib 
# 1*0=0 bo'lib false holatga o'tadi va shartdan o'tmasdan else ga jo'natadi
# agar biz bu yerda or ishlatsak ('moxira'=='moxira' yoki 'moxira'=='islombek') bo'lib 
# 1+0=1 bo'lib true holatga o'tadi va shartga javob berib if da qoladi

# ismlar = ['moxira', 'Alimjon', 'RahmaTULLA', 'Islombek']
# for ism in ismlar:
#     if ism.lower() == 'moxira' or ism.lower() == 'islombek':  
#         print(ism.upper())
#     else:
#         print(ism.capitalize())

# son = int(input('Son: '))
# if son < 0:
#     print("Manfiy.")
# elif son > 0:
#     print("Musbat.")
# # elif son == 0:
# #     print(son)
# else:
#     print(False)
#     pass

#if va else bir martta ishlatilinadi boshida va oxirida, elif esa istalgancha kelishi mumkin


# ______________________kassani algoritmini yozamiz______________________________________

#  1. 
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 7 or yosh >= 65:
#         print("Siz uchun chipta puli bepul!")
# else:
#         print("Siz uchun chipta pullik!")


# 2.
# kun = input("Kunni kirining: ").lower()
# yosh = int(input("Yoshingizni kiriting: "))
# if kun == "juma" and (yosh <= 7 or yosh >= 65 ):
#     print("Tekin!")
# elif kun == "juma" and (yosh > 7 and yosh <=18 ):
#     print("25 000")
# else:
#     print("100 000")
# pass
# # qo'shimcha
# kun = input("Kunni kirining: ").lower()
# yosh = int(input("Yoshingizni kiriting: "))
# print("chipta tekin!") if kun == "juma" and (yosh <= 7 or yosh >= 65) else print("pullik")
# pass

# __________________________________UYGA VAZIFA________________________________
# _______________________1_____________________________________________________


# ________________________2______________________________________________________

# son = int(input("Iltimos juft son kiriting: "))
# if son % 2 == 1:
# # if son % 2 != 0:
#     print('Siz toq son kiritdingin!')
# else:
#     print('Siz imtixondan o\'tdinguz!')
# pass

# _______________________3____________________________________________________________

# yosh = int(input('Yoshingizni kiriting: '))
# if yosh < 7 or yosh > 60:
#     print('Tekin!')
# elif yosh > 7 and yosh < 18:
#     print('5 000 chegirma!')
# else:
#     print('25 000')
# pass

# _______________________4____________________________________________________________

# a = int(input("Son kiriting: "))
# b = int(input("Son kiriting: "))
# c = int(input("Son kiriting: "))

# if a>b>=c:
#     print("a>b>=c")
# elif a>b>=c:
#     print("a>b>=c")
# elif b>a>=c:
#     print("b>a>=c")
# elif c>b>=a:
#     print("c>b>=a")
# elif b>a<=c:
#     print("b>a<=c")
# elif c>b<=a:
#     print("c>b<=a")
# elif a<b>=c:
#     print("a<b>=c")
# elif b<a>=c:
#     print("b<a>=c")
# elif c<b>=a:
#     print("c<b>=a")
# elif a<b<=c:
#     print("a<b<=c")
# elif b<a<=c:
#     print("b<a<=c")
# elif c<b<=a:
#     print("c<b<=a")
# else:
#     print('a=b=c')


# if a>b>c:
#     print("a>b>c")
# elif a>c>b:
#     print("a>c>b")
# elif b>a>c:
#     print("b>a>c")
# elif b>c>a:
#     print("b>c>a")
# elif c>a>b:
#     print("c>a>b")
# else:
#     print('c>b>a')



# _________________________5_________________________________________________

# a = []
# b = []
# son = int(input('Kiriting: '))
# 
#     if son % 2 != 0:
#         print(a.append(i))
#     else:
#         print(b.append(i))

# a = []
# b = []
# son = int(input('Butun son kiriting: '))
# if son % 2 == 0:
#     print(a.append(son))
# else:
#     print(b.append(son))
#     pass


# numbers = list(range(11))
# sonkv = []
# for i in numbers:
#     sonkv.append(i*i) #bitta qiymatti boshqa o'zgaruvchiga o'zlashtirib beradi
# print(sonkv)  



