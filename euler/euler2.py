result = 2
f1, f2, f3 = 1, 2, 0
while True:
    f3 = f1 + f2
    if f3 >= 4000000:
        break
    if f3 % 2 == 0:
        result += f3
    f1 = f2
    f2 = f3