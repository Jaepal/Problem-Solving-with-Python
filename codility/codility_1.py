'''
def solution(N):
    while(N<=0)
'''
N = 564
bn = ''
tmp = 0
tmp_loc = 0
flag = False

while N > 0:
    if N % 2 == 1:
        if flag:
            tmp = tmp if tmp > tmp_loc else tmp_loc
        tmp_loc = 0
        flag = True
        bn = '1' + bn
    elif N % 2 == 0:
        bn = '0' + bn
        tmp_loc = tmp_loc + 1
    N = N//2
return tmp