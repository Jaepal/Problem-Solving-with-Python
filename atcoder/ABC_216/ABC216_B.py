n = int(input())
l = []

for _ in range(n):
    l.append(input())

l_set = list(set(l))

if len(l) != len(l_set):
    print('Yes')
else:
    print('No')