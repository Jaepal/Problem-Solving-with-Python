num = 600851475143
i = 2
lst = []
while True:
    if num % i == 0:
        lst.append(i)
        num /= i
        if num == 1:
            print(max(lst))
            break
    else:
        i += 1