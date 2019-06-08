num = 0
for i in range(1, 101):
    for j in range(i+1, 101):
        num += i * j
print(2*num)



# 더 나은 풀이
n = range(1, 101)
square = lambda x: x**2
print(square(sum(n)) - sum(map(square, n)))