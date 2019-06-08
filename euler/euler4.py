i = 999
p = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        num = i * j
        rev = str(num)[::-1]
        if str(num) == rev:
            p.append(num)
print(max(p))