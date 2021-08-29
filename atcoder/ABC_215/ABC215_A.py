import sys

input = sys.stdin.readline


string = input()
check = 'Hello,World!'

if len(string) == len(check):
    for n in range(0, len(string)):
        if string[n] == check[n]:
            continue
        else:
            print('WA')
            break
    print('AC')
else:
    print('WA')