# __________________________________DEF - 3 / *args - **kwargs__________________________

# def narxini_kirit(nomi):
#     narxlari = {}
#     while nomi:
#         nom = nomi.pop()
#         summa = input(f"{nom.title()}ning narxini kiriting: ")
#         narxlari[nom] = summa
#     return narxlari
    
# cars = ['rolse royse', 'alfa rameo', 'bmw', 'tesla', 'ferrari', 'lamborghini']


# narxlari = narxini_kirit(cars[:])

# print(narxlari)
# print(cars)

# print(id(narxini_kirit))
# print(id(cars))


# ______________________________*args / **kwargs________________________________________

# *args -> bitta yulduzcha degani, **kwargs -> ikkita yuzlud degani 

# *args qoyilgan argument istalgancha qiymat qabulqiladi
# def summa(*numbers):
#     # overall = 0
#     for i in numbers:
#         overall += i
#     return overall
# print(summa(1, 2, 7))


# __________________________________sum()________________________________________________

# sum() -> umumiy qiymatni qo'shib hisoblab beradi

# def somma(*raqamlar):
#     return sum(raqamlar)

# print(somma(1, 2, 3, 4, 5, 6, 7, 8, 9))



# def info(a, b, *info):
#     return a+b+sum(info)
# # print(info(1, 2))
# print(info(1, 2, 7, 5, 5, 5))

# **kwargs -> dictionaryga javob beradi

# def autoInfo(company, model, **information):
#     information['kompaniya'] = company
#     information['model'] = model
#     return information
# car1 = autoInfo("Rolls Royce", "Plantom", rangi='qora', year=2024, cost=55000) 
# print(car1)


# ___________________________________UYGA VAZIFA______________________________________________

# _____________1________________

# def narx(nomi):
#     prices = {}
#     while nomi:
#         name = nomi.pop()
#         som = int(input(f"{name.title()}ning narxini kiriting: "))
#         prices[name] = som
#     return prices

# books = ['tafsiri hilol'.title(), 'sarvari olam'.title(), 'Iymon', 'ibodati islomiya'.title()]


# prices = narx(books[:]) # [:] -> bu belgi books ro'yxati ichidagi malumotlarni saqlab qoladi
# print('\n', prices )


# _______________2______________

# def son(son):
#     yigindi = 0
#     for i in range(int(input("Nechta son kiritishni hojlaysiz: "))):
#         while i:
#             son = int(input(">>> "))
#             yigindi += son
#         return yigindi
    



# ________________3_______________



# _________________4_______________

# def country_info(davlat, poytaxt, aholi, til):
#     information = {
#         "Davlat": davlat,
#         "Poytaxti": poytaxt,
#         "Aholisi": aholi,
#         "Tili": til,
#     }
#     return information

# def save_country_info():
#     country = []
#     while True:
#         davlat = input("Davlat nomini kiriting: ")
#         poytaxt = input("Poytaxt nomini kiriting: ")
#         aholi = input("Aholisi sonini kiriting: ")
#         til = input("Rasmiy tilini kiriting: ")
#         country.append(country_info(davlat, poytaxt, aholi, til))

#         javob = input("Yana javob kiritishni hohlaysizmi? (yes/no): ").lower()
#         if javob!= "no":
#             break
#         return country


# print(save_country_info())

# _____________________________________________________________________________________


# def CountryInfo(**information):
#     return information
# country = CountryInfo(Davlat=input('Davlatni kiriting: ').title(), Poytaxt=input('Pytaxt nomi: ').title(),  Aholi=int(input('Aholisi sonini kiriting: ')), Til=input('Tili: ').title())
# print(country)


# _______________5_____________________

# def talaba_info(**malumotlar):
#     return malumotlar
# talaba = talaba_info(Talaba=input("Talaba ismi: ").title(), Familiyasi=input("Familiyasi: ").title(), 
# Otasi=input("Otasining ismi: ").title(), Yili=input("Tug'ilgan yili: "), Talim=input("O'qish joyini kiriting: ").capitalize(), Hobbi=input("Qiziqarli mashg'uloti: ").capitalize())

# print(talaba)







