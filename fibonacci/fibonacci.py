# -*- coding: utf-8 -*-


def fibonacci(n):
    """Calulcates the fibonacci number.

    :param n: The input for which the fibonacci number is calculated.
    :type n: Integer
    :return: The fibonacci number.
    :rtype:
    """
    if n < 0 or not isinstance(n, int):
        raise ValueError("%s is not a natural number. Only natural numbers are allowed." % n)
    a, b = 0, 1
    while n != 0:
        a, b = b, a+b
        n -= 1
    return int(a)


