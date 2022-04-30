import sys

input = sys.stdin.readline

string = input()
string = list(string)

s = string[0]
ans = 0

for st in string:
    if s == st:
        ans += 1
if ans == 3:    
    print('Won')
else:
    print('Lost')