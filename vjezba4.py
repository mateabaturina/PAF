def jednadzba_pravca(x1, y1, x2, y2):
    a = (x2 - x1)/(y2 - y1)
    return a
x1 = int(input("Unesite x1 koordinatu: "))
y1 = int(input("Unesite y1 koordinatu: "))
x2 = int(input("Unesite x2 koordinatu: "))
y2 = int(input("Unesite y2 koordinatu: "))
    
a = jednadzba_pravca(x1, y1, x2, y2)
print("y - {} = {} * x - {}".format(y1, a, x1))
