'''
LeetCode 412. Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.
'''


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    lst = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 15 != 0:
            lst.append('Fizz')
        elif i % 5 == 0 and i % 15 != 0:
            lst.append('Buzz')
        elif i % 15 == 0:
            lst.append('FizzBuzz')
        else:
            lst.append(str(i))
    return lst


# 더 짧은 코드
def fizzBuzz2(n):
    """
    :type n: int
    :rtype: List[str]
    """
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]