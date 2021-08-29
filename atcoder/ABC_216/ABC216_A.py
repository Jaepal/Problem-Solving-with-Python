n = input()

x, y = n.split('.')
y = int(y)
s = ''
if y <= 2:
    s = '-'
elif y >= 3 and y <= 6:
    s = ''
elif y >= 7:
    s = '+'

print(x + s)