#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    elif n > 1:
        func(n - 1, a, c, b)
        print(a, '-->', c)
        func(n - 1, b, a, c)
    else:
        print("n值输入错误")


if __name__ == '__main__':
    func(3,'A','B','C')
