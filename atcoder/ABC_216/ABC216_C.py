n = int(input())
s = ''

while n != 0:
    if n % 2 != 0:
        s += 'A'
        n -= 1
    else:
        s += 'B'
        n //= 2
    
print(s[::-1])