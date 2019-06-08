num = 20
stack = 0
while True:
    for i in range(20, 0, -1):
        if num % i == 0:
            stack += 1
        else:
            break
    if stack == 20:
        result = num
        break
    num += 20
    stack = 0