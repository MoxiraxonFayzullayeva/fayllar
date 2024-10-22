# ________________________FASTFOOD PROJECT_______________________________



# ismlar = ["Rahmatilla", "Alimjon", "Moxiraxon"]
# t_yillar = [1995, 1998, 2006]


# dct = {}

# for key, value in zip(ismlar, t_yillar):
#     dct[key] = value
# print(dct)


# kinolar = []
# k = 1
# while True:
#     kino = input(f"{k}-yoqtirgan film kiriting: ")
#     kinolar.append(kino)
#     javob = input("Yana kino qoshishni istaysizmi? (ha/yo'q): ")
#     if javob.lower() == 'ha':
#         continue
#     else:
#         break

# print("\nRo'yxat tuzildi!")
# for i in kinolar:
#     print(i.title())


# filmlar = {}
# ishora = True

# while ishora:
#     nomi = input("Rejissior kiriting: ")
#     film = input(f"{nomi.title()}ning filmini kiriting: ")
#     filmlar[nomi] = film

#     answer = input("Yana ma'lumot qo'shasizmi? (yes/no): ").lower()
#     if answer == 'no':
#         ishora = False

# for ism, film in filmlar.items():
#     print(f"{ism.title()}: {film.title()}.")


# odamlar = ['alim', 'moxir', 'raxmatulla', 'otajon', 'alim', 'alim', 'odina', 'alim', 'alim', 'alim',]

# while 'alim' in odamlar:
#     odamlar.remove('alim')
# print(odamlar)

# students = ['moxira', 'raxmatulla', 'otajon', 'odina']
# baholanganlar = {}

# while students:
#     student = students.pop()
#     baho = int(input(f"{student.title()}ning bahosini kiriting: "))
#     print(f"{student.title()} baholandi!")
#     baholanganlar[student] = baho
# print(baholanganlar)



# menu = {
#     'lavash': {
#         'l_oddiy': 25_000,
#         'l_tovuqli': 35_000,
#         'l_goshtli': 40_000,
#         'l_qazili': 50_000,
#         'l_sirli': 45_000,
#     },
#     'pizza': {
#         'p_oddiy': 40_000,
#         'p_peperoniy': 45_000,
#         'p_danar': 65_000,
#         'p_sirli': 70_000,
#     },
#     'ichimlik': {
#         'coca cola': 18_000,
#         'fanta': 20_000,
#         'sprite': 18_000,
#         'pepsi': 16_000,
#         'flesh': 16_000
#     }
# }

# hisob = 0

# for i in menu:
#     print(f"\n{i.upper()}: ")
#     son = 1
#     for k, v in menu[i].items():
#         print(f"\t{son}. {k.title()} -------------------- {v:,.0f} so'm.")
#         son += 1

# client = {}

# while True:
#     buyurtma = input("Nima buyurtma berasiz: ").lower()
#     for i in menu:
#         if buyurtma in menu[i]:
#             print(f"{menu[i][buyurtma]} so'm.")
#             client[buyurtma] = menu[i][buyurtma]
#             hisob += menu[i][buyurtma]
#             break
#     else:
#         if buyurtma in ['stop', 'exit']:
#             for k, v in client.items():
#                 print(f'{k.upper()} ---------------------- {v} so\'m.')
#             print(f"\nUMUMIY HISOB: {hisob} so'm.")
#             break
#         else:
#             print("Bunday taom mavjud emas!")



class A:
    a = 5
    class Meta:
        abstarct = True

class B:
    b = A.a
print(B.b)
