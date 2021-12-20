"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    l=[num**2 for num in args]
    return l
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    if num == 1 or num == 0:
        return False
    counter = 0
    div_max = num//2
    for div in range(2,div_max+1):
        if num % div == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False

def filter_numbers(l,type):
    if type==ODD:
        list_fltr=list(filter((lambda x: x % 2 == 1),l))
    if type==EVEN:
        list_fltr=list(filter((lambda x: x % 2 == 0),l))
    if type==PRIME:
        list_fltr=list(filter((lambda x: is_prime(x)),l))
    return list_fltr

    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
