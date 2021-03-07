while True:
    try:
        x1 = int(input("Unesite x1 koordinatu: "))
        break
    except ValueError:
        print("Netocan unos!")
while True:
    try:
        y1 = int(input("Unesite y1 koordinatu: "))
        break
    except ValueError:
        print("Netocan unos!")
while True:
    try:
        x2 = int(input("Unesite x2 koordinatu: "))
        break
    except ValueError:
        print("Netocan unos!")
while True:
    try:
        y2 = int(input("Unesite y2 koordinatu: "))
        break
    except ValueError:
        print("Netocan unos!")
a = (y2 - y1)/(x2 - x1)

print("y - {} = {} * x - {}".format(y1, a, x1))
