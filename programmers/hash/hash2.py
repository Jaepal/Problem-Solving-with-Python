"""
해시 2  - 전화번호 목록
"""

def solution(phone_book):
    d = {}
    for number in phone_book:
        for i in range(len(number)):
            string = number[:i+1]
            d[string] = d.get(string, 0) + 1
    for number in phone_book:
        if d[number] >= 2:
            return False
    return True