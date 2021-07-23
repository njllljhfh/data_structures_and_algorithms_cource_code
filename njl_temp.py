# -*- coding:utf-8 -*-

def factorial(n):
    print(dir(), vars())
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    # print(factorial(0))
    print(factorial(5))
