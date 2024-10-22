# __________________________________________________DEF - 2_____________________________________________


# Qiymat qaytaruvchi funksiya:

# def ism_familiya(ism, familiya):
#     toliq_ism = f"{ism} {familiya.upper()}"
#     return toliq_ism # o'zidan qiymat qaytaradi, terminalda qiymat chiqishiga javob bermaydi

# print(ism_familiya('rahmatulla', 'alimjonov'))


# def ism_familiya(ism, familiya, otasining_ismi=''): #otasining_ismiga standart qiymat berildi -> bosh katak
#     if otasining_ismi:
#         toliq_ism = f"{ism} {familiya} {otasining_ismi}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism

# print(ism_familiya('moxiraxon', 'fayzullayeva', '5'))
# print(ism_familiya('moxiraxon', 'fayzullayeva', 'abduxalil qizi'))
# print(ism_familiya('moxiraxon', 'fayzullayeva'))

# def auto_info(made, model, color, engine, year, price=None):
#     auto= {
#         "Company": made,
#         "Model": model,
#         "Color": color,
#         "Engine": engine,
#         "Year": year,
#         "Price": price
#     }
#     return auto

# car1 = auto_info("Chevrolet", "Malibu 2 Turbo", "qora", "avtomat", 2024, 35_000)
# car2 = auto_info("Deawoo", "Nexia 3", "oq", "avtomat", 2020, 15_000)
# car3 = auto_info("Zeekr", "007", "red", "avtomat", 2024, 50_000)

# cars = (car1, car2, car3)
# for i in cars:
#     # print(i.values())
#     # print(i["Company"])
#     # print(i)
#     if i["Price"]:
#         price = i["Price"]
#     else:
#         price = "Noma'lum!"
#     print(f"{i['Company']}, {i['Model']}, Narxi: {price}")



# def auto_info(made, model, color, engine, year, price=None):
#     auto= {
#         "Company": made,
#         "Model": model,
#         "Color": color,
#         "Engine": engine,
#         "Year": year,
#         "Price": price
#     }
#     return auto


# car = []
# while True:
#     made = input("Ishlab chiqargan kompaniya: ").upper()
#     model = input("Model: ").upper()
#     color = input("Color: ").title()
#     engine = input("Engine: ").title()
#     year = input("Year: ")
#     price = input("Price: ")
#     car.append(auto_info(made, model, color, engine, year, price))
#     answer = input("Answer: ").lower()
#     if answer == "yes":
#         continue
#     else:
#         break
# print(car, '\n')

# # range ishlash funksiyasi

# def masofa(min, max):
#     number = []
#     while min < max:
#         number.append(min)
#         min += 1
#     return number
# print(masofa(0, 10))

# # optimal varianti

# def oraliq(min, max, step=''):
#     numbers = []
#     while min < max:
#         numbers.append(min)
#         min += step
#     return numbers

# print(oraliq(0, 21, 2))


# _________________________________________DEF-2 UY ISHI______________________________________________________________________

# _________________1__________________

# def malumotlar(**informations):
#     return informations

# for i in range(int(input("Nechta odam ma'lumot kiritadi: "))):
#     info = malumotlar(name=input(f"{i+1}. Ismingiz: ").capitalize(), surname=input(f"{i+1}. Familiya: ").capitalize(), year=input(f"{i+1}. Yilingiz: "),
#                     born=input(f"{i+1}. Tug'ilgan joy: ").capitalize(), gmail=input(f"{i+1}. Elektron manzil: "), number=input(f"{i+1}. Telefon: "))
#     i += 1
#     print(info)


# __________________2_________________


# def son(son1, son2):
#     return max(son1, son2)
# print(son(int(input("1-sonni kiriting: ")), int(input("2-sonni kiriting: "))))


# ___________________3_________________

# def digit(a, b):
#     return a ** b
# print(digit(int(input("A sonni kiriting: ")), int(input("B sonni kiriting: "))))




















