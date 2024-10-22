def autoInfo(made, model, color, engine, year, price=None):
    auto = {
        "Company": made,
        "Model": model,
        "Color": color,
        "Engine": engine,
        "Year": year,
        "Price": price
    }
    return auto

def auto_kirit():
    cars = []
    while True:
        made= input("Ishlab chiqargan kompaniya: ").upper()
        model = input("Model: ").upper()
        color = input("Color: ").title()
        engine = input("Engine: ").title()
        year = int(input("Year: "))
        price = int(input("Narxi: "))
        cars.append(autoInfo(made, model, color, engine, year, price))


        javob = input("Yana javob kiritishni hohlaysizmi? (yes/no): ").lower()
        if javob!= "no":
            break
        return cars


def info_cars(autoInfo):
    print(f"{autoInfo['Company'].title()}, "
    f"{autoInfo['Model'].title()}, "
    f"{autoInfo['Color']}, "
    f"{autoInfo['Engine']}, "
    f"{autoInfo['Year']}-yil, ${autoInfo['Price']}")

def daraja_hisoblovchi(a, b):
    return a ** b


# ___________________________UY VAZIFASI SHARTI_______________________________________

# _________________1_____________

def malumotlar():
    talabalar = []
    while True:
        ism = input("Ismingiz:")
        familiya = input("Familiya: ")
        yil = int(input("Yil: "))
        manzil = input("Manzil: ")
        talim = input("Oliy t'alim: ")
        talabalar.append(ism, familiya, yil, manzil, talim)
        javob = input("Yana javob kiritishni hohlaysizmi? (yes/no): ").lower()
        if javob!= "no":
            break
        return talabalar

# ________________2__________________

def country_info(*args):
    country = []
    while True:
        davlat = input("Davlat nomini kiriting: ")
        poytaxt = input("Poytaxt nomini kiriting: ")
        aholi = input("Aholisi sonini kiriting: ")
        til = input("Rasmiy tilini kiriting: ")
        country.append(country_info(davlat, poytaxt, aholi, til ))
        args = input("Yana javob kiritishni hohlaysizmi? (yes/no): ").lower()
        if args == "no":
            break
    return country




################

def son(son):
    for i in range(int(input("Nechta son kiritishni hojlaysiz: "))):
        yigindi = 0
        son = int(input(f"{i+1}-sonni kiriting: "))
        while son >= son:
            yigindi += i
        return yigindi










