t = int(input())

for _ in range(t):
    length = int(input())
    b = str(input())
    a = ['1']
    tmp = 1
    for i in range(1, length):
        if b[i-1] == b[i]:
            if tmp == 1:
                a.append('0')
                tmp = 0
            else:
                a.append('1')
                tmp = 1
        elif b[i-1] != b[i]:
            if b[i] == '0' and tmp == 0:
                a.append('0')
                tmp = 0
            else:
                a.append('1')
                tmp = 1
    a = ''.join(a)
    print(a)