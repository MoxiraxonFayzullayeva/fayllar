# obbo
# muqum
# matn = input(">>> ")
# print(matn == matn[::-1])

# _______________________________________________________________________________

# number = int(input("Son kiriting: "))
# print(number+(number % 2))

# a = [6, 9, 12, 18, 24, 36, 45, 72]
# s = 1

# for i in range(len(a)):
#     if a[i] % 6 == 0:
#         a[i] = s
#         s += 1
# print(a)

# _______________________________________________________________________________
# cars = {}


# dasturchilar = {
#     'ismi': ['abdulloh'],
#     'familoiyasi': ['najibov'],
#     'rahmatilla': ['python'],
#     'alimjon': ['python', 'java']
# }
# for name, languages in dasturchilar.items():
#     print(f"\n{name.title()}:", end=" ")
#     for o in languages:
#         if o == languages[-1]:
#             print(f"{o.upper()}", end=".")
#         else:
#             print(o.upper(), end=", ")
    
# for name, languages in dasturchilar.items():
#     print(f"\n{name.title()}:", end=" ")
#     for o in languages:
#         if o == languages[-1]:
#             print(f"{o.upper()}", end=".")
#         else:
#             print(o.upper(), end=", ")

# ______________________________________________________________________________________

# # 
# user = input("O'zingiz haqida ma'lumot kiriting: ")
# soz = ' '
# unlilar = ['a', 'e', 'i', 'o', 'u']

# for i in user:
#     if i == 'a' or 'e' or 'i' or 'o' or 'u':
#         soz += '$'
#     else:
#         continue

# juft = []
# toq = []

# son = 1 
# while son <= 101:
#     if i 











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


# **kwargs
# def auotInfo(company, model, **information):
#     information['kompaniya'] = company
#     information['Modeli'] = model
#     return information
# car1 = auotInfo("Rolls Royce", "Phantom", rangi='qora', yili=2024, narxi=55000)
# print(car1)
















# print(map(a=int(input("A: ")) + b=int(input("B: "))))

# print(filter(lambda x: x % 2 == 0, range(1, 21)))

# print(int(input("A: ")) + int(input("B: ")))
# print(int(input("A: ")) ** int(input("B: ")))


# a, b = int(input("A: ")), int(input("B: "))


# import random as r
# print(list(filter(lambda x: x % 2 == 0, r.sample(range(100), 10))))



# from math import sqrt
# print(list(map(sqrt, range(11))))



# a,b = map(int, input().split())
# print(a+b)






# import random as r
# def juft(x):
#     return x % 2 == 0
# print(list(filter(juft, r.sample(range(100), 10))))  



















# a = 257
# b = 257
# resul = id(a) == id(b)
# print(resul)
# print(id(a))
# print(id(b))

# t = (1,[2,3])
# t[1].append(4)
# print(t)


# x = [1,2]
# y = x
# result = id(x) == id(y)
# print(result)
# print(id(x))
# print(id(y))




# def ildiz(a):
#     return a










import os
os.system("cls")

k = input("Kunni kiriting: ").lower()
y = int(input("Yoshni kiriting: "))

if k == "juma" and y <= 7:
    print("Tekin!")
elif y > 7 and y <= 18:
    print(25_000)
else:
    print(65_000)
